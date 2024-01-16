#	SCOEngineController実行テスト	20220824

#	ディレクトリ構成
#	[current directory]
#	SCOEngineController			ライブラリディレクトリ
#		__init__.py				ライブラリ設定
#		library.py				python側ラッパ-－ライブラリ
#		SCOEngineController.dll	エンジン本体

#	---------------------------------------------------------------------------
#	スクリプト実行サンプル
#	pythonにて実行する際の動作セット

#	---------------------------------------------------------------------------
#	以下コマンドライン実行サンプル
#	---------------------------------------------------------------------------
#	使用ライブラリ(必須)
import pandas
import datetime
#	SCOエンジンコントローラライブラリ本体
import SCOEngineController

#	---------------------------------------------------------------------------
#	山口様データ

wXMLPath = ("SCSimEngine.xml").encode('utf-8')
wInputPath = ("テストデータ/data").encode('utf-8')
wOutputPath = ("テストデータ/result/out").encode('utf-8')
wLogPath = ("テストデータ/result/log").encode('utf-8')
#	XMLファイル設定
wRtn = SCOEngineController.set_env_XML(wXMLPath)
#	入出力ディレクトリ設定
wRtn = SCOEngineController.set_env_InputDir(wInputPath)
wRtn = SCOEngineController.set_env_OutputDir(wOutputPath)
wRtn = SCOEngineController.set_env_LogDir(wLogPath)
#	入力ファイル設定
wRtn = SCOEngineController.set_input()
print(wRtn)

#	---------------------------------------------------------------------------

#	実行(終了まで)
#wRtn = SCOEngineController.step()
#print(wRtn)
#	実行(1日)
SCOEngineController.step(1)
wCorpStr = ("CI003").encode('utf-8')
wItemStr = ("P1").encode('utf-8')
wRtn = SCOEngineController.set_SC_incident_inventory_qty(wCorpStr,wItemStr,100)
#wProdList = SCOEngineController.get_SC_incident_prodWIP_list()
#wRtn = SCOEngineController.set_SC_incident_prodWIP_qty(0,33)
SCOEngineController.step(3)
wRtn = SCOEngineController.set_SC_incident_inventory_qty(wCorpStr,wItemStr,30) 
wRtn = SCOEngineController.step()
print(wRtn)
#	実行(3日)
SCOEngineController.step(3)

#	---------------------------------------------------------------------------
#	結果確認

#	日毎保管量
wList = SCOEngineController.get_sim_result_daily_InventoryActual()
print(wList)

#	日毎出庫実績
wList = SCOEngineController.get_sim_result_daily_ShipActual()
print(wList)

#	イベント出庫実績
wList = SCOEngineController.get_sim_result_event_ShipActual()
print(wList)

#	ログ注文
wList = SCOEngineController.get_sim_result_log_PurchaseOrder()
print(wList)

#	---------------------------------------------------------------------------
#	実行前に戻す
wRtn = SCOEngineController.reset()
print(wRtn)

#	---------------------------------------------------------------------------
#	破棄(設定からやりなおし)
SCOEngineController.dispose()

#	---------------------------------------------------------------------------
#	環境設定例

#	結果ファイル出力設定(0…出力しない 0以外…出力)
wSecStr = 'Daily'.encode('utf-8')
wFileStr = 'ShipActual'.encode('utf-8')

wSecStr = 'event'.encode('utf-8')

wSecStr = 'log'.encode('utf-8')
wFileStr = 'PurchaseOrder'.encode('utf-8')

wRtn = SCOEngineController.set_env_LogOutputControl(wSecStr, wFileStr, 0)
print(wRtn)

#	結果保存設定(0…保存しない 0以外…保存)

wRtn = SCOEngineController.set_env_LogSaveControl(wSecStr, wFileStr, 0)
print(wRtn)


#	---------------------------------------------------------------------------
#	最小有効量の算出用除数桁数設定
wRtn = SCOEngineController.set_env_MinEffectNumDigit(3)
print(wRtn)

wRtn = SCOEngineController.set_env_MinEffectNumDigit()
print(wRtn)

#	BoxOFRデフォルト値設定
wRtn = SCOEngineController.set_env_BoxOFR(0.5)
print(wRtn)

wRtn = SCOEngineController.set_env_BoxOFR()
print(wRtn)

#	省略時通貨為替レート値設定
wRtn = SCOEngineController.set_env_DefaultExchangeRate(1.5)
print(wRtn)

wRtn = SCOEngineController.set_env_DefaultExchangeRate()
print(wRtn)


#	---------------------------------------------------------------------------
#	KPI計算	山口様データ

#	需要充足率計算

wCorpStr = ("WH_CHUGOKU").encode('utf-8')
wItemStr = ("CVVP5W").encode('utf-8')

wRtn = SCOEngineController.get_kpi_order_fill_rate(wCorpStr, wItemStr)
wRtn = SCOEngineController.get_kpi_order_fill_rate()
print(wRtn)

#	平均在庫計算
wCorpStr = ("WH_CHUGOKU").encode('utf-8')
wItemStr = ("CVVP5W").encode('utf-8')
wRtn = SCOEngineController.get_kpi_average_inventoryQty(wCorpStr, wItemStr)
print(wRtn)

#	---------------------------------------------------------------------------
#	KPI計算	需要優先度

#	需要充足率計算
wCorpStr = ("C2000000").encode('utf-8')
wItemStr = ("P00002").encode('utf-8')
SCOEngineController.get_kpi_order_fill_rate(wCorpStr, wItemStr)

#	需要充足率計算(平均計算)
SCOEngineController.get_kpi_order_fill_rate_d1(wCorpStr, wItemStr)

#	平均在庫計算
wRtn = SCOEngineController.get_kpi_average_inventoryQty(wCorpStr, wItemStr)

SCOEngineController.step(2)
SCOEngineController.get_kpi_order_fill_rate(wCorpStr, wItemStr)
SCOEngineController.step(1)
SCOEngineController.get_kpi_order_fill_rate(wCorpStr, wItemStr)
#7/6には出る。

#	---------------------------------------------------------------------------
#	KPI計算		CO2

#	需要充足率計算
wCorpStr = ("WH_CHUGOKU").encode('utf-8')
wItemStr = ("RZTS105MR").encode('utf-8')

wRtn = SCOEngineController.get_kpi_order_fill_rate(wCorpStr, wItemStr)
print(wRtn)


#	平均在庫計算
wCorpStr = ("FAC_02").encode('utf-8')
wItemStr = ("RZV100EMW").encode('utf-8')
wRtn = SCOEngineController.get_kpi_average_inventoryQty(wCorpStr, wItemStr)
print(wRtn)

#	CO2排出量計算	CO2
wCorpStr = ("FAC_02").encode('utf-8')
wItemStr = ("RZV100EMW").encode('utf-8')

wCorpStr = ("L0017").encode('utf-8')
wItemStr = ("RZV100EMK").encode('utf-8')
wRtn = SCOEngineController.get_kpi_CO2(wCorpStr, wItemStr)
print(wRtn)

#	---------------------------------------------------------------------------
#	入力値変更例
#	実需

#	実行前に戻す
SCOEngineController.reset()

wList = SCOEngineController.get_input_ActualDemand()
print(wList)
print(wList.iat[0,3])
print(wList.iat[0,4])
wList.iat[0,4] = 123
wList.iat[1,4] = 234
wList.iat[169,4] = 456


wList.iat[556,4] = 999

SCOEngineController.set_input_ActualDemand(wList)

SCOEngineController.step()
#	---------------------------------------------------------------------------
#	需要予測

wList = SCOEngineController.get_input_DemandForecast()
print(wList)
wTemp = wList[15:20]
print(wTemp)
print(wTemp.iat[4,6])
wTemp.iat[4,6] = 999

SCOEngineController.set_input_DemandForecast(wTemp)

#	---------------------------------------------------------------------------
#	安全在庫

wList = SCOEngineController.get_input_SafetyStock()
print(wList)

wTemp = wList[112:114]
print(wTemp)

wTemp.iat[0,4] = 567
wTemp.iat[0,5] = 456
wTemp.iat[0,6] = 345
wTemp.iat[0,7] = 23.45
wTemp.iat[0,8] = 123

wRtn = SCOEngineController.set_input_SafetyStock(wTemp)

#	---------------------------------------------------------------------------
#	エージェント振る舞い

wList = SCOEngineController.get_input_AgentIS()
print(wList)

wTemp = wList[112:114]
print(wTemp)

wTemp.iat[0,3] = 'LP_proc_06'

wRtn = SCOEngineController.set_input_AgentIS(wTemp)

#	---------------------------------------------------------------------------
#	TransportMaster
wList = SCOEngineController.get_input_TransportMaster()
print(wList)

wTargetCorpID = ("CI011").encode('utf-8')
wTargetItemID = ("P0000000001").encode('utf-8')
wTargetTranType = 1

wList = SCOEngineController.get_input_TransportMaster(wTargetCorpID)
wList = SCOEngineController.get_input_TransportMaster(wTargetCorpID, wTargetItemID)
wList = SCOEngineController.get_input_TransportMaster(wTargetCorpID, wTargetItemID, wTargetTranType)
wList = SCOEngineController.get_input_TransportMaster(ItemID=wTargetItemID)
wList = SCOEngineController.get_input_TransportMaster(ItemID=wTargetItemID, TransportType=wTargetTranType)
wList = SCOEngineController.get_input_TransportMaster(wTargetCorpID, TransportType=wTargetTranType)

print(wList)

wCorpStr = ("CI003").encode('utf-8')
wItemStr = ("P0000000001").encode('utf-8')

wRtn = SCOEngineController.get_kpi_order_fill_rate(wCorpStr, wItemStr)
print(wRtn)

SCOEngineController.set_input_TransportMaster_alloc_rate(1,110)
SCOEngineController.set_input_TransportMaster_tran_type(1,5)
SCOEngineController.set_input_TransportMaster_LT(1, 4)

SCOEngineController.set_input_TransportMaster_LT(1, 'TranLT', 3)
SCOEngineController.set_input_TransportMaster_LT(1, 'OrderFixedPeriod', 5)

SCOEngineController.set_input_TransportMaster_alloc_rate(5,0)
SCOEngineController.set_input_TransportMaster_alloc_rate(6,100)
SCOEngineController.set_input_TransportMaster_alloc_rate(7,100)
SCOEngineController.set_input_TransportMaster_alloc_rate(8,100)

SCOEngineController.update_TransportMaster()
#	---------------------------------------------------------------------------
#	需要充足率計算
wCorpStr = ("C2000000").encode('utf-8')
wItemStr = ("P00002").encode('utf-8')

SCOEngineController.get_kpi_order_fill_rate()

wCorpStr = ("CI001").encode('utf-8')
wCorpStr = ("CI002").encode('utf-8')
wCorpStr = ("CI003").encode('utf-8')

SCOEngineController.get_kpi_order_fill_rate()
SCOEngineController.get_kpi_order_fill_rate(wCorpStr)
SCOEngineController.get_kpi_order_fill_rate(wCorpStr, wItemStr)
SCOEngineController.get_kpi_order_fill_rate(ItemID = wItemStr)

wCorpStr = ("MKT_21_WH_CHUGOKU").encode('utf-8')
wItemStr = ("CVVP5W").encode('utf-8')

#	---------------------------------------------------------------------------
#	平均在庫計算
wCorpStr = ("FAC_02").encode('utf-8')
wItemStr = ("PVBL50JN").encode('utf-8')

wCorpStr = ("CI003").encode('utf-8')
wItemStr = ("P0000000004").encode('utf-8')

SCOEngineController.get_kpi_average_inventoryQty()
SCOEngineController.get_kpi_average_inventoryQty(wCorpStr)
SCOEngineController.get_kpi_average_inventoryQty(ItemID = wItemStr)
SCOEngineController.get_kpi_average_inventoryQty(wCorpStr, wItemStr)

SCOEngineController.get_kpi_average_inventoryAmount()
SCOEngineController.get_kpi_average_inventoryAmount(wCorpStr)
SCOEngineController.get_kpi_average_inventoryAmount(ItemID = wItemStr)
SCOEngineController.get_kpi_average_inventoryAmount(wCorpStr, wItemStr)

#	---------------------------------------------------------------------------
#	制約値設定

import pandas
import datetime
import SCOEngineController

wXMLPath = ("あああ/SCSimEngine.xml").encode('utf-8')
wInputPath = ("テストデータ/data_test230110").encode('utf-8')
wOutputPath = ("テストデータ/result/out").encode('utf-8')
wLogPath = ("テストデータ/result/log").encode('utf-8')

#	XMLファイル設定
SCOEngineController.set_env_XML(wXMLPath)
#	入出力ディレクトリ設定
SCOEngineController.set_env_InputDir(wInputPath)
SCOEngineController.set_env_OutputDir(wOutputPath)
SCOEngineController.set_env_LogDir(wLogPath)
#	入力ファイル設定(読込)
SCOEngineController.set_input()
#	実行
wRtn = SCOEngineController.step()
print("step() result:",wRtn)

#	制約値設定(オプションなし)
wConstraintID = ("ProdPlanFixPeriod").encode('utf-8')
wCorpISID = ("FAC_02").encode('utf-8')
wDate = datetime.date(2018, 2, 12)
wValue = 12.0

wRtn = SCOEngineController.set_input_constraint_value(wConstraintID, wCorpISID, wDate, wValue)
print(wRtn)

#	制約値設定(品目ID指定)
wConstraintID = ("ProdPlanFixPeriod").encode('utf-8')
wCorpISID = ("FAC_02").encode('utf-8')
wItemID = ("BWDV100EN").encode('utf-8')
wDate = datetime.date(2018, 2, 12)
wValue = 12.0

wRtn = SCOEngineController.set_input_constraint_value(wConstraintID, wCorpISID, wDate, wValue, wItemID)
print(wRtn)

wRtn = SCOEngineController.set_input_constraint_value(wConstraintID, wCorpISID, wDate, wValue, ItemID=wItemID)
print(wRtn)


#	制約値設定(輸送タイプ指定)
wConstraintID = ("TransportUpperLimit").encode('utf-8')
wCorpISID = ("L0001").encode('utf-8')
wTranTypeNum = 1
wDate = datetime.date(2018, 2, 12)
wValue = 9898.0

wRtn = SCOEngineController.set_input_constraint_value(wConstraintID, wCorpISID, wDate, wValue, TransportType=wTranTypeNum)
print(wRtn)

#	制約値設定(生産設備ID指定)
wConstraintID = ("ProdPlanFixPeriod").encode('utf-8')
wCorpISID = ("FAC_02").encode('utf-8')
wProdFacilityID = ("EN02").encode('utf-8')
wDate = datetime.date(2018, 2, 12)
wValue = 123.0

wRtn = SCOEngineController.set_input_constraint_value(wConstraintID, wCorpISID, wDate, wValue, ProdFacilityID=wProdFacilityID)
print(wRtn)

#	制約値設定(生産ラインID指定)
wConstraintID = ("ProductionCapacity").encode('utf-8')
wCorpISID = ("FAC_02").encode('utf-8')
wProdLineID = ("LINE01").encode('utf-8')
wDate = datetime.date(2018, 2, 12)
wValue = 123.0

wRtn = SCOEngineController.set_input_constraint_value(wConstraintID, wCorpISID, wDate, wValue, ProdLineID=wProdLineID)
print(wRtn)

#	制約値設定(品目カテゴリID指定)
wConstraintID = ("ProdPlanFixPeriod").encode('utf-8')
wCorpISID = ("FAC_02").encode('utf-8')
wItemCategoryID = ("ICategory01").encode('utf-8')
wDate = datetime.date(2018, 2, 12)
wValue = 123.0

wRtn = SCOEngineController.set_input_constraint_value(wConstraintID, wCorpISID, wDate, wValue, ItemCategoryID=wItemCategoryID)
print(wRtn)

#	制約値設定(生産ラインID指定)
wConstraintID = ("ProductionCapacity").encode('utf-8')
wCorpISID = ("FAC_02").encode('utf-8')
wProdLineID = ("LINE01").encode('utf-8')
wDate = datetime.date(2018, 2, 12)
wValue = 123.0

wRtn = SCOEngineController.set_input_constraint_value(wConstraintID, wCorpISID, wDate, wValue, ProdLineID=wProdLineID)
print(wRtn)

#	制約値設定(生産ラインID指定…リミット数値大指定)
wConstraintID = ("ProductionCapacity").encode('utf-8')
wCorpISID = ("FAC_02").encode('utf-8')
wProdLineID = ("LINE01").encode('utf-8')
wDate = datetime.date(2020, 2, 12)
wValue = 999999.0

wRtn = SCOEngineController.set_input_constraint_value(wConstraintID, wCorpISID, wDate, wValue, ProdLineID=wProdLineID)
print(wRtn)

#	---------------------------------------------------------------------------
#	カレンダID変更
wCorpISID = ("FAC_02").encode('utf-8')
wCalendarID = ("CALtest").encode('utf-8')
#wCalendarID = ("CAL111").encode('utf-8')

wRtn = SCOEngineController.set_input_cal_ID(wCorpISID, wCalendarID)
print(wRtn)
#	カレンダID未定義指定
wRtn = SCOEngineController.set_input_cal_ID(wCorpISID)
print(wRtn)


#	---------------------------------------------------------------------------
#	需要充足率計算(期間付き)

import pandas
import datetime
import SCOEngineController

wXMLPath = ("あああ/SCSimEngine.xml").encode('utf-8')
wInputPath = ("テストデータ/data_AI_CO2").encode('utf-8')
wOutputPath = ("テストデータ/result/out").encode('utf-8')
wLogPath = ("テストデータ/result/log").encode('utf-8')
#	XMLファイル設定
SCOEngineController.set_env_XML(wXMLPath)
#	入出力ディレクトリ設定
SCOEngineController.set_env_InputDir(wInputPath)
SCOEngineController.set_env_OutputDir(wOutputPath)
SCOEngineController.set_env_LogDir(wLogPath)
#	入力ファイル設定(読込)
SCOEngineController.set_input()

#	実行
wRtn = SCOEngineController.step()
print("step() result:",wRtn)

wCorpStr = ("CI001").encode('utf-8')
wItemStr = ("P0000000001").encode('utf-8')

wRtn = SCOEngineController.get_kpi_order_fill_rate(wCorpStr, wItemStr)
print(wRtn)


wCalcStartDate = datetime.date(2022, 2, 3)
wCalcEndDate = datetime.date(2022, 2, 10)

wRtn = SCOEngineController.get_kpi_order_fill_rate(wCorpStr, wItemStr, wCalcStartDate, wCalcEndDate)
print(wRtn)

wRtn = SCOEngineController.get_kpi_order_fill_rate(wCorpStr, wItemStr, wCalcStartDate)
print(wRtn)

wRtn = SCOEngineController.get_kpi_order_fill_rate(wCorpStr, CalcStartDate=wCalcStartDate)
print(wRtn)

wRtn = SCOEngineController.get_kpi_order_fill_rate(CalcEndDate=wCalcEndDate)
print(wRtn)

#	---------------------------------------------------------------------------
#	平均在庫計算(期間付き)

import pandas
import datetime
import SCOEngineController

wXMLPath = ("あああ/SCSimEngine.xml").encode('utf-8')
wInputPath = ("テストデータ/data_test230111").encode('utf-8')
wOutputPath = ("テストデータ/result/out").encode('utf-8')
wLogPath = ("テストデータ/result/log").encode('utf-8')
#	XMLファイル設定
SCOEngineController.set_env_XML(wXMLPath)
#	入出力ディレクトリ設定
SCOEngineController.set_env_InputDir(wInputPath)
SCOEngineController.set_env_OutputDir(wOutputPath)
SCOEngineController.set_env_LogDir(wLogPath)
#	入力ファイル設定(読込)
SCOEngineController.set_input()

#	実行
wRtn = SCOEngineController.step()
print("step() result:",wRtn)

wCorpStr = ("CI003").encode('utf-8')
wItemStr = ("P0000000004").encode('utf-8')

wRtn = SCOEngineController.get_kpi_average_inventoryQty(wCorpStr, wItemStr)
print(wRtn)

wCalcStartDate = datetime.date(2015, 10, 10)
wCalcEndDate = datetime.date(2015, 10, 20)

wRtn = SCOEngineController.get_kpi_average_inventoryQty(wCorpStr, wItemStr, wCalcStartDate, wCalcEndDate)
print(wRtn)

wRtn = SCOEngineController.get_kpi_average_inventoryQty(wCorpStr, wItemStr, wCalcStartDate)
print(wRtn)

wRtn = SCOEngineController.get_kpi_average_inventoryQty(wCorpStr, wItemStr, CalcEndDate=wCalcEndDate)
print(wRtn)




#エラーケース
wCalcStartDate = datetime.date(2015, 9, 30)
wCalcEndDate = datetime.date(2015, 11, 1)

wCalcStartDate = datetime.date(2015, 10, 30)
wCalcEndDate = datetime.date(2015, 10, 1)

#	---------------------------------------------------------------------------
#	平均在庫計算(期間付き)

wRtn = SCOEngineController.get_kpi_average_inventoryAmount(wCorpStr, wItemStr)
print(wRtn)

wCalcStartDate = datetime.date(2015, 10, 10)
wCalcEndDate = datetime.date(2015, 10, 20)

wRtn = SCOEngineController.get_kpi_average_inventoryAmount(wCorpStr, wItemStr, wCalcStartDate, wCalcEndDate)
print(wRtn)

wRtn = SCOEngineController.get_kpi_average_inventoryAmount(wCorpStr, wItemStr, wCalcStartDate)
print(wRtn)

wRtn = SCOEngineController.get_kpi_average_inventoryAmount(wCorpStr, wItemStr, CalcEndDate=wCalcEndDate)
print(wRtn)



