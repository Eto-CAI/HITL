#	人機械協調	20231128_プロト実装

#	ディレクトリ構成
#	[current directory]
#	SCOEngineController			ライブラリディレクトリ
#		__init__.py				ライブラリ設定
#		library.py				python側ラッパ-－ライブラリ
#		SCOEngineController.dll	エンジン本体
#       SimData                 エンジン入出力CSV一式

#	使用ライブラリ(必須)
import pandas as pd
import datetime
#	SCOエンジンコントローラライブラリ本体
import SCOEngineController as SCO

#マスタパラメータ
step = 7 #KPI確認日数
comp = ("Factory").encode('utf-8') #着目企業

#マスタ読込み->後々使うかどうかは不明
item_master= pd.read_csv("SimData/data/ItemMaster.csv")
comp_master= pd.read_csv("SimData/data/CompanyIS.csv")
tran_master = pd.read_csv("SimData/data/TransportMaster.csv")
bom_master = pd.read_csv("SimData/data/BOM.csv")
demand = pd.read_csv("SimData/data/ActualDemand.csv")


#Dir設定
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
print(Rtn) #念のため確認
print(1)

prod_ofrs={}
#KPI確認(需要充足率)
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
print(ofr_each_item_averages)
print(2)

#各itemごとの平均需要予測量を計算
average_demand_per_item = demand.groupby('ItemID')['DemandQty'].mean()
print(average_demand_per_item)
print(3)

#需要充足できない数量が多いほどKPIが悪い(KPIが低い)
#需要非充足量 = 各商品毎の平均需要非充足率 * 各商品毎の平均需要量
unfulfilled_demand_quantity = (1 - pd.Series(ofr_each_item_averages)) * average_demand_per_item
print(unfulfilled_demand_quantity)
print(4)

#DFに加工
unfulfilled_demand_quantity = pd.DataFrame(unfulfilled_demand_quantity)
unfulfilled_demand_quantity = unfulfilled_demand_quantity.reset_index()
unfulfilled_demand_quantity = unfulfilled_demand_quantity.rename(columns={'index':"#ParentItemID"})
print(unfulfilled_demand_quantity)
print(5)

#関連子品目を取得
child_items = pd.merge(unfulfilled_demand_quantity, bom_master)
child_items.columns=["#ParentItemID","unfulfilled_demand_quantity","ItemID","Consumption"]
print(child_items)
print(6)

#子品目調達LTを取得し、KPI計算
#KPIが低いもの＝対策が必要
#KPI = 1 / (需要非充足量 * 子品目の調達LT)
proc_LT = pd.merge(child_items, tran_master, on="ItemID")
Coef = 1000
proc_LT["KPI_score"] = Coef / (proc_LT["unfulfilled_demand_quantity"] * proc_LT["OrderFixedPeriod"])
proc_LT.loc[proc_LT["unfulfilled_demand_quantity"] == 0, "KPI_score"] = 1
proc_LT = proc_LT.sort_values(by="KPI_score")

print(proc_LT["OrderFixedPeriod"])
print(7)
print(proc_LT)
