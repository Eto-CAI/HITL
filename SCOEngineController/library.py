##
#	@file: library.py
#	@brief: SCOエンジンコントローラ関数群
#
#	SCO Engine Controller Library Module
#	SCOエンジンコントローラのインタフェース関数群本体。
#
#	@version 1.0.0.0

import ctypes
import os

import pandas
import numpy

import datetime

mdll_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'SCOEngineController.dll')
libc = ctypes.cdll.LoadLibrary(mdll_file)

libc.setEnvXML.argtypes = [ctypes.c_char_p]
libc.setEnvInputDir.argtypes = [ctypes.c_char_p]
libc.setEnvOutputDir.argtypes = [ctypes.c_char_p]
libc.setEnvLogDir.argtypes = [ctypes.c_char_p]

libc.setEnvLogOutputControl.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int)
libc.setEnvLogSaveControl.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int)
libc.setEnvBoxOFR.argtypes = [ctypes.c_double]
libc.setEnvDefaultExchangeRate.argtypes = [ctypes.c_double]

#	sim_input
libc.getInputActualDemandCorpID.restype = ctypes.c_char_p
libc.getInputActualDemandItemID.restype = ctypes.c_char_p
libc.getInputActualDemandArrivalRequestDate.restype = ctypes.c_char_p

libc.setInputActualDemandQty.argtypes = (ctypes.c_long, ctypes.c_long)

libc.getInputDemandForecastCorpID.restype = ctypes.c_char_p
libc.getInputDemandForecastItemID.restype = ctypes.c_char_p
libc.getInputDemandForecastToCorpID.restype = ctypes.c_char_p
libc.getInputDemandForecastForecastPlannedTimePoint.restype = ctypes.c_char_p
libc.getInputDemandForecastArrivalRequestDate.restype = ctypes.c_char_p

libc.getInputSafetyStockCorpID.restype = ctypes.c_char_p
libc.getInputSafetyStockItemID.restype = ctypes.c_char_p
libc.getInputSafetyStockStartDate.restype = ctypes.c_char_p
libc.getInputSafetyStockSafetyStockCoef.restype = ctypes.c_double

libc.setInputSafetyStockSafetyStockQty.argtypes = (ctypes.c_long, ctypes.c_long)
libc.setInputSafetyStockPrecedingRetentionDays.argtypes = (ctypes.c_long, ctypes.c_long)
libc.setInputSafetyStockKanbanQty.argtypes = (ctypes.c_long, ctypes.c_long)
libc.setInputSafetyStockSafetyStockCoef.argtypes = (ctypes.c_long, ctypes.c_double)
libc.setInputSafetyStockPastDemandRefPeriod.argtypes = (ctypes.c_long, ctypes.c_long)

libc.getInputAgentISAgentISID.restype = ctypes.c_char_p
libc.getInputAgentISAgcmID.restype = ctypes.c_char_p
libc.getInputAgentISLogicID.restype = ctypes.c_char_p

libc.setInputAgentISLogicID.argtypes = (ctypes.c_long, ctypes.c_char_p)

#	20221021	RM#1766_SCOエンジンコントローラのパラメータおよびKPI種別追加 Add start
libc.checkTargetTranMasterElement.restype = ctypes.c_bool
libc.checkTargetCorpTranMasterElement.argtypes = (ctypes.c_long, ctypes.c_char_p)
libc.checkTargetCorpTranMasterElement.restype = ctypes.c_bool
libc.checkTargetItemTranMasterElement.argtypes = (ctypes.c_long, ctypes.c_char_p)
libc.checkTargetItemTranMasterElement.restype = ctypes.c_bool
libc.checkTargetCitmTranMasterElement.argtypes = (ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p)
libc.checkTargetCitmTranMasterElement.restype = ctypes.c_bool
libc.checkTargetCitmTypeTranMasterElement.argtypes = (ctypes.c_long, ctypes.c_char_p, ctypes.c_char_p,ctypes.c_long)
libc.checkTargetCitmTypeTranMasterElement.restype = ctypes.c_bool

libc.getInputTranMasterCorpID.restype = ctypes.c_char_p
libc.getInputTranMasterItemID.restype = ctypes.c_char_p
libc.getInputTranMasterTranType.restype = ctypes.c_int
libc.getInputTranMasterTranLT.restype = ctypes.c_int
libc.getInputTranMasterAllocRate.restype = ctypes.c_double
libc.getInputTranMasterTranUnitCost.restype = ctypes.c_double
libc.getInputTranMasterTranLotSize.restype = ctypes.c_int
libc.getInputTranMasterOrderFixedPeriod.restype = ctypes.c_int
libc.getInputTranMasterTranMeanID.restype = ctypes.c_char_p
libc.getInputTranMasterResourceAccomAgentISID.restype = ctypes.c_char_p

libc.setInputTranMasterAllocRate.argtypes = (ctypes.c_long, ctypes.c_double)
libc.setInputTranMasterAllocRate.restype = ctypes.c_int
libc.setInputTranMasterTranType.argtypes = (ctypes.c_long, ctypes.c_long)
libc.setInputTranMasterTranType.restype = ctypes.c_int
libc.setInputTranMasterTranLT.argtypes = (ctypes.c_long, ctypes.c_long, ctypes.c_long)
libc.setInputTranMasterTranLT.restype = ctypes.c_int
libc.updateTransportMasterAllocRate.restype = ctypes.c_int
#	20221021	RM#1766_SCOエンジンコントローラのパラメータおよびKPI種別追加 Add end

#	20230104	RM#1784_SCOエンジンコントローラの制約値およびカレンダID変更 Add start
libc.setInputConstraintValue.restype = ctypes.c_long
libc.setInputConstraintValue.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double)
libc.setInputConstraintValueWithItemID.restype = ctypes.c_long
libc.setInputConstraintValueWithItemID.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double)
libc.setInputConstraintValueWithTranType.restype = ctypes.c_long
libc.setInputConstraintValueWithTranType.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_long, ctypes.c_char_p, ctypes.c_double)
libc.setInputConstraintValueWithProdFacilityID.restype = ctypes.c_long
libc.setInputConstraintValueWithProdFacilityID.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double)
libc.setInputConstraintValueWithProdLineID.restype = ctypes.c_long
libc.setInputConstraintValueWithProdLineID.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double)
libc.setInputConstraintValueWithItemCategoryID.restype = ctypes.c_long
libc.setInputConstraintValueWithItemCategoryID.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double)

libc.setInputCalendarID.restype = ctypes.c_long
libc.setInputCalendarID.argtypes = (ctypes.c_char_p, ctypes.c_char_p)
#	20230104	RM#1784_SCOエンジンコントローラの制約値およびカレンダID変更 Add end

#	sim_result
libc.getResultDailyInventoryActualDateTime.restype = ctypes.c_char_p
libc.getResultDailyInventoryActualCorpID.restype = ctypes.c_char_p
libc.getResultDailyInventoryActualItemID.restype = ctypes.c_char_p
libc.getResultDailyInventoryActualCCType.restype = ctypes.c_char_p
libc.getResultDailyInventoryActualDblQty.restype = ctypes.c_double
libc.getResultDailyInventoryActualAmount.restype = ctypes.c_double

libc.getResultDailyShipActualDateTime.restype = ctypes.c_char_p
libc.getResultDailyShipActualCorpID.restype = ctypes.c_char_p
libc.getResultDailyShipActualItemID.restype = ctypes.c_char_p
libc.getResultDailyShipActualToCorpID.restype = ctypes.c_char_p
libc.getResultDailyShipActualTranMeanID.restype = ctypes.c_char_p
libc.getResultDailyShipActualTranMeanName.restype = ctypes.c_char_p
libc.getResultDailyShipActualShipReqAmount.restype = ctypes.c_double
libc.getResultDailyShipActualShipAmount.restype = ctypes.c_double

libc.getResultEventShipActualDateTime.restype = ctypes.c_char_p
libc.getResultEventShipActualCorpID.restype = ctypes.c_char_p
libc.getResultEventShipActualItemID.restype = ctypes.c_char_p
libc.getResultEventShipActualToCorpID.restype = ctypes.c_char_p
libc.getResultEventShipActualTranMeanID.restype = ctypes.c_char_p
libc.getResultEventShipActualTranMeanName.restype = ctypes.c_char_p
libc.getResultEventShipActualShipReqAmount.restype = ctypes.c_double
libc.getResultEventShipActualShipAmount.restype = ctypes.c_double
libc.getResultEventShipActualDemandPriorityID.restype = ctypes.c_char_p

libc.getResultLogPurchaseOrderDateTime.restype = ctypes.c_char_p
libc.getResultLogPurchaseOrderToCorpID.restype = ctypes.c_char_p
libc.getResultLogPurchaseOrderItemID.restype = ctypes.c_char_p
libc.getResultLogPurchaseOrderFromCorpID.restype = ctypes.c_char_p
libc.getResultLogPurchaseOrderDateOfIssue.restype = ctypes.c_char_p
libc.getResultLogPurchaseOrderArrivalRequestDate.restype = ctypes.c_char_p
libc.getResultLogPurchaseOrderShipReqDate.restype = ctypes.c_char_p
libc.getResultLogPurchaseOrderTranMeanID.restype = ctypes.c_char_p
libc.getResultLogPurchaseOrderTranMeanName.restype = ctypes.c_char_p
libc.getResultLogPurchaseOrderDemandPriorityID.restype = ctypes.c_char_p

#	KPI
#	20221021	RM#1766_SCOエンジンコントローラのパラメータおよびKPI種別追加 DA start
#	libc.getKPIAverageInventory.argtypes = (ctypes.c_char_p, ctypes.c_char_p)
#	libc.getKPIAverageInventory.restype = ctypes.c_double
#	20230123	RM#1788_SCOエンジンコントローラのKPI計算期間の指定 DA start
#	libc.getKPIAverageInventoryQty.argtypes = (ctypes.c_char_p, ctypes.c_char_p)
#	libc.getKPIAverageInventoryQty.restype = ctypes.c_double
#	libc.getKPIAverageInventoryAmount.argtypes = (ctypes.c_char_p, ctypes.c_char_p)
#	libc.getKPIAverageInventoryAmount.restype = ctypes.c_double
libc.getKPIAverageInventoryQty.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p)
libc.getKPIAverageInventoryQty.restype = ctypes.c_double
libc.getKPIAverageInventoryAmount.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p)
libc.getKPIAverageInventoryAmount.restype = ctypes.c_double
#	20230123	RM#1788_SCOエンジンコントローラのKPI計算期間の指定 DA end
#	20221021	RM#1766_SCOエンジンコントローラのパラメータおよびKPI種別追加 DA end
libc.getKPICO2.argtypes = (ctypes.c_char_p, ctypes.c_char_p)
libc.getKPICO2.restype = ctypes.c_double
#	20230123	RM#1788_SCOエンジンコントローラのKPI計算期間の指定 DA start
#libc.getKPIOrderFillRate.argtypes = (ctypes.c_char_p, ctypes.c_char_p)
libc.getKPIOrderFillRate.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p)
#	20230123	RM#1788_SCOエンジンコントローラのKPI計算期間の指定 DA end
libc.getKPIOrderFillRate.restype = ctypes.c_double
libc.getKPIOrderFillRateAverage.argtypes = (ctypes.c_char_p, ctypes.c_char_p)
libc.getKPIOrderFillRateAverage.restype = ctypes.c_double

#	20230605	RM#1825_リスク評価対応型エンジンコントローラ Add start
libc.checktKPIInventoryQtyInt.argtypes = (ctypes.c_char_p, ctypes.c_char_p)
libc.checktKPIInventoryQtyInt.restype = ctypes.c_int
libc.getKPIInventoryQtyInt.argtypes = (ctypes.c_char_p, ctypes.c_char_p)
libc.getKPIInventoryQtyInt.restype = ctypes.c_int
libc.getKPIInventoryQtyDouble.argtypes = (ctypes.c_char_p, ctypes.c_char_p)
libc.getKPIInventoryQtyDouble.restype = ctypes.c_double
libc.getKPIInventoryAmount.argtypes = (ctypes.c_char_p, ctypes.c_char_p)
libc.getKPIInventoryAmount.restype = ctypes.c_double

libc.setIncidentInventoryQtyInt.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int)
libc.setIncidentInventoryQtyInt.restype = ctypes.c_int
libc.setIncidentInventoryQtyDouble.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_double)
libc.setIncidentInventoryQtyDouble.restype = ctypes.c_int

libc.getSCTncidentTranWIPElementNum.restype = ctypes.c_int
libc.getSCTncidentTranWIPActive.restype = ctypes.c_int
libc.getSCTncidentTranWIPCorpID.argtypes = [ctypes.c_int]
libc.getSCTncidentTranWIPCorpID.restype = ctypes.c_char_p
libc.getSCTncidentTranWIPItemID.argtypes = [ctypes.c_int]
libc.getSCTncidentTranWIPItemID.restype = ctypes.c_char_p
libc.getSCTncidentTranWIPTranType.argtypes = [ctypes.c_int]
libc.getSCTncidentTranWIPTranType.restype = ctypes.c_int
libc.getSCTncidentTranWIPArrivalDate.argtypes = [ctypes.c_int]
libc.getSCTncidentTranWIPArrivalDate.restype = ctypes.c_char_p
libc.getSCTncidentTranWIPQty.argtypes = [ctypes.c_int]
libc.getSCTncidentTranWIPQty.restype = ctypes.c_int

libc.getSCTncidentProdWIPElementNum.restype = ctypes.c_int
libc.getSCTncidentProdWIPActive.restype = ctypes.c_int
libc.getSCTncidentProdWIPCorpID.argtypes = [ctypes.c_int]
libc.getSCTncidentProdWIPCorpID.restype = ctypes.c_char_p
libc.getSCTncidentProdWIPItemID.argtypes = [ctypes.c_int]
libc.getSCTncidentProdWIPItemID.restype = ctypes.c_char_p
libc.getSCTncidentProdWIPProdType.argtypes = [ctypes.c_int]
libc.getSCTncidentProdWIPProdType.restype = ctypes.c_int
libc.getSCTncidentProdWIPCompletionDate.argtypes = [ctypes.c_int]
libc.getSCTncidentProdWIPCompletionDate.restype = ctypes.c_char_p
libc.getSCTncidentProdWIPQty.argtypes = [ctypes.c_int]
libc.getSCTncidentProdWIPQty.restype = ctypes.c_int
libc.setSCTncidentProdWIPQty.argtypes = (ctypes.c_int, ctypes.c_int)
libc.setSCTncidentProdWIPQty.restype = ctypes.c_int

#	20230605	RM#1825_リスク評価対応型エンジンコントローラ Add end

wRtn = libc.initialize()

##	----------------------------------------------------------------------------
#	@brief SCOエンジンコントローラの初期化
#
#	SCOエンジンコントローラのインスタンスおよびSCOデータを初期化する。
#
#	@param なし
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval =0 成功
#	@retval <0 失敗
#
def initialize():
	#	データマネージャ/シミュレーションマネージャを初期化
	wRtn = libc.initialize()
	return wRtn

##	----------------------------------------------------------------------------
#	@brief SCOエンジンコントローラの破棄
#
#	SCOエンジンコントローラのインスタンスを破棄し、SCOデータを破棄する。
#
#	@param なし
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval =0 成功
#	@retval <0 失敗
#
def dispose():
	#	データマネージャ/シミュレーションマネージャを再初期化
	wRtn = libc.initialize()
	return wRtn

##	----------------------------------------------------------------------------
#	@brief シミュレーション開始時点までの巻き戻し
#
#	シミュレーション開始時点(set_input()が呼び出された直後)までシミュレーション状態を戻す。
#
#	@param なし
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def reset():
	#	実行状態リセットを実行し、初期状態に巻き戻す
	wRtn = libc.execReset()
	return wRtn

#	----------------------------------------------------------------------------
#	設定関連

##	----------------------------------------------------------------------------
#	@brief 定義ファイル読み込み
#
#	指定された設定ファイルの読み込みを行なう。
#	設定ファイルパス省略時は、実行フォルダ位置の定義ファイルを読み込む。
#
#	@param[in] pXMLPath 設定ファイルパス
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#	@retval eERR_ERR_MANAGE_FILEOPEN_FAIL(>0) XMLファイルオープン失敗
#
def set_env_XML(pXMLPath=''):
	if (len(pXMLPath) == 0):
		#	設定ファイルパス省略時、実行ディレクトリを設定
		pXMLPath = os.path.join(os.getcwd(), 'SCSimEngine.xml')
	#	指定された設定ファイルの読み込み
	wRtn = libc.setEnvXML(pXMLPath)
	return wRtn

##	----------------------------------------------------------------------------
#	@brief 入力ファイル位置指定
#
#	入力ディレクトリの設定を行なう。
#
#	@param[in] pInputPath 入力ディレクトリ
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def set_env_InputDir(pInputPath):
	#	入力ディレクトリ位置を設定
	wRtn = libc.setEnvInputDir(pInputPath)
	return wRtn

##	----------------------------------------------------------------------------
#	@brief 結果ファイル出力位置指定
#
#	結果ファイルの出力ディレクトリ設定を行なう。
#
#	@param[in] pOutputPath 出力ディレクトリ
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def set_env_OutputDir(pOutputPath):
	#	出力ディレクトリ位置を設定
	wRtn = libc.setEnvOutputDir(pOutputPath)
	return wRtn

##	----------------------------------------------------------------------------
#	@brief ログファイル出力位置指定
#
#	ログファイル出力位置の設定を行なう。
#
#	@param[in] pLogPath ログディレクトリ
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def set_env_LogDir(pLogPath):
	#	ログディレクトリ位置を設定
	wRtn = libc.setEnvLogDir(pLogPath)
	return wRtn

##	----------------------------------------------------------------------------
#	@brief ファイル出力可否指定
#
#	指定結果ファイル出力を設定する。
#	指定セクションラベルには、結果(イベント("event")/日々("daily"))、ログ("log")の何れかを指定する。
#
#	@param[in] pSecStr 指定セクションラベル
#	@param[in] pFileStr 指定ファイルラベル
#	@param[in] pNum 出力指定(出力しない:0、出力：0以外)省略時：1
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def set_env_LogOutputControl(pSecStr, pFileStr, pNum=1):
	#	結果ファイル出力の可否を設定
	wRtn = libc.setEnvLogOutputControl(pSecStr, pFileStr, pNum)
	return wRtn

##	----------------------------------------------------------------------------
#	@brief 結果保存可否指定
#
#	指定結果保存を設定する。
#	指定セクションラベルには、結果(イベント("event")/日々("daily"))、ログ("log")の何れかを指定する。
#
#	@param[in] pSecStr 指定セクションラベル
#	@param[in] pFileStr 指定ファイルラベル
#	@param[in] pNum 保存指定(保存しない:0、保存：0以外)省略時：0
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def set_env_LogSaveControl(pSecStr, pFileStr, pNum=0):
	#	結果保存設定の可否を設定
	wRtn = libc.setEnvLogSaveControl(pSecStr, pFileStr, pNum)
	return wRtn

##	----------------------------------------------------------------------------
#	@brief 最小有効量の算出用除数桁数設定
#
#	最小有効量の算出用除数桁数を設定する。
#
#	@param[in] pNum 算出用除数桁数 省略時：-1
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def set_env_MinEffectNumDigit(pNum=-1):
	#	 最小有効量の算出用除数桁数を設定
	wRtn = libc.setEnvMinEffectNumDigit(pNum)
	return wRtn

##	----------------------------------------------------------------------------
#	@brief BoxOFR下限省略時値設定
#
#	BoxOFRデフォルト値を設定する。
#
#	@param[in] pRate BoxOFRデフォルト値 省略時：0.0
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def set_env_BoxOFR(pRate=0.0):
	#	BoxOFRデフォルト値を設定
	wRtn = libc.setEnvBoxOFR(pRate)
	return wRtn

##	----------------------------------------------------------------------------
#	@brief 省略時為替レート指定値設定
#
#	省略時通貨為替レート値を設定する。
#
#	@param pRate 省略時通貨為替レート値 省略時：-1.0
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def set_env_DefaultExchangeRate(pRate= -1.0):
	#	省略時通貨為替レート値を設定
	wRtn = libc.setEnvDefaultExchangeRate(pRate)
	return wRtn

##	----------------------------------------------------------------------------
#	@brief 指定入力パスから入力ファイル読み込み
#
#	環境設定されたファイルパスから入力ファイルを読み込む動作を行う。
#	この際に、シミュレーション実行に必要な各種設定も行う。
#	DLLが以前使用していたデータセットが存在する場合の削除(リフレッシュ)、
#	準備完了段階のデータセットのバックアップ(スナップショット作成)もここで行なう。
#
#	@param なし
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def set_input():
	#	エンジン実行用ファイル関係設定を行う
	wRtn = libc.setInput()
	return wRtn

##	----------------------------------------------------------------------------
#	@brief シミュレーション実行
#
#	設定された入力データによりシミュレーションを実行する。
#	引数で指定された日数分のシミュレーションを実行する。これは一日の終了イベントにて実行を停止する。
#
#	@param[in] pNumOfDate 動作日数 省略時：0(全期間実行)
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eEXIT_CODE_RUNTIME_DATA_FAILURE(3) 実行時データエラー
#	@retval eEXIT_CODE_RUNTIME_SYSTEM_FAILURE(4) 実行時システムエラー
#
def step(pNumOfDate = 0):
	if pNumOfDate <= 0:
		#	シミュレーション実行(全期間)
		wRtn = libc.simExecUntilEnd()
	else:
		#	シミュレーション実行(動作日数指定)
		wRtn = libc.simExecStep(pNumOfDate)
	return wRtn

#	----------------------------------------------------------------------------
#	入力関連

##	----------------------------------------------------------------------------
#	@brief 入力値入手
#
#	指定エンジンインプットデータを取得する。
#	(現状、「ActualDemand」のみ対応。)
#	(ただし、本関数については、未使用。)
#
#	@param[in] pDataKind 入力データ取得対象
#	@return Dataframe 指定エンジンインプットデータリスト(データ無し時：空リスト)
#
def get_input(pDataKind):
	wRtnList = pandas.DataFrame()

	if (pDataKind == 'ActualDemand.csv'):
		#	入力データ数として、実需エレメント個数を取得
		wSize = libc.getInputActualDemandElementNum()
		print(wSize)
		if (wSize <= 0):
			print('ERROR!')
			return wRtnList
		#ID,CompanyISID,ItemID,ArrivalRequestDate,DemandQty
		wColumns = ['ID', 'CompanyISID', 'ItemID', 'ArrivalRequestDate', 'DemandQty']
		#for i in range(0,wSize - 1):
		for i in range(0,wSize):
			#	企業ISIDを取得
			wCorpID = (libc.getInputActualDemandCorpID(i)).decode(encoding='utf-8')
			#	品目IDを取得
			wItemID = (libc.getInputActualDemandItemID(i)).decode(encoding='utf-8')
			#	実需対象要求日時を取得
			wDateStr = (libc.getInputActualDemandArrivalRequestDate(i)).decode(encoding='utf-8')
			wDatetime = datetime.datetime.strptime(wDateStr, '%Y/%m/%d')
			wDate = datetime.date(wDatetime.year, wDatetime.month, wDatetime.day)
			#	実需値を取得
			wQty = libc.getInputActualDemandQty(i)
			#print(wCorpID)
			#print(wItemID)
			#print(wDate)
			#print(wQty)
			wAppend = pandas.DataFrame(data =[[i, wCorpID, wItemID, wDate, wQty]], 
				columns = wColumns)
			#	取得した入力データをデータリストに追加
			wRtnList = pandas.concat([wRtnList, wAppend], ignore_index=True, axis=0)

	return wRtnList

##	----------------------------------------------------------------------------
#	@brief 実需入力値入手
#
#	指定エンジンインプットデータ(実需値)を取得する。
#
#	@param なし
#	@return Dataframe 指定エンジンインプットデータ(実需)リスト(データ無し時：空リスト)
#
def get_input_ActualDemand():
	wRtnList = pandas.DataFrame()

	#ID,CompanyISID,ItemID,ArrivalRequestDate,DemandQty
	wColumns = ['ID', 'CompanyISID', 'ItemID', 'ArrivalRequestDate', 'DemandQty']	
	#	入力データ数として、実需エレメント個数を取得
	wSize = libc.getInputActualDemandElementNum()
	#print(wSize)
	if (wSize <= 0):
		#	空データ作成
		wRtnList = pandas.DataFrame(index=[], columns=wColumns)
		return wRtnList

	for i in range(0,wSize):
		#	企業IDの取得
		wCorpID = (libc.getInputActualDemandCorpID(i)).decode(encoding='utf-8')
		#	品目IDの取得
		wItemID = (libc.getInputActualDemandItemID(i)).decode(encoding='utf-8')
		#	実需対象要求日時の取得
		wDateStr = (libc.getInputActualDemandArrivalRequestDate(i)).decode(encoding='utf-8')
		wDatetime = datetime.datetime.strptime(wDateStr, '%Y/%m/%d')
		wDate = datetime.date(wDatetime.year, wDatetime.month, wDatetime.day)
		#	実需値の取得
		wQty = libc.getInputActualDemandQty(i)
		#print(wCorpID)
		#print(wItemID)
		#print(wDate)
		#print(wQty)
		wAppend = pandas.DataFrame(data =[[i, wCorpID, wItemID, wDate, wQty]], 
			columns = wColumns)
		#	取得したデータをDataframeリストに追加
		wRtnList = pandas.concat([wRtnList, wAppend], ignore_index=True, axis=0)

	return wRtnList

##	----------------------------------------------------------------------------
#	@brief 実需値設定
#
#	指定エンジンインプットデータ(実需値)を設定する。
#
#	@param[in] pDataList 指定エンジンインプットデータ
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def set_input_ActualDemand(pDataList):
	wRtn = 0
	#	設定する入力データ数としてデータリストのサイズを取得
	wSize = len(pDataList)
	if (wSize <= 0):
		print('ERROR!')
		return -2
	for wID, wQty in zip(pDataList['ID'], pDataList['DemandQty']):
		#print(wID, wQty)
		#	指定されたIDの実需値を変更
		wRtn = libc.setInputActualDemandQty(wID, wQty)
		if (wRtn < 0):
			return wRtn
	return wRtn

##	----------------------------------------------------------------------------
#	@brief 需要予測入力値入手
#
#	指定エンジンインプットデータ(需要予測値)を取得する。
#
#	@param なし
#	@return Dataframe 指定エンジンインプットデータ(需要予測値)リスト(データ無し時：空リスト)
#
def get_input_DemandForecast():
	wRtnList = pandas.DataFrame()

	#ID,CompanyISID,ItemID,ToCompanyISID,ForecastPlannedTimePoint,ArrivalRequestDate,Quantity
	wColumns = ['ID', 'CompanyISID', 'ItemID', 'ToCompanyISID', 'ForecastPlannedTimePoint', 'ArrivalRequestDate', 'Quantity']

	#	入力データ数として、需要予測エレメント個数を取得
	wSize = libc.getInputDemandForecastElementNum()
	#print(wSize)
	if (wSize <= 0):
		#	空データ作成
		wRtnList = pandas.DataFrame(index=[], columns=wColumns)
		return wRtnList

	for i in range(0,wSize):
		#	企業IDを取得
		wCorpID = (libc.getInputDemandForecastCorpID(i)).decode(encoding='utf-8')
		#	品目IDを取得
		wItemID = (libc.getInputDemandForecastItemID(i)).decode(encoding='utf-8')
		#	入庫側企業ISIDを取得
		wToCorpID = (libc.getInputDemandForecastToCorpID(i)).decode(encoding='utf-8')

		#	予測立案時点を取得
		wDateStr = (libc.getInputDemandForecastForecastPlannedTimePoint(i)).decode(encoding='utf-8')
		wDatetime = datetime.datetime.strptime(wDateStr, '%Y/%m/%d')
		wFPDate = datetime.date(wDatetime.year, wDatetime.month, wDatetime.day)

		#	到着リクエスト日時を取得
		wDateStr = (libc.getInputDemandForecastArrivalRequestDate(i)).decode(encoding='utf-8')
		wDatetime = datetime.datetime.strptime(wDateStr, '%Y/%m/%d')
		wARDate = datetime.date(wDatetime.year, wDatetime.month, wDatetime.day)

		#	予想値を取得
		wQty = libc.getInputDemandForecastQty(i)
#		print(wCorpID)
#		print(wItemID)
#		print(wToCorpID)
#		print(wFPDate)
#		print(wARDate)
#		print(wQty)
		wAppend = pandas.DataFrame(data =[[i, wCorpID, wItemID, wToCorpID, wFPDate, wARDate, wQty]], 
			columns = wColumns)
		#	取得したデータをDataframeリストに追加
		wRtnList = pandas.concat([wRtnList, wAppend], ignore_index=True, axis=0)

	return wRtnList

##	----------------------------------------------------------------------------
#	@brief 需要予測値設定
#
#	指定エンジンインプットデータ(需要予測値)を設定する。
#
#	@param[in] pDataList 指定エンジンインプットデータ
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def set_input_DemandForecast(pDataList):
	wRtn = 0
	#	入力データ数としてデータリストのサイズを取得
	wSize = len(pDataList)
	if (wSize <= 0):
		print('ERROR!')
		return -2
	for wID, wQty in zip(pDataList['ID'], pDataList['Quantity']):
		#print(wID, wQty)
		#	指定されたIDの需要予測値を変更
		wRtn = libc.setInputDemandForecastQty(wID, wQty)
		if (wRtn < 0):
			return wRtn
	return wRtn

##	----------------------------------------------------------------------------
#	@brief 安全在庫入力値入手
#
#	指定エンジンインプットデータ(安全在庫)を取得する。
#
#	@param なし
#	@return Dataframe 指定エンジンインプットデータ(安全在庫)リスト(データ無し時：空リスト)
#
def get_input_SafetyStock():
	wRtnList = pandas.DataFrame()

	#ID,CompanyISID,ItemID,StartDate,SafetyStockQuantity,PrecedingRetentionDays,
	#KanbanQuantity,SafetyStockCoefficient,PastActualDemandReferencePeriod
	wColumns = ['ID', 'CompanyISID', 'ItemID', 'StartDate', 'SafetyStockQuantity'
		, 'PrecedingRetentionDays', 'KanbanQuantity', 'SafetyStockCoefficient', 'PastActualDemandReferencePeriod']

	#	入力データ数として、安全在庫エレメント個数を取得
	wSize = libc.getInputSafetyStockElementNum()
	#print(wSize)
	if (wSize <= 0):
		#	空データ作成
		wRtnList = pandas.DataFrame(index=[], columns=wColumns)
		return wRtnList

	for i in range(0,wSize):
		#	企業IDを取得
		wCorpID = (libc.getInputSafetyStockCorpID(i)).decode(encoding='utf-8')
		#	品目IDを取得
		wItemID = (libc.getInputSafetyStockItemID(i)).decode(encoding='utf-8')
		#	開始日時を取得
		wDateStr = (libc.getInputSafetyStockStartDate(i)).decode(encoding='utf-8')
		wDatetime = datetime.datetime.strptime(wDateStr, '%Y/%m/%d')
		wDate = datetime.date(wDatetime.year, wDatetime.month, wDatetime.day)

		#	安全在庫量を取得
		wQty = libc.getInputSafetyStockSafetyStockQty(i)
		#	先行保持日数を取得
		wDays = libc.getInputSafetyStockPrecedingRetentionDays(i)
		#	かんばん枚数を取得
		wKanbanQty = libc.getInputSafetyStockKanbanQty(i)
		#	安全在庫係数を取得
		wCoefDbl = libc.getInputSafetyStockSafetyStockCoef(i)
		#	過去実需参照期間を取得
		wPeriod = libc.getInputSafetyStockPastDemandRefPeriod(i)
		#print(wCorpID)
		#print(wItemID)
		#print(wDate)
		#print(wQty)
		#print(wDays)
		#print(wKanbanQty)
		#print(wCoefDbl)
		#print(wPeriod)
		wAppend = pandas.DataFrame(data =[[i, wCorpID, wItemID, wDate, wQty, wDays, wKanbanQty, wCoefDbl, wPeriod]], 
			columns = wColumns)
		#	取得したデータをDataframeリストに追加
		wRtnList = pandas.concat([wRtnList, wAppend], ignore_index=True, axis=0)

	return wRtnList

##	----------------------------------------------------------------------------
#	@brief 安全在庫値設定
#
#	指定エンジンインプットデータ(安全在庫)を設定する。
#
#	@param[in] pDataList 指定エンジンインプットデータ(安全在庫)リスト
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def set_input_SafetyStock(pDataList):
	wRtn = 0
	#	入力データ数としてデータリストのサイズを取得
	wSize = len(pDataList)
	if (wSize <= 0):
		print('ERROR!')
		return -2
	for wID, wSSQty, wDays, wKanbanQty, wCoefDbl, wPeriod in zip(pDataList['ID'], pDataList['SafetyStockQuantity'], pDataList['PrecedingRetentionDays'], pDataList['KanbanQuantity'], pDataList['SafetyStockCoefficient'], pDataList['PastActualDemandReferencePeriod']):
		#print(wID, wSSQty, wDays, wKanbanQty, wCoefDbl, wPeriod)
		#	指定されたIDの安全在庫量を変更
		wRtn = libc.setInputSafetyStockSafetyStockQty(wID, wSSQty)
		if (wRtn < 0):
			return wRtn
		#	指定されたIDの先行保持日数を変更
		wRtn = libc.setInputSafetyStockPrecedingRetentionDays(wID, wDays)
		if (wRtn < 0):
			return wRtn
		#	指定されたIDのかんばん枚数を変更
		wRtn = libc.setInputSafetyStockKanbanQty(wID, wKanbanQty)
		if (wRtn < 0):
			return wRtn
		#	指定されたIDの安全在庫係数を変更
		wRtn = libc.setInputSafetyStockSafetyStockCoef(wID, wCoefDbl)
		if (wRtn < 0):
			return wRtn
		#	指定されたIDの過去実需参照期間を変更
		wRtn = libc.setInputSafetyStockPastDemandRefPeriod(wID, wPeriod)
		if (wRtn < 0):
			return wRtn
	return wRtn

##	----------------------------------------------------------------------------
#	@brief AgentIS入力値入手
#
#	指定エンジンインプットデータ(AgentIS)を取得する。
#
#	@param なし
#	@return Dataframe 指定エンジンインプットデータ(AgentIS)リスト(データ無し時：空リスト)
#
def get_input_AgentIS():
	wRtnList = pandas.DataFrame()
	#ID,AgentISID,AgentClassID,Behavior
	wColumns = ['ID', 'AgentISID', 'AgentClassID', 'Behavior']

	#	入力データ数として、AgentISエレメント個数を取得
	wSize = libc.getInputAgentISElementNum()
	#print(wSize)
	if (wSize <= 0):
		#	空データ作成
		wRtnList = pandas.DataFrame(index=[], columns=wColumns)
		return wRtnList

	for i in range(0,wSize):
		#	エージェントISIDを取得
		wAISID = (libc.getInputAgentISAgentISID(i)).decode(encoding='utf-8')
		#	エージェントクラスIDを取得
		wACID = (libc.getInputAgentISAgcmID(i)).decode(encoding='utf-8')
		#	振る舞いを取得
		wLogicID = (libc.getInputAgentISLogicID(i)).decode(encoding='utf-8')
		#print(wAISID)
		#print(wACID)
		#print(wLogicID)
		wAppend = pandas.DataFrame(data =[[i, wAISID, wACID, wLogicID]], 
			columns = wColumns)
		#	取得したデータをDataframeリストに追加
		wRtnList = pandas.concat([wRtnList, wAppend], ignore_index=True, axis=0)
	return wRtnList

##	----------------------------------------------------------------------------
#	@brief AgentIS値設定
#
#	指定エンジンインプットデータ(AgentIS値)を設定する。
#
#	@param[in] pDataList 指定エンジンインプットデータ(AgentIS値)リスト
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def set_input_AgentIS(pDataList):
	wRtn = 0
	#	入力データ数としてデータリストのサイズを取得
	wSize = len(pDataList)
	if (wSize <= 0):
		print('ERROR!')
		return -2
	for wID, wQty in zip(pDataList['ID'], pDataList['Behavior']):
		wLogicID = wQty.encode('utf-8')
		#print(wID, wLogicID)
		#	指定されたIDの振る舞いを変更する
		wRtn = libc.setInputAgentISLogicID(wID, wLogicID)
		if (wRtn < 0):
			return wRtn
	return wRtn

#	20221021	RM#1766_SCOエンジンコントローラのパラメータおよびKPI種別追加 Add start
#	----------------------------------------------------------------------------
#	TransportMaster関連
##	----------------------------------------------------------------------------
#	@brief TransportMaster入力値入手
#
#	指定エンジンインプットデータ(TransportMaster)を取得する。
#
#	@param[in] CorpISID 		指定企業 省略時:(全企業)
#	@param[in] ItemID 			指定品目 省略時:(全品目)
#	@param[in] TransportType 	指定輸送タイプ 省略時:(全輸送タイプ)
#	@return Dataframe 指定エンジンインプットデータ(AgentIS)リスト(データ無し時：空リスト)
#
def get_input_TransportMaster(
		CorpISID=('').encode('utf-8'), 
		ItemID=('').encode('utf-8'), 
		TransportType=-1):
	
	wRtnList = pandas.DataFrame()
	#ID,CompanyISID,ItemID,TransportType,TransportLT,AllocationRate,
	#	TransportUnitCost,TransportLotSize,OrderFixedPeriod,
	#	TransportMeanID,ResourceAccomAgentISID
	wColumns = ['ID', 'CompanyISID','ItemID','TransportType','TransportLT',
		'AllocationRate','TransportUnitCost','TransportLotSize',
		'OrderFixedPeriod','TransportMeanID','ResourceAccomAgentISID']

	#	入力組み合わせ判定
	wCitmFl = False
	wCorpFl = False
	wItemFl = False
	wTranTypeFl = False
	if (len(CorpISID) > 0):
		wCorpFl = True
	if (len(ItemID) > 0):
		wItemFl = True
	if (wCorpFl and wItemFl):
		wCitmFl = True
	if (TransportType > 0):
		wTranTypeFl = True
	#	入力データ数として、TransportMasterエレメント個数を取得
	wSize = libc.getInputTranMasterElementNum()
	#print(wSize)
	if (wSize <= 0):
		#	空データ作成
		wRtnList = pandas.DataFrame(index=[], columns=wColumns)
		return wRtnList

	for i in range(0,wSize):
		#	取得対象判定
		wTargetFl = False
		if (wTranTypeFl):
			#	全条件使用
			wTargetFl = libc.checkTargetCitmTypeTranMasterElement(i, CorpISID, ItemID, TransportType)
		elif (wCitmFl):
			#	企業-品目指定
			wTargetFl = libc.checkTargetCitmTranMasterElement(i, CorpISID, ItemID)
		elif (wCorpFl):
			#	企業指定
			wTargetFl = libc.checkTargetCorpTranMasterElement(i, CorpISID)
		elif (wItemFl):
			#	品目指定
			wTargetFl = libc.checkTargetItemTranMasterElement(i, ItemID)
		else:
			#	指定なし
			wTargetFl = libc.checkTargetTranMasterElement(i)
		if (not wTargetFl):
			continue
		
		#	CompanyISID取得
		wCorpID = (libc.getInputTranMasterCorpID(i)).decode(encoding='utf-8')
		#	ItemID取得
		wItemID = (libc.getInputTranMasterItemID(i)).decode(encoding='utf-8')
		#	TransportType取得
		wTranType = libc.getInputTranMasterTranType(i)
		#	TransportLT取得
		wTranLT = libc.getInputTranMasterTranLT(i)
		#	AllocationRate取得
		wAllocRate = libc.getInputTranMasterAllocRate(i)
		#	TransportUnitCost取得
		wTranUnitCost = libc.getInputTranMasterTranUnitCost(i)
		#	TransportLotSize取得
		wTranLotSize = libc.getInputTranMasterTranLotSize(i)
		#	OrderFixedPeriod取得
		wOrderFixedPeriod = libc.getInputTranMasterOrderFixedPeriod(i)
		#	TransportMeanID取得
		wTranMeanID = (libc.getInputTranMasterTranMeanID(i)).decode(encoding='utf-8')
		#	ResourceAccomAgentISID取得
		weAccomAgentISID = (libc.getInputTranMasterResourceAccomAgentISID(i)).decode(encoding='utf-8')

		wAppend = pandas.DataFrame(data =[[i, wCorpID, wItemID, wTranType,wTranLT,wAllocRate,wTranUnitCost,wTranLotSize,wOrderFixedPeriod,wTranMeanID,weAccomAgentISID]], 
			columns = wColumns)
		#	取得したデータをDataframeリストに追加
		wRtnList = pandas.concat([wRtnList, wAppend], ignore_index=True, axis=0)
	if (len(wRtnList) == 0):
		wRtnList = pandas.DataFrame(index=[], columns=wColumns)
	return wRtnList



##	----------------------------------------------------------------------------
#	@brief 輸送マスタ配分率設定
#
#	指定エンジンインプットデータ(TransportMaster)の配分率を設定する。
#
#	@param[in] pID 			指定エンジンインプットデータ輸送マスタID
#	@param[in] pAlloc_Rate	設定入力配分率
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def set_input_TransportMaster_alloc_rate(pID, pAlloc_Rate):
	wRtn = 0
	wRtn = libc.setInputTranMasterAllocRate(pID, pAlloc_Rate)
	return wRtn

##	----------------------------------------------------------------------------
#	@brief 輸送マスタ標準輸送タイプ設定
#
#	指定エンジンインプットデータ(TransportMaster)を標準輸送タイプに設定する。
#	該当輸送企業-品目の標準輸送タイプに引数輸送タイプを指定します。
#	輸送マスタIDデータが標準輸送タイプの場合、エラーとなります。
#
#	@param[in] pID 					指定エンジンインプットデータ輸送マスタID
#	@param[in] pChange_Tran_Type	設定の標準輸送タイプ変更輸送タイプ値
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def set_input_TransportMaster_tran_type(pID, pChange_Tran_Type):
	wRtn = 0
	wRtn = libc.setInputTranMasterTranType(pID, pChange_Tran_Type)
	return wRtn

##	----------------------------------------------------------------------------
#	@brief 輸送マスタ輸送LT/注文発行期間設定
#
#	指定エンジンインプットデータ(TransportMaster)の輸送LT/注文発行期間を設定する。
#	引数『column』に『TranLT』『OrderFixedPeriod』を指定し、設定パラメータを選択します。
#	引数を
#
#	@param[in] pID 			指定エンジンインプットデータ輸送マスタID
#	@param[in] column 		指定カラム名称『TranLT』又は『OrderFixedPeriod』
#	@param[in] pTerm		設定輸送LT値
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def set_input_TransportMaster_LT(pID, column, pTerm = -1):
	wRtn = 0
	wTranLT = -1
	wOrderFixPeriod = -1
	wColumn = 'TranLT'
	if (pTerm < 0):
		pTerm = column
		wColumn = 'TranLT'
	else:
		wColumn = column

	if (wColumn == 'TranLT'):
		wTranLT = pTerm
	elif (wColumn == 'OrderFixedPeriod'):
		wOrderFixPeriod = pTerm
	else:
		print("Wrong column Index[", column, "]")
		wRtn = -1
		return wRtn

	wRtn = libc.setInputTranMasterTranLT(pID, wTranLT, wOrderFixPeriod)
	return wRtn

##	----------------------------------------------------------------------------
#	@brief 輸送マスタ配分率正規化更新
#
#	指定エンジンインプットデータ(TransportMaster)の配分率正規化更新を行う。
#
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def update_TransportMaster():
	wRtn = 0
	wRtn = libc.updateTransportMasterAllocRate()
	return wRtn

#	20221021	RM#1766_SCOエンジンコントローラのパラメータおよびKPI種別追加 Add end

#	20230104	RM#1784_SCOエンジンコントローラの制約値およびカレンダID変更 Add start

##	----------------------------------------------------------------------------
#	@brief 制約値設定
#
#	指定対象制約ID/企業ID/対象日の制約値設定を行う。
#	オプションで『品目』『輸送タイプ』『生産設備ID』『生産ラインID』『品目カテゴリID』を指定します。
#
#	@param[in] pConstraintID 	指定制約ID
#	@param[in] pCorpID			指定企業ISID
#	@param[in] pDate			参照指定日付
#	@param[in] pValue			設定制約値
#	@param[in] ItemID 			指定品目 (省略可)
#	@param[in] TransportType 	指定輸送タイプ (省略可)
#	@param[in] ProdFacilityID 	指定生産設備ID (省略可)
#	@param[in] ProdLineID 		指定生産ラインID (省略可)
#	@param[in] ItemCategoryID 	品目カテゴリID (省略可)

#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def set_input_constraint_value(
		pConstraintID, pCorpID, pDate, pValue, 
		ItemID=('').encode('utf-8'), 
		TransportType=-1,
		ProdFacilityID=('').encode('utf-8'),
		ProdLineID=('').encode('utf-8'),
		ItemCategoryID=('').encode('utf-8')):

	wRtn = 0

	#	入力組み合わせ判定
	wItemFl = False
	wTransportTypeFl = False
	wProdFacilityFl = False
	wProdLineFl = False
	wItemCategoryFl = False

	if (len(ItemID) > 0):
		wItemFl = True
	if (TransportType > 0):
		wTransportTypeFl = True
	if (len(ProdFacilityID) > 0):
		wProdFacilityFl = True
	if (len(ProdLineID) > 0):
		wProdLineFl = True
	if (len(ItemCategoryID) > 0):
		wItemCategoryFl = True

	#	日付文字列変換
	wDate = pDate.strftime('%Y/%m/%d').encode('utf-8')

	#	動作処理分岐
	#	現状省略対象パラメータ同時指定はない。
	if (wItemFl):
		#	制約値設定(品目ID指定)
		wRtn = libc.setInputConstraintValueWithItemID(pConstraintID, pCorpID, ItemID, wDate, pValue)
	elif (wTransportTypeFl):
		#	制約値設定(輸送タイプ指定)
		wRtn = libc.setInputConstraintValueWithTranType(pConstraintID, pCorpID, TransportType, wDate, pValue)
	elif (wProdFacilityFl):
		#	制約値設定(生産設備ID指定)
		wRtn = libc.setInputConstraintValueWithProdFacilityID(pConstraintID, pCorpID, ProdFacilityID, wDate, pValue)
	elif (wProdLineFl):
		#	制約値設定(生産ラインID指定)
		wRtn = libc.setInputConstraintValueWithProdLineID(pConstraintID, pCorpID, ProdLineID, wDate, pValue)
	elif (wItemCategoryFl):
		#	制約値設定(品目カテゴリID指定)
		wRtn = libc.setInputConstraintValueWithItemCategoryID(pConstraintID, pCorpID, ItemCategoryID, wDate, pValue)
	else:
		#	制約値設定(オプションなし)
		wRtn = libc.setInputConstraintValue(pConstraintID, pCorpID, wDate, pValue)
	return wRtn

##	----------------------------------------------------------------------------
#	@brief カレンダID変更
#
#	指定対象企業IDのカレンダIDを、指定カレンダIDへの変更を行う。
#	カレンダID無指定の場合は、未定義(空文字列)変更を行います。
#
#	@param[in] pCorpID			指定企業ISID
#	@param[in] pCalendarID		指定カレンダID

#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def set_input_cal_ID(
		pCorpID, pCalendarID=('').encode('utf-8')):

	wRtn = 0
	wRtn = libc.setInputCalendarID(pCorpID, pCalendarID)
	return wRtn

#	20230104	RM#1784_SCOエンジンコントローラの制約値およびカレンダID変更 Add end

#	----------------------------------------------------------------------------
#	実行取得関連

##
#	@brief 日毎保管量入手
#
#	日毎保管量を取得する。
#	なお、シミュレーション途中(実行は停止状態)でも取得可能とする。
#
#	@param なし
#	@return Dataframe シミュレーションデイリーログリスト(データ無し時：空リスト)
#
def get_sim_result_daily_InventoryActual():
	wRtnList = pandas.DataFrame()
	#OutputTimePoint,CompanyISID,ItemID,CompanyClassType,StorageQty,StorageAmount
	wColumns = ['OutputTimePoint', 'CompanyISID', 'ItemID', 'CompanyClassType', 'StorageQty', 'StorageAmount']

	#	出力データ数として、日毎保管量エレメント個数を取得
	wSize = libc.getResultDailyInventoryActualElementNum()
	#print(wSize)
	if (wSize <= 0):
		#	空データ作成
		wRtnList = pandas.DataFrame(index=[], columns=wColumns)
		return wRtnList

	wTempList = []
	for i in range(0,wSize):
		#	出力日時を取得
		wDateStr = (libc.getResultDailyInventoryActualDateTime(i)).decode(encoding='utf-8')
		wDatetime = datetime.datetime.strptime(wDateStr, '%Y/%m/%d %H:%M:%S')

		#	企業インスタンスIDを取得
		wCorpID = (libc.getResultDailyInventoryActualCorpID(i)).decode(encoding='utf-8')
		#	品目IDを取得
		wItemID = (libc.getResultDailyInventoryActualItemID(i)).decode(encoding='utf-8')
		#	企業クラスタイプを取得
		wCCType = (libc.getResultDailyInventoryActualCCType(i)).decode(encoding='utf-8')
		#	実数在庫量使用フラグを取得
		wRealQtyFl = libc.getResultDailyInventoryActualRealQtyFl(i)

		#	整数在庫量を取得
		wQty = libc.getResultDailyInventoryActualIntQty(i)
		#	実数在庫量を取得
		wQtyDbl = libc.getResultDailyInventoryActualDblQty(i)
		#	在庫価格換算を取得
		wAmount = libc.getResultDailyInventoryActualAmount(i)
		#print(wDatetime)
		#print(wCorpID)
		#print(wItemID)
		#print(wCCType)
		#print(wRealQtyFl)
		#print(wQty)
		#print(wQtyDbl)
		#print(wAmount)
		if (wRealQtyFl == 0):
			#	実数在庫量使用フラグが整数在庫量使用
			wAppend = [wDatetime, wCorpID, wItemID, wCCType, wQty, wAmount]
		else:
			#	実数在庫量使用フラグが実数在庫量使用
			wAppend = [wDatetime, wCorpID, wItemID, wCCType, wQtyDbl, wAmount]

		#	取得したデータをDataframeリストに追加
		wTempList.append(wAppend)
	wRtnList = pandas.DataFrame(wTempList, columns=wColumns)

	return wRtnList

##	----------------------------------------------------------------------------
#	@brief 日毎出庫実績入手
#
#	日毎出庫実績を取得する。
#	なお、シミュレーション途中(実行は停止状態)でも取得可能とする。
#
#	@param なし
#	@return Dataframe シミュレーションデイリーログリスト(データ無し時：空リスト)
#
def get_sim_result_daily_ShipActual():
	wRtnList = pandas.DataFrame()
	#OutputTimePoint,CompanyISID,ItemID,ToCompanyISID,TransportType,TransportMeanID,TransportMeanName,ShipReqQty,ShipQty,ShipReqAmount,ShipAmount,LT
	wColumns = ['OutputTimePoint', 'CompanyISID', 'ItemID', 'ToCompanyISID', 'TransportType', 'TransportMeanID', 'TransportMeanName', 'ShipReqQty', 'ShipQty', 'ShipReqAmount', 'ShipAmount', 'LT']

	#	出力データ数として、日毎出庫実績エレメント個数を取得
	wSize = libc.getResultDailyShipActualElementNum()
	#print(wSize)
	if (wSize <= 0):
		#	空データ作成
		wRtnList = pandas.DataFrame(index=[], columns=wColumns)
		return wRtnList
	wTempList = []
	for i in range(0,wSize):

		#	出力日時を取得
		wDateStr = (libc.getResultDailyShipActualDateTime(i)).decode(encoding='utf-8')
		wDatetime = datetime.datetime.strptime(wDateStr, '%Y/%m/%d %H:%M:%S')

		#	企業インスタンスIDを取得
		wCorpID = (libc.getResultDailyShipActualCorpID(i)).decode(encoding='utf-8')
		#	品目IDを取得
		wItemID = (libc.getResultDailyShipActualItemID(i)).decode(encoding='utf-8')
		#	入庫側企業インスタンスIDを取得
		wToCorpID = (libc.getResultDailyShipActualToCorpID(i)).decode(encoding='utf-8')
		#	輸送タイプ番号を取得
		wTranTypeNum = libc.getResultDailyShipActualTrantypeNum(i)
		#	輸送手段IDを取得
		wTranMeanID = (libc.getResultDailyShipActualTranMeanID(i)).decode(encoding='utf-8')
		#	輸送手段名称を取得
		wTranMeanName = (libc.getResultDailyShipActualTranMeanName(i)).decode(encoding='utf-8')
		#	出庫要求量を取得
		wShipReqQty = libc.getResultDailyShipActualShipReqQty(i)
		#	出庫量を取得
		wShipQty = libc.getResultDailyShipActualShipQty(i)
		#	出庫要求金額を取得
		wReqAmountDbl = libc.getResultDailyShipActualShipReqAmount(i)
		#	出庫金額を取得
		wAmountDbl = libc.getResultDailyShipActualShipAmount(i)
		#	輸送LTを取得
		wTranLT = libc.getResultDailyShipActualTranLT(i)
		#print(wDatetime)
		#print(wCorpID)
		#print(wItemID)
		#print(wToCorpID)
		#print(wTranTypeNum)
		#print(wTranMeanID)
		#print(wTranMeanName)
		#print(wShipReqQty)
		#print(wShipQty)
		#print(wReqAmountDbl)
		#print(wAmountDbl)
		#print(wTranLT)
		wAppend = [wDatetime, wCorpID, wItemID, wToCorpID, wTranTypeNum, wTranMeanID, wTranMeanName, wShipReqQty, wShipQty, wReqAmountDbl, wAmountDbl, wTranLT]
		#	取得したデータをDataframeリストに追加
		wTempList.append(wAppend)
	wRtnList = pandas.DataFrame(wTempList, columns=wColumns)

	return wRtnList

##	----------------------------------------------------------------------------
#	@brief イベント出庫実績入手
#
#	イベント出庫実績を取得する。
#	なお、シミュレーション途中(実行は停止状態)でも取得可能とする。
#
#	@param なし
#	@return Dataframe シミュレーションイベントログリスト(データ無し時：空リスト)
#
def get_sim_result_event_ShipActual():
	wRtnList = pandas.DataFrame()
	#OutputTimePoint,CompanyISID,ItemID,ToCompanyISID,TransportType,TransportMeanID,TransportMeanName,ShipReqQty,ShipQty,ShipReqAmount,ShipAmount,LT,DemandTypeID
	wColumns = ['OutputTimePoint', 'CompanyISID', 'ItemID', 'ToCompanyISID', 'TransportType', 'TransportMeanID', 'TransportMeanName', 'ShipReqQty', 'ShipQty', 'ShipReqAmount', 'ShipAmount', 'LT', 'DemandTypeID']

	#	出力データ数として、イベント出庫実績エレメント個数を取得
	wSize = libc.getResultEventShipActualElementNum()
	#print(wSize)
	if (wSize <= 0):
		#	空データ作成
		wRtnList = pandas.DataFrame(index=[], columns=wColumns)
		return wRtnList
	wTempList = []
	for i in range(0,wSize):
		#	出力日時を取得
		wDateStr = (libc.getResultEventShipActualDateTime(i)).decode(encoding='utf-8')
		wDatetime = datetime.datetime.strptime(wDateStr, '%Y/%m/%d %H:%M:%S')

		#	企業インスタンスIDを取得
		wCorpID = (libc.getResultEventShipActualCorpID(i)).decode(encoding='utf-8')
		#	品目IDを取得
		wItemID = (libc.getResultEventShipActualItemID(i)).decode(encoding='utf-8')
		#	入庫側企業インスタンスIDを取得
		wToCorpID = (libc.getResultEventShipActualToCorpID(i)).decode(encoding='utf-8')
		#	輸送タイプ番号を取得
		wTranTypeNum = libc.getResultEventShipActualTrantypeNum(i)
		#	輸送手段IDを取得
		wTranMeanID = (libc.getResultEventShipActualTranMeanID(i)).decode(encoding='utf-8')
		#	輸送手段名称を取得
		wTranMeanName = (libc.getResultEventShipActualTranMeanName(i)).decode(encoding='utf-8')
		#	出庫要求量を取得
		wShipReqQty = libc.getResultEventShipActualShipReqQty(i)
		#	出庫量を取得
		wShipQty = libc.getResultEventShipActualShipQty(i)
		#	出庫要求金額を取得
		wReqAmountDbl = libc.getResultEventShipActualShipReqAmount(i)
		#	出庫金額を取得
		wAmountDbl = libc.getResultEventShipActualShipAmount(i)
		#	輸送LTを取得
		wTranLT = libc.getResultEventShipActualTranLT(i)
		#	需要優先度IDを取得
		wDemandPriorityID = (libc.getResultEventShipActualDemandPriorityID(i)).decode(encoding='utf-8')
		#print(wDatetime)
		#print(wCorpID)
		#print(wItemID)
		#print(wToCorpID)
		#print(wTranTypeNum)
		#print(wTranMeanID)
		#print(wTranMeanName)
		#print(wShipReqQty)
		#print(wShipQty)
		#print(wReqAmountDbl)
		#print(wAmountDbl)
		#print(wTranLT)
		#print(wDemandPriorityID)
		wAppend = [wDatetime, wCorpID, wItemID, wToCorpID, wTranTypeNum, wTranMeanID, wTranMeanName, wShipReqQty, wShipQty, wReqAmountDbl, wAmountDbl, wTranLT, wDemandPriorityID]
		#	取得したデータをDataframeリストに追加
		wTempList.append(wAppend)
	wRtnList = pandas.DataFrame(wTempList, columns=wColumns)

	return wRtnList

##	----------------------------------------------------------------------------
#	@brief ログ注文入手
#
#	ログ注文を取得する。
#	なお、シミュレーション途中(実行は停止状態)でも取得可能とする。
#
#	@param なし
#	@return Dataframe シミュレーションログリスト(データ無し時：空リスト)
#
def get_sim_result_log_PurchaseOrder():
	wRtnList = pandas.DataFrame()

	#OutputTimePoint,CompanyISID,ItemID,FromCompanyISID,DateOfIssue,ArrivalRequestDate,ShipReqDate,Quantity,ArrivalSettled,TransportType,TransportMeanID,TransportMeanName,DemandTypeID
	wColumns = ['OutputTimePoint', 'CompanyISID', 'ItemID', 'FromCompanyISID', 'DateOfIssue', 'ArrivalRequestDate', 'ShipReqDate', 'Quantity', 'ArrivalSettled', 'TransportType', 'TransportMeanID', 'TransportMeanName', 'DemandTypeID']
	
	#	保存リスト
	wSaveListFl = 1
	#	保存リスト出力データ数として、ログ注文エレメント個数を取得
	wSize = libc.getResultLogPurchaseOrderElementNum(wSaveListFl)
	#print(wSize)
	if (wSize <= 0):
		#	空データ作成
		wRtnList = pandas.DataFrame(index=[], columns=wColumns)
		return wRtnList
	wTempList = []
	for i in range(0,wSize):
		wInvalidFl = libc.getResultLogPurchaseOrderInvalid(wSaveListFl,i)
		if (wInvalidFl != 0):
			continue

		#	出力日時を取得
		wDateStr = (libc.getResultLogPurchaseOrderDateTime(wSaveListFl,i)).decode(encoding='utf-8')
		wDatetimePoint = datetime.datetime.strptime(wDateStr, '%Y/%m/%d %H:%M:%S')

		#	企業インスタンスIDを取得
		wCorpID = (libc.getResultLogPurchaseOrderToCorpID(wSaveListFl,i)).decode(encoding='utf-8')
		#	品目IDを取得
		wItemID = (libc.getResultLogPurchaseOrderItemID(wSaveListFl,i)).decode(encoding='utf-8')
		#	出庫側企業インスタンスIDを取得
		wFromCorpID = (libc.getResultLogPurchaseOrderFromCorpID(wSaveListFl,i)).decode(encoding='utf-8')

		#	発効日を取得
		wDateStr = (libc.getResultLogPurchaseOrderDateOfIssue(wSaveListFl,i)).decode(encoding='utf-8')
		wDatetime = datetime.datetime.strptime(wDateStr, '%Y/%m/%d')
		wDateOfIssue = datetime.date(wDatetime.year, wDatetime.month, wDatetime.day)

		#	入庫要求日を取得
		wDateStr = (libc.getResultLogPurchaseOrderArrivalRequestDate(wSaveListFl,i)).decode(encoding='utf-8')
		wDatetime = datetime.datetime.strptime(wDateStr, '%Y/%m/%d')
		wArrivalRequestDate = datetime.date(wDatetime.year, wDatetime.month, wDatetime.day)

		#	出庫要求日を取得
		wDateStr = (libc.getResultLogPurchaseOrderShipReqDate(wSaveListFl,i)).decode(encoding='utf-8')
		wDatetime = datetime.datetime.strptime(wDateStr, '%Y/%m/%d')
		wShipReqDate = datetime.date(wDatetime.year, wDatetime.month, wDatetime.day)

		#	要求量を取得
		wQuantity = libc.getResultLogPurchaseOrderQuantity(wSaveListFl,i)
		#	着荷済量を取得
		wArrivalSettled = libc.getResultLogPurchaseOrderArrivalSettled(wSaveListFl,i)
		#	輸送タイプ番号を取得
		wTranTypeNum = libc.getResultLogPurchaseOrderTrantypeNum(wSaveListFl,i)
		#	輸送手段IDを取得
		wTranMeanID = (libc.getResultLogPurchaseOrderTranMeanID(wSaveListFl,i)).decode(encoding='utf-8')
		#	輸送手段名称を取得
		wTranMeanName = (libc.getResultLogPurchaseOrderTranMeanName(wSaveListFl,i)).decode(encoding='utf-8')
		#	需要優先度IDを取得
		wDemandPriorityID = (libc.getResultLogPurchaseOrderDemandPriorityID(wSaveListFl,i)).decode(encoding='utf-8')

		#print(wDatetimePoint)
		#print(wCorpID)
		#print(wItemID)
		#print(wFromCorpID)
		#print(wDateOfIssue)
		#print(wArrivalRequestDate)
		#print(wShipReqDate)
		#print(wQuantity)
		#print(wArrivalSettled)
		#print(wTranTypeNum)
		#print(wTranMeanID)
		#print(wTranMeanName)
		#print(wDemandPriorityID)
		wAppend = [wDatetime, wCorpID, wItemID, wFromCorpID, wDateOfIssue, wArrivalRequestDate, wShipReqDate, wQuantity, wArrivalSettled, wTranTypeNum, wTranMeanID, wTranMeanName, wDemandPriorityID]
		#	取得したデータ(保存リスト)をDataframeリストに追加
		wTempList.append(wAppend)

	#	通常リスト
	wSaveListFl = 0

	#	通常リスト出力データ数として、ログ注文エレメント個数を取得
	wSize = libc.getResultLogPurchaseOrderElementNum(wSaveListFl)
	#print(wSize)
	if (wSize <= 0):
		return wRtnList

	for i in range(0,wSize):
		#	ログ注文エレメント無効フラグを取得
		wInvalidFl = libc.getResultLogPurchaseOrderInvalid(wSaveListFl,i)
		if (wInvalidFl != 0):
			continue

		#	出力日時を取得
		wDateStr = (libc.getResultLogPurchaseOrderDateTime(wSaveListFl,i)).decode(encoding='utf-8')
		wDatetimePoint = datetime.datetime.strptime(wDateStr, '%Y/%m/%d %H:%M:%S')

		#	企業インスタンスIDを取得
		wCorpID = (libc.getResultLogPurchaseOrderToCorpID(wSaveListFl,i)).decode(encoding='utf-8')
		#	品目IDを取得
		wItemID = (libc.getResultLogPurchaseOrderItemID(wSaveListFl,i)).decode(encoding='utf-8')
		#	出庫側企業インスタンスIDを取得
		wFromCorpID = (libc.getResultLogPurchaseOrderFromCorpID(wSaveListFl,i)).decode(encoding='utf-8')

		#	発効日を取得
		wDateStr = (libc.getResultLogPurchaseOrderDateOfIssue(wSaveListFl,i)).decode(encoding='utf-8')
		wDatetime = datetime.datetime.strptime(wDateStr, '%Y/%m/%d')
		wDateOfIssue = datetime.date(wDatetime.year, wDatetime.month, wDatetime.day)

		#	入庫要求日を取得
		wDateStr = (libc.getResultLogPurchaseOrderArrivalRequestDate(wSaveListFl,i)).decode(encoding='utf-8')
		wDatetime = datetime.datetime.strptime(wDateStr, '%Y/%m/%d')
		wArrivalRequestDate = datetime.date(wDatetime.year, wDatetime.month, wDatetime.day)

		#	出庫要求日を取得
		wDateStr = (libc.getResultLogPurchaseOrderShipReqDate(wSaveListFl,i)).decode(encoding='utf-8')
		wDatetime = datetime.datetime.strptime(wDateStr, '%Y/%m/%d')
		wShipReqDate = datetime.date(wDatetime.year, wDatetime.month, wDatetime.day)

		#	要求量を取得
		wQuantity = libc.getResultLogPurchaseOrderQuantity(wSaveListFl,i)
		#	着荷済量を取得
		wArrivalSettled = libc.getResultLogPurchaseOrderArrivalSettled(wSaveListFl,i)
		#	輸送タイプ番号を取得
		wTranTypeNum = libc.getResultLogPurchaseOrderTrantypeNum(wSaveListFl,i)
		#	輸送手段IDを取得
		wTranMeanID = (libc.getResultLogPurchaseOrderTranMeanID(wSaveListFl,i)).decode(encoding='utf-8')
		#	輸送手段名称を取得
		wTranMeanName = (libc.getResultLogPurchaseOrderTranMeanName(wSaveListFl,i)).decode(encoding='utf-8')
		#	需要優先度IDを取得
		wDemandPriorityID = (libc.getResultLogPurchaseOrderDemandPriorityID(wSaveListFl,i)).decode(encoding='utf-8')

		#print(wDatetimePoint)
		#print(wCorpID)
		#print(wItemID)
		#print(wFromCorpID)
		#print(wDateOfIssue)
		#print(wArrivalRequestDate)
		#print(wShipReqDate)
		#print(wQuantity)
		#print(wArrivalSettled)
		#print(wTranTypeNum)
		#print(wTranMeanID)
		#print(wTranMeanName)
		#print(wDemandPriorityID)
		wAppend = [wDatetime, wCorpID, wItemID, wFromCorpID, wDateOfIssue, wArrivalRequestDate, wShipReqDate, wQuantity, wArrivalSettled, wTranTypeNum, wTranMeanID, wTranMeanName, wDemandPriorityID]
		#	取得したデータ(通常リスト)をDataframeリストに追加
		wTempList.append(wAppend)
	wRtnList = pandas.DataFrame(wTempList, columns=wColumns)

	return wRtnList

#	----------------------------------------------------------------------------
#	KPI計算関連

##	----------------------------------------------------------------------------
#	@brief 需要充足率計算
#
#	指定企業-品目の需要充足率をdaily/ActualDemand.csvから計算する。
#	なお、シミュレーション途中(実行は停止状態)でも取得可能とする。
#	計算期間を指定した場合、指定範囲に入っている情報のみ使用します。
#
#	@param[in] CorpISID 		指定企業 省略時:(全市場)
#	@param[in] ItemID 			指定品目 省略時:(全品目)
#	@param[in] CalcStartDate	指定計算開始日(未指定:=省略)
#	@param[in] CalcEndDate		指定計算終了日(未指定:=省略)
#
#	@return double 計算値(エラー時:<0.0)
#	@retval >=0.0 需要充足率計算値
#	@retval eERR_ERR_DATA_FAIL(-1.0) データ系エラー(『需要なし』も含む)
#	@retval eERR_ERR_SYSTEM_FAIL(-2.0) システム系エラー
#
#	20221021	RM#1766_SCOエンジンコントローラのパラメータおよびKPI種別追加 DA start
#def get_kpi_order_fill_rate(pCorpISID, pItemID):
#	20230123	RM#1788_SCOエンジンコントローラのKPI計算期間の指定 DA start
#def get_kpi_order_fill_rate(CorpISID=('').encode('utf-8'), ItemID=('').encode('utf-8')):
def get_kpi_order_fill_rate(CorpISID=('').encode('utf-8'), ItemID=('').encode('utf-8'), CalcStartDate=datetime.date(1970, 1, 1), CalcEndDate=datetime.date(1970, 1, 1)):
#	20230123	RM#1788_SCOエンジンコントローラのKPI計算期間の指定 DA end
#	20221021	RM#1766_SCOエンジンコントローラのパラメータおよびKPI種別追加 DA end

	#	20230123	RM#1788_SCOエンジンコントローラのKPI計算期間の指定 Add start
	#	範囲日付確認
	wLimitDate = datetime.date(1971, 1, 1)
	wCalcStartDateStr = ("").encode('utf-8')
	wCalcEndDateStr = ("").encode('utf-8')
	if (CalcStartDate > wLimitDate):
		wCalcStartDateStr = CalcStartDate.strftime('%Y/%m/%d').encode('utf-8')
	if (CalcEndDate > wLimitDate):
		wCalcEndDateStr = CalcEndDate.strftime('%Y/%m/%d').encode('utf-8')

	#	20230123	RM#1788_SCOエンジンコントローラのKPI計算期間の指定 Add end
	#	需要充足率計算値を取得
	#	20221021	RM#1766_SCOエンジンコントローラのパラメータおよびKPI種別追加 DA start
	#	wRtn = libc.getKPIOrderFillRate(pCorpISID, pItemID)
	#	20230123	RM#1788_SCOエンジンコントローラのKPI計算期間の指定 Add start
	#	wRtn = libc.getKPIOrderFillRate(CorpISID, ItemID)
	wRtn = libc.getKPIOrderFillRate(CorpISID, ItemID, wCalcStartDateStr, wCalcEndDateStr)
	#	20230123	RM#1788_SCOエンジンコントローラのKPI計算期間の指定 Add end
	#	20221021	RM#1766_SCOエンジンコントローラのパラメータおよびKPI種別追加 DA end
	return wRtn

##	----------------------------------------------------------------------------
#	@brief 需要充足率計算(平均計算)
#
#	指定企業-品目の需要充足率(平均計算)をdaily/ShipActual.csvから計算する。
#	なお、シミュレーション途中(実行は停止状態)でも取得可能とする。
#
#	@param[in] pCorpISID 指定企業ISID(出庫側)
#	@param[in] pItemID 指定品目ID
#	@param[in] CalcStartDate	指定計算開始日(未指定:=省略)
#	@param[in] CalcEndDate		指定計算終了日(未指定:=省略)
#
#	@return double 計算値(エラー時:<0.0)
#	@retval >=0.0 需要充足率計算値
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def get_kpi_order_fill_rate_d1(pCorpISID, pItemID):
	#	需要充足率(平均)計算値を取得
	wRtn = libc.getKPIOrderFillRateAverage(pCorpISID, pItemID)
	return wRtn

##	----------------------------------------------------------------------------
#	@brief 平均在庫計算
#
#	指定企業-品目の平均在庫量をdaily/InventoryActual.csvから計算する。
#	なお、シミュレーション途中(実行は停止状態)でも取得可能とする。
#
#	@param[in] CorpISID 		指定企業 省略時:(全対象企業)
#	@param[in] ItemID 			指定品目 省略時:(全品目)
#	@param[in] CalcStartDate	指定計算開始日(未指定:=省略)
#	@param[in] CalcEndDate		指定計算終了日(未指定:=省略)
#
#	@return double 計算値(エラー時:<0.0)
#	@retval >=0.0 平均在庫計算値
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
#	20221021	RM#1766_SCOエンジンコントローラのパラメータおよびKPI種別追加 DA start
#	def get_kpi_average_inventory(pCorpISID, pItemID):
def get_kpi_average_inventoryQty(CorpISID=('').encode('utf-8'), ItemID=('').encode('utf-8'), CalcStartDate=datetime.date(1970, 1, 1), CalcEndDate=datetime.date(1970, 1, 1)):
#	20221021	RM#1766_SCOエンジンコントローラのパラメータおよびKPI種別追加 DA end
	#	20230123	RM#1788_SCOエンジンコントローラのKPI計算期間の指定 Add start
	#	範囲日付確認
	wLimitDate = datetime.date(1971, 1, 1)
	wCalcStartDateStr = ("").encode('utf-8')
	wCalcEndDateStr = ("").encode('utf-8')
	if (CalcStartDate > wLimitDate):
		wCalcStartDateStr = CalcStartDate.strftime('%Y/%m/%d').encode('utf-8')
	if (CalcEndDate > wLimitDate):
		wCalcEndDateStr = CalcEndDate.strftime('%Y/%m/%d').encode('utf-8')
	#	20230123	RM#1788_SCOエンジンコントローラのKPI計算期間の指定 Add end
	#	平均在庫計算値を取得
	#	20221021	RM#1766_SCOエンジンコントローラのパラメータおよびKPI種別追加 DA start
	#	wRtn = libc.getKPIAverageInventory(pCorpISID, pItemID)
	#	20230123	RM#1788_SCOエンジンコントローラのKPI計算期間の指定 DA start
	#	wRtn = libc.getKPIAverageInventoryQty(CorpISID, ItemID)
	#	20230123	RM#1788_SCOエンジンコントローラのKPI計算期間の指定 DA start
	#	wRtn = libc.getKPIAverageInventoryQty(CorpISID, ItemID)
	wRtn = libc.getKPIAverageInventoryQty(CorpISID, ItemID, wCalcStartDateStr, wCalcEndDateStr)
	#	20230123	RM#1788_SCOエンジンコントローラのKPI計算期間の指定 DA end
	#	20230123	RM#1788_SCOエンジンコントローラのKPI計算期間の指定 DA end

	#	20221021	RM#1766_SCOエンジンコントローラのパラメータおよびKPI種別追加 DA end
	return wRtn

#	20221021	RM#1766_SCOエンジンコントローラのパラメータおよびKPI種別追加 Add start
##	----------------------------------------------------------------------------
#	@brief 平均在庫金額計算
#
#	指定企業-品目の平均在庫金額量をdaily/InventoryActual.csvから計算する。
#	なお、シミュレーション途中(実行は停止状態)でも取得可能とする。
#
#	@param[in] CorpISID 		指定企業 省略時:(全対象企業)
#	@param[in] ItemID 			指定品目 省略時:(全品目)
#	@param[in] CalcStartDate	指定計算開始日(未指定:=省略)
#	@param[in] CalcEndDate		指定計算終了日(未指定:=省略)
#
#	@return double 計算値(エラー時:<0.0)
#	@retval >=0.0 平均在庫金額計算値
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
#	20230123	RM#1788_SCOエンジンコントローラのKPI計算期間の指定 DA start
#	def get_kpi_average_inventoryAmount(CorpISID=('').encode('utf-8'), ItemID=('').encode('utf-8')):
def get_kpi_average_inventoryAmount(CorpISID=('').encode('utf-8'), ItemID=('').encode('utf-8'), CalcStartDate=datetime.date(1970, 1, 1), CalcEndDate=datetime.date(1970, 1, 1)):
#	20230123	RM#1788_SCOエンジンコントローラのKPI計算期間の指定 DA end
	#	20230123	RM#1788_SCOエンジンコントローラのKPI計算期間の指定 Add start
	#	範囲日付確認
	wLimitDate = datetime.date(1971, 1, 1)
	wCalcStartDateStr = ("").encode('utf-8')
	wCalcEndDateStr = ("").encode('utf-8')
	if (CalcStartDate > wLimitDate):
		wCalcStartDateStr = CalcStartDate.strftime('%Y/%m/%d').encode('utf-8')
	if (CalcEndDate > wLimitDate):
		wCalcEndDateStr = CalcEndDate.strftime('%Y/%m/%d').encode('utf-8')
	#	20230123	RM#1788_SCOエンジンコントローラのKPI計算期間の指定 Add end
	#	平均在庫計算値を取得
	#	20230123	RM#1788_SCOエンジンコントローラのKPI計算期間の指定 DA start
	#	wRtn = libc.getKPIAverageInventoryAmount(CorpISID, ItemID)
	wRtn = libc.getKPIAverageInventoryAmount(CorpISID, ItemID, wCalcStartDateStr, wCalcEndDateStr)
	#	20230123	RM#1788_SCOエンジンコントローラのKPI計算期間の指定 DA end
	return wRtn
#	20221021	RM#1766_SCOエンジンコントローラのパラメータおよびKPI種別追加 Add end

##	----------------------------------------------------------------------------
#	@brief CO2排出量計算
#
#	指定企業-品目のCO2排出量合計を計算する。
#	なお、シミュレーション途中(実行は停止状態)でも取得可能とする。
#
#	@param[in] pCorpISID 指定企業ISID(出庫側)
#	@param[in] pItemID 指定品目ID
#	@return double 計算値(エラー時:<0.0)
#	@retval >=0.0 CO2排出量計算値
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def get_kpi_CO2(pCorpISID, pItemID):
	#	指定企業-品目のCO2排出量合計値を取得
	wRtn = libc.getKPICO2(pCorpISID, pItemID)
	return wRtn

#	20230605	RM#1825_リスク評価対応型エンジンコントローラ Add start
#	----------------------------------------------------------------------------
#	リスク評価対応関連


##	----------------------------------------------------------------------------
#	@brief 在庫取得
#
#	現在指定企業-品目の在庫量を取得する。
#	なお、シミュレーション途中(実行は停止状態)でも取得可能とする。
#
#	@param[in] CorpISID 		指定企業 省略時:(全対象企業)
#	@param[in] ItemID 			指定品目 省略時:(全品目)
#
#	@return int/double 計算値(エラー時:<0.0)
#	@retval >=0.0 在庫計算値
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def get_kpi_inventoryQty(CorpISID=('').encode('utf-8'), ItemID=('').encode('utf-8')):

	wRtnFl = libc.checktKPIInventoryQtyInt(CorpISID, ItemID)
	if (wRtnFl == 1):
		#	対象企業在庫量取得(整数)
		wRtn = libc.getKPIInventoryQtyInt(CorpISID, ItemID)
	else:
		#	対象企業在庫量取得(実数)
		wRtn = libc.getKPIInventoryQtyDouble(CorpISID, ItemID)
	return wRtn

##	----------------------------------------------------------------------------
#	@brief 在庫金額量取得
#
#	現在指定企業-品目の在庫金額量を取得する。
#	なお、シミュレーション途中(実行は停止状態)でも取得可能とする。
#
#	@param[in] CorpISID 		指定企業 省略時:(全対象企業)
#	@param[in] ItemID 			指定品目 省略時:(全品目)
#
#	@return double 計算値(エラー時:<0.0)
#	@retval >=0.0 金額計算値
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def get_kpi_inventoryAmount(CorpISID=('').encode('utf-8'), ItemID=('').encode('utf-8')):

	wRtn = libc.getKPIInventoryAmount(CorpISID, ItemID)
	return wRtn

##	----------------------------------------------------------------------------
#	@brief 在庫数量変更
#
#	指定企業-品目の現在在庫量を変更する。
#	なお、シミュレーション途中(実行は停止状態)でも変更可能とする。
#
#	@param[in] CorpISID 		指定企業ISID
#	@param[in] ItemID 			指定品目ID
#	@param[in] pQty				設定在庫量
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def set_SC_incident_inventory_qty(CorpISID, ItemID, pQty):
	wRtn = 0
	#	設定変数型分岐
	if (type(pQty) is int):
		wRtn = libc.setIncidentInventoryQtyInt(CorpISID, ItemID, pQty)
	else:
		wRtn = libc.setIncidentInventoryQtyDouble(CorpISID, ItemID, pQty)
	return wRtn

##	----------------------------------------------------------------------------
#	@brief 輸送中在庫リスト取得
#
#	輸送中在庫リストを取得する。
#	なお、シミュレーション途中(実行は停止状態)でも取得可能とする。
#
#	@param なし
#	@return Dataframe 輸送中在庫リスト(データ無し時：空リスト)
#
def get_SC_incident_tranWIP_list():
	wRtnList = pandas.DataFrame()
	#ID,CompanyISID,ItemID,TransportType,ArrivalDate,Qty
	wColumns = ['ID', 'CompanyISID', 'ItemID', 'TransportType', 'ArrivalDate', 'Qty']

	#	出力データ数として、輸送中在庫リストエレメント個数を取得
	wSize = libc.getSCTncidentTranWIPElementNum()
	#print(wSize)
	if (wSize <= 0):
		#	空データ作成
		wRtnList = pandas.DataFrame(index=[], columns=wColumns)
		return wRtnList
	wTempList = []
	for i in range(0,wSize):
		wFl = libc.getSCTncidentTranWIPActive(i)
		if (wFl < 0):
			#	エラー
			return wFl
		elif (wFl == 0):
			continue
		#	輸送企業インスタンスIDを取得
		wCorpID = (libc.getSCTncidentTranWIPCorpID(i)).decode(encoding='utf-8')
		#	品目IDを取得
		wItemID = (libc.getSCTncidentTranWIPItemID(i)).decode(encoding='utf-8')
		#	輸送タイプ番号を取得
		wTranTypeNum = libc.getSCTncidentTranWIPTranType(i)
		#	出力日時を取得
		wDateStr = (libc.getSCTncidentTranWIPArrivalDate(i)).decode(encoding='utf-8')
		wDatetime = datetime.datetime.strptime(wDateStr, '%Y/%m/%d')
		wArrivalDate = datetime.date(wDatetime.year, wDatetime.month, wDatetime.day)
		#	輸送量を取得
		wQty = libc.getSCTncidentTranWIPQty(i)
		#print(wCorpID)
		#print(wItemID)
		#print(wTranTypeNum)
		#print(wArrivalDate)
		#print(wQty)
		wAppend = [i, wCorpID, wItemID, wTranTypeNum, wArrivalDate, wQty]
		#	取得したデータをDataframeリストに追加
		wTempList.append(wAppend)
	wRtnList = pandas.DataFrame(wTempList, columns=wColumns)

	return wRtnList

##	----------------------------------------------------------------------------
#	@brief 輸送中在庫変更
#
#	指定対象リストIDの輸送中在庫を変更する。
#	なお、シミュレーション途中(実行は停止状態)でも変更可能とする。
#
#	@param[in] pListID 		変更対象リストID
#	@param[in] pQty			設定在庫量
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def set_SC_incident_tranWIP_qty(pListID, pQty):

	wRtn = libc.setSCTncidentTranWIPQty(pListID, pQty)
	return wRtn

##	----------------------------------------------------------------------------
#	@brief 生産中在庫リスト取得
#
#	工場生産中リストを取得する。
#	なお、シミュレーション途中(実行は停止状態)でも取得可能とする。
#
#	@param なし
#	@return Dataframe 生産中在庫リスト(データ無し時：空リスト)
#
def get_SC_incident_prodWIP_list():
	wRtnList = pandas.DataFrame()
	#ID,CompanyISID,ItemID,TransportType,ArrivalDate,Qty
	wColumns = ['ID', 'CompanyISID', 'ItemID', 'CompletionDate', 'Qty']

	#	出力データ数として、生産中在庫リストエレメント個数を取得
	wSize = libc.getSCTncidentProdWIPElementNum()
	#print(wSize)
	if (wSize <= 0):
		#	空データ作成
		wRtnList = pandas.DataFrame(index=[], columns=wColumns)
		return wRtnList
	wTempList = []
	for i in range(0,wSize):
		wFl = libc.getSCTncidentProdWIPActive(i)
		if (wFl < 0):
			#	エラー
			return wFl
		elif (wFl == 0):
			continue
		#	企業インスタンスIDを取得
		wCorpID = (libc.getSCTncidentTranWIPCorpID(i)).decode(encoding='utf-8')
		#	品目IDを取得
		wItemID = (libc.getSCTncidentTranWIPItemID(i)).decode(encoding='utf-8')
		#	生産/検査タイプを取得
		wProdTypeNum = libc.getSCTncidentProdWIPProdType(i)
		if (wProdTypeNum < 0):
			#	エラー
			return wFl
		elif (wProdTypeNum == 0):
			#	検査タイプ
			continue
		#	出力日時を取得
		wDateStr = (libc.getSCTncidentProdWIPCompletionDate(i)).decode(encoding='utf-8')
		wDatetime = datetime.datetime.strptime(wDateStr, '%Y/%m/%d')
		wCompletionDate = datetime.date(wDatetime.year, wDatetime.month, wDatetime.day)
		#	輸送量を取得
		wQty = libc.getSCTncidentProdWIPQty(i)
		#print(wCorpID)
		#print(wItemID)
		#print(wCompletionDate)
		#print(wQty)
		wAppend = [i, wCorpID, wItemID, wCompletionDate, wQty]
		#	取得したデータをDataframeリストに追加
		wTempList.append(wAppend)
	wRtnList = pandas.DataFrame(wTempList, columns=wColumns)

	return wRtnList

##	----------------------------------------------------------------------------
#	@brief 生産中在庫変更
#
#	指定対象リストIDのの生産中在庫量を変更する。
#	なお、シミュレーション途中(実行は停止状態)でも変更可能とする。
#
#	@param[in] pListID 		変更対象リストID
#	@param[in] pQty			設定在庫量
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def set_SC_incident_prodWIP_qty(pListID, pQty):

	#	生産/検査タイプを取得
	wProdTypeNum = libc.getSCTncidentProdWIPProdType(pListID)
	if (wProdTypeNum < 0):
		#	エラー
		return (-1)
	elif (wProdTypeNum == 0):
		#	検査タイプ
		return (-1)
	wRtn = libc.setSCTncidentProdWIPQty(pListID, pQty)
	return wRtn

##	----------------------------------------------------------------------------
#	@brief 検査中在庫リスト取得
#
#	工場検査中リストを取得する。
#	なお、シミュレーション途中(実行は停止状態)でも取得可能とする。
#
#	@param なし
#	@return Dataframe 検査中在庫リスト(データ無し時：空リスト)
#
def get_SC_incident_inspctWIP_list():
	wRtnList = pandas.DataFrame()
	#ID,CompanyISID,ItemID,TransportType,ArrivalDate,Qty
	wColumns = ['ID', 'CompanyISID', 'ItemID', 'CompletionDate', 'Qty']

	#	出力データ数として、検査中在庫リストエレメント個数を取得
	wSize = libc.getSCTncidentProdWIPElementNum()
	#print(wSize)
	if (wSize <= 0):
		#	空データ作成
		wRtnList = pandas.DataFrame(index=[], columns=wColumns)
		return wRtnList
	wTempList = []
	for i in range(0,wSize):
		wFl = libc.getSCTncidentProdWIPActive(i)
		if (wFl < 0):
			#	エラー
			return wFl
		elif (wFl == 0):
			continue
		#	企業インスタンスIDを取得
		wCorpID = (libc.getSCTncidentTranWIPCorpID(i)).decode(encoding='utf-8')
		#	品目IDを取得
		wItemID = (libc.getSCTncidentTranWIPItemID(i)).decode(encoding='utf-8')
		#	生産/検査タイプを取得
		wProdTypeNum = libc.getSCTncidentProdWIPProdType(i)
		if (wProdTypeNum < 0):
			#	エラー
			return wFl
		elif (wProdTypeNum == 1):
			#	工場タイプ
			continue
		#	出力日時を取得
		wDateStr = (libc.getSCTncidentProdWIPCompletionDate(i)).decode(encoding='utf-8')
		wDatetime = datetime.datetime.strptime(wDateStr, '%Y/%m/%d')
		wCompletionDate = datetime.date(wDatetime.year, wDatetime.month, wDatetime.day)
		#	輸送量を取得
		wQty = libc.getSCTncidentProdWIPQty(i)
		#print(wCorpID)
		#print(wItemID)
		#print(wCompletionDate)
		#print(wQty)
		wAppend = [i, wCorpID, wItemID, wCompletionDate, wQty]
		#	取得したデータをDataframeリストに追加
		wTempList.append(wAppend)
	wRtnList = pandas.DataFrame(wTempList, columns=wColumns)

	return wRtnList

##	----------------------------------------------------------------------------
#	@brief 検査中在庫変更
#
#	指定対象リストIDのの検査中在庫量を変更する。
#	なお、シミュレーション途中(実行は停止状態)でも変更可能とする。
#
#	@param[in] pListID 		変更対象リストID
#	@param[in] pQty			設定在庫量
#	@return int 成否 (正常:=0 エラー!=0)
#	@retval eEXIT_SUCCESS(0) 成功
#	@retval eERR_ERR_DATA_FAIL(-1) データ系エラー
#	@retval eERR_ERR_SYSTEM_FAIL(-2) システム系エラー
#
def set_SC_incident_inspctWIP_qty(pListID, pQty):

	wProdTypeNum = libc.getSCTncidentProdWIPProdType(pListID)
	if (wProdTypeNum < 0):
		#	エラー
		return (-1)
	elif (wProdTypeNum == 1):
		#	工場タイプ
		return (-1)
	wRtn = libc.setSCTncidentProdWIPQty(pListID, pQty)
	return wRtn

#	20230605	RM#1825_リスク評価対応型エンジンコントローラ Add end

#	end of file library.py
