#	人機械協調	20231128_プロト実装

#	ディレクトリ構成
#	[current directory]
#	SCOEngineController			ライブラリディレクトリ
#		__init__.py				ライブラリ設定
#		library.py				python側ラッパ-－ライブラリ
#		SCOEngineController.dll	エンジン本体
#       SimData                 エンジン入出力CSV一式

# BOM構成拡張・員数拡張　テスト項目
# [[A,partsA,1],[B,partsB,1],[C,partsC,1]] 1:1 員数単数〇
# [[A,partsA,2],[B,partsB,3],[C,partsC,4]] 1:1 員数複数〇
# [[A,partsA,1],[B,partsA,1],[C,partsC,1]] 1:M 員数単数〇
# [[A,partsA,1],[B,partsA,2],[C,partsC,1]] 1:M 員数複数〇
# [[A,partsA,1],[A,partsB,1],[C,partsC,1]] M:1 員数単数〇
# [[A,partsA,1],[A,partsB,2],[C,partsC,1]] M:1 員数複数〇
# [[A,partsA,1],[A,partsB,1],[B,partsA,1],[B,partsA,1]] M:N 員数単数〇
# [[A,partsA,1],[A,partsB,2],[B,partsA,3],[B,partsA,4]] M:N 員数複数〇
# 

#	使用ライブラリ(必須)
import pandas as pd
import datetime
#	SCOエンジンコントローラライブラリ本体
import SCOEngineController as SCO

# マスタパラメータ
step = 7 #KPI確認日数]
comp = ("Market").encode('utf-8') #着目企業

# マスタ読込み->後々使うかどうかは不明
item_master= pd.read_csv("SimData/data/ItemMaster.csv")
comp_master= pd.read_csv("SimData/data/CompanyIS.csv")
tran_master = pd.read_csv("SimData/data/TransportMaster.csv")
bom_master = pd.read_csv("SimData/data/BOM.csv")
demand = pd.read_csv("SimData/data/ActualDemand.csv")

# Dir設定
XML_Path = ("SCSimEngine.xml").encode('utf-8')
Input_Path = ("SimData/data").encode('utf-8')
Output_Path = ("SimData/out").encode('utf-8')
Log_Path = ("SimData/log").encode('utf-8')
#	XMLファイル設定
Rtn = SCO.set_env_XML(XML_Path)
#	入出力ディレクトリ設定
Rtn = SCO.set_env_InputDir(Input_Path)
Rtn = SCO.set_env_OutputDir(Output_Path)
Rtn = SCO.set_env_LogDir(Log_Path)
#	入力ファイル設定
Rtn = SCO.set_input()
print("1_ErrorCheck")
print(Rtn) #念のため確認

prod_ofrs={}
# KPI確認(需要充足率)
for i in range(0, 181, 7): #(start, stop, step)
    SCO.step(step)
    for item in bom_master["#ParentItemID"]:
        item_enc = item.encode('utf-8')
        ofr = SCO.get_kpi_order_fill_rate_d1(comp, item_enc)

        if item not in prod_ofrs:
            prod_ofrs[item]=[]
        prod_ofrs[item].append(ofr)
        #print("Item=    ", item, "  osfr=    ", ofr)

# 各itemごとの平均需要充足率を計算
ofr_each_item_averages = {}
for item, ofr in prod_ofrs.items():
    average_value = sum(ofr) / len(ofr) if ofr else 0  # 0で割り算を防ぐための条件分岐
    ofr_each_item_averages[item] = average_value
print("\n2_ofr_each_item_averages")
print(ofr_each_item_averages)

# 各itemごとの平均需要予測量を計算
average_demand_per_item = demand.groupby('ItemID')['DemandQty'].mean()
print("\n3_average_demand_per_item")
print(average_demand_per_item)

# 需要充足できない数量が多いほどKPIが悪い(KPIが低い)
# 需要非充足量 = 各商品毎の平均需要非充足率 * 各商品毎の平均需要量
unfulfilled_demand_quantity = (1 - pd.Series(ofr_each_item_averages)) * average_demand_per_item

# DFに加工
unfulfilled_demand_quantity = pd.DataFrame(unfulfilled_demand_quantity)
unfulfilled_demand_quantity = unfulfilled_demand_quantity.reset_index()
unfulfilled_demand_quantity = unfulfilled_demand_quantity.rename(columns={'index':"#ParentItemID"})
print("\n4_unfulfilled_demand_quantity")
print(unfulfilled_demand_quantity)

# 子品目・員数取得
child_items = pd.merge(unfulfilled_demand_quantity, bom_master)
child_items.columns=["#ParentItemID","Unfulfilled_Demand_Quantity","ChildItemID","Consumption"]
print("\n5_with_bom_master")
print(child_items)

# 親品目ごとに需要非充足量を集計
child_items["Unfulfilled_Demand_Quantity_with_consumption"] = child_items["Unfulfilled_Demand_Quantity"] * child_items["Consumption"]
print("\n6_Unfulfilled_Demand_Quantity_with_consumption")
print(child_items)

# 子品目ごとに需要非充足量を集計
child_items = child_items.groupby('ChildItemID')["Unfulfilled_Demand_Quantity_with_consumption"].sum()
child_items = child_items.reset_index(drop=False)
child_items.columns = ["ItemID", "Unfulfilled_Demand_Quantity_with_consumption"]
print("\n7_unfulfilled_demand_quantity_per_child_items")
print(child_items)

# Tran_masterをマージし、子品目調達LTを取得
kpi_calc = pd.merge(child_items, tran_master[["ItemID","OrderFixedPeriod"]], on="ItemID")
print("\n8_with_tran_master")
print(kpi_calc)

# KPI計算：KPIが低いもの＝対策が必要
# KPI = 係数 / (需要非充足量 * 員数 * 子品目の調達LT)
Coef = 1000
kpi_calc["KPI_score"] = Coef / (kpi_calc["Unfulfilled_Demand_Quantity_with_consumption"] * kpi_calc["OrderFixedPeriod"])
kpi_calc.loc[kpi_calc["Unfulfilled_Demand_Quantity_with_consumption"] == 0, "KPI_score"] = 1

# 結果をsortして確認
kpi_calc = kpi_calc.sort_values(by="KPI_score")
print("\n9_kpi_calc")
print(kpi_calc)
