# Databricks notebook source
# MAGIC %run "./udf_informatica"

# COMMAND ----------


from pyspark.sql.types import *

spark.sql("use DELTA_TRAINING")
spark.sql("set spark.sql.legacy.timeParserPolicy = LEGACY")


# COMMAND ----------
# DBTITLE 1, Shortcut_to_SEQ_MA_EVENT_ID


spark.sql(
  """CREATE TABLE IF NOT EXISTS Shortcut_to_SEQ_MA_EVENT_ID(NEXTVAL BIGINT,
CURRVAL BIGINT,
Increment_By Int);"""
)

spark.sql(
  """INSERT INTO Shortcut_to_SEQ_MA_EVENT_ID(NEXTVAL BIGINT,
CURRVAL BIGINT,
Increment_By Int) VALUES(2, 1, 1)"""
)

# COMMAND ----------
# DBTITLE 1, Shortcut_to_MA_DC_COST_ADJ_CTRL1_1


df_1 = spark.sql("""SELECT
  FISCAL_MO AS FISCAL_MO,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  EST_DC_COST_USD AS EST_DC_COST_USD,
  ACT_DC_COST_USD AS ACT_DC_COST_USD,
  DC_COST_ADJ_PCT AS DC_COST_ADJ_PCT,
  UPDATE_TSTMP AS UPDATE_TSTMP,
  LOAD_TSTMP AS LOAD_TSTMP
FROM
  MA_DC_COST_ADJ_CTRL""")

df_1.createOrReplaceTempView("Shortcut_to_MA_DC_COST_ADJ_CTRL1_1")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_MA_DC_COST_ADJ_CTRL_2


df_2 = spark.sql("""SELECT
  FISCAL_MO AS FISCAL_MO,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  EST_DC_COST_USD AS EST_DC_COST_USD,
  ACT_DC_COST_USD AS ACT_DC_COST_USD,
  DC_COST_ADJ_PCT AS DC_COST_ADJ_PCT,
  UPDATE_TSTMP AS UPDATE_TSTMP,
  LOAD_TSTMP AS LOAD_TSTMP
FROM
  MA_DC_COST_ADJ_CTRL""")

df_2.createOrReplaceTempView("Shortcut_to_MA_DC_COST_ADJ_CTRL_2")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_MA_EVENT11_3


df_3 = spark.sql("""SELECT
  MA_EVENT_ID AS MA_EVENT_ID,
  OFFER_ID AS OFFER_ID,
  SAP_DEPT_ID AS SAP_DEPT_ID,
  PRODUCT_ID AS PRODUCT_ID,
  COUNTRY_CD AS COUNTRY_CD,
  START_DT AS START_DT,
  END_DT AS END_DT,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  LOCATION_ID AS LOCATION_ID,
  MOVEMENT_ID AS MOVEMENT_ID,
  VALUATION_CLASS_CD AS VALUATION_CLASS_CD,
  GL_ACCT_NBR AS GL_ACCT_NBR,
  LOCATION_TYPE_ID AS LOCATION_TYPE_ID,
  ROYALTY_BRAND_ID AS ROYALTY_BRAND_ID,
  BRAND_CD AS BRAND_CD,
  MA_FORMULA_CD AS MA_FORMULA_CD,
  FISCAL_MO AS FISCAL_MO,
  SAP_CATEGORY_ID AS SAP_CATEGORY_ID,
  FROM_LOCATION_ID AS FROM_LOCATION_ID,
  SOURCE_VENDOR_ID AS SOURCE_VENDOR_ID,
  COMPANY_ID AS COMPANY_ID,
  MA_EVENT_DESC AS MA_EVENT_DESC,
  EM_VENDOR_FUNDING_ID AS EM_VENDOR_FUNDING_ID,
  EM_COMMENT AS EM_COMMENT,
  EM_BILL_ALT_VENDOR_FLAG AS EM_BILL_ALT_VENDOR_FLAG,
  EM_ALT_VENDOR_ID AS EM_ALT_VENDOR_ID,
  EM_ALT_VENDOR_NAME AS EM_ALT_VENDOR_NAME,
  EM_ALT_VENDOR_COUNTRY_CD AS EM_ALT_VENDOR_COUNTRY_CD,
  EM_VENDOR_ID AS EM_VENDOR_ID,
  EM_VENDOR_NAME AS EM_VENDOR_NAME,
  EM_VENDOR_COUNTRY_CD AS EM_VENDOR_COUNTRY_CD,
  VENDOR_NAME_TXT AS VENDOR_NAME_TXT,
  MA_PCT_IND AS MA_PCT_IND,
  MA_AMT AS MA_AMT,
  MA_MAX_AMT AS MA_MAX_AMT,
  UPDATE_DT AS UPDATE_DT,
  LOAD_DT AS LOAD_DT
FROM
  MA_EVENT""")

df_3.createOrReplaceTempView("Shortcut_to_MA_EVENT11_3")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_MA_EVENT1_4


df_4 = spark.sql("""SELECT
  MA_EVENT_ID AS MA_EVENT_ID,
  OFFER_ID AS OFFER_ID,
  SAP_DEPT_ID AS SAP_DEPT_ID,
  PRODUCT_ID AS PRODUCT_ID,
  COUNTRY_CD AS COUNTRY_CD,
  START_DT AS START_DT,
  END_DT AS END_DT,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  LOCATION_ID AS LOCATION_ID,
  MOVEMENT_ID AS MOVEMENT_ID,
  VALUATION_CLASS_CD AS VALUATION_CLASS_CD,
  GL_ACCT_NBR AS GL_ACCT_NBR,
  LOCATION_TYPE_ID AS LOCATION_TYPE_ID,
  ROYALTY_BRAND_ID AS ROYALTY_BRAND_ID,
  BRAND_CD AS BRAND_CD,
  MA_FORMULA_CD AS MA_FORMULA_CD,
  FISCAL_MO AS FISCAL_MO,
  SAP_CATEGORY_ID AS SAP_CATEGORY_ID,
  FROM_LOCATION_ID AS FROM_LOCATION_ID,
  SOURCE_VENDOR_ID AS SOURCE_VENDOR_ID,
  COMPANY_ID AS COMPANY_ID,
  MA_EVENT_DESC AS MA_EVENT_DESC,
  EM_VENDOR_FUNDING_ID AS EM_VENDOR_FUNDING_ID,
  EM_COMMENT AS EM_COMMENT,
  EM_BILL_ALT_VENDOR_FLAG AS EM_BILL_ALT_VENDOR_FLAG,
  EM_ALT_VENDOR_ID AS EM_ALT_VENDOR_ID,
  EM_ALT_VENDOR_NAME AS EM_ALT_VENDOR_NAME,
  EM_ALT_VENDOR_COUNTRY_CD AS EM_ALT_VENDOR_COUNTRY_CD,
  EM_VENDOR_ID AS EM_VENDOR_ID,
  EM_VENDOR_NAME AS EM_VENDOR_NAME,
  EM_VENDOR_COUNTRY_CD AS EM_VENDOR_COUNTRY_CD,
  VENDOR_NAME_TXT AS VENDOR_NAME_TXT,
  MA_PCT_IND AS MA_PCT_IND,
  MA_AMT AS MA_AMT,
  MA_MAX_AMT AS MA_MAX_AMT,
  UPDATE_DT AS UPDATE_DT,
  LOAD_DT AS LOAD_DT
FROM
  MA_EVENT""")

df_4.createOrReplaceTempView("Shortcut_to_MA_EVENT1_4")

# COMMAND ----------
# DBTITLE 1, Shortcut_To_DAYS1_5


df_5 = spark.sql("""SELECT
  DAY_DT AS DAY_DT,
  BUSINESS_DAY_FLAG AS BUSINESS_DAY_FLAG,
  HOLIDAY_FLAG AS HOLIDAY_FLAG,
  DAY_OF_WK_NAME AS DAY_OF_WK_NAME,
  DAY_OF_WK_NAME_ABBR AS DAY_OF_WK_NAME_ABBR,
  DAY_OF_WK_NBR AS DAY_OF_WK_NBR,
  CAL_DAY_OF_MO_NBR AS CAL_DAY_OF_MO_NBR,
  CAL_DAY_OF_YR_NBR AS CAL_DAY_OF_YR_NBR,
  CAL_WK AS CAL_WK,
  CAL_WK_NBR AS CAL_WK_NBR,
  CAL_MO AS CAL_MO,
  CAL_MO_NBR AS CAL_MO_NBR,
  CAL_MO_NAME AS CAL_MO_NAME,
  CAL_MO_NAME_ABBR AS CAL_MO_NAME_ABBR,
  CAL_QTR AS CAL_QTR,
  CAL_QTR_NBR AS CAL_QTR_NBR,
  CAL_HALF AS CAL_HALF,
  CAL_YR AS CAL_YR,
  FISCAL_DAY_OF_MO_NBR AS FISCAL_DAY_OF_MO_NBR,
  FISCAL_DAY_OF_YR_NBR AS FISCAL_DAY_OF_YR_NBR,
  FISCAL_WK AS FISCAL_WK,
  FISCAL_WK_NBR AS FISCAL_WK_NBR,
  FISCAL_MO AS FISCAL_MO,
  FISCAL_MO_NBR AS FISCAL_MO_NBR,
  FISCAL_MO_NAME AS FISCAL_MO_NAME,
  FISCAL_MO_NAME_ABBR AS FISCAL_MO_NAME_ABBR,
  FISCAL_QTR AS FISCAL_QTR,
  FISCAL_QTR_NBR AS FISCAL_QTR_NBR,
  FISCAL_HALF AS FISCAL_HALF,
  FISCAL_YR AS FISCAL_YR,
  LYR_WEEK_DT AS LYR_WEEK_DT,
  LWK_WEEK_DT AS LWK_WEEK_DT,
  WEEK_DT AS WEEK_DT,
  EST_TIME_CONV_AMT AS EST_TIME_CONV_AMT,
  EST_TIME_CONV_HRS AS EST_TIME_CONV_HRS,
  ES0_TIME_CONV_AMT AS ES0_TIME_CONV_AMT,
  ES0_TIME_CONV_HRS AS ES0_TIME_CONV_HRS,
  CST_TIME_CONV_AMT AS CST_TIME_CONV_AMT,
  CST_TIME_CONV_HRS AS CST_TIME_CONV_HRS,
  CS0_TIME_CONV_AMT AS CS0_TIME_CONV_AMT,
  CS0_TIME_CONV_HRS AS CS0_TIME_CONV_HRS,
  MST_TIME_CONV_AMT AS MST_TIME_CONV_AMT,
  MST_TIME_CONV_HRS AS MST_TIME_CONV_HRS,
  MS0_TIME_CONV_AMT AS MS0_TIME_CONV_AMT,
  MS0_TIME_CONV_HRS AS MS0_TIME_CONV_HRS,
  PST_TIME_CONV_AMT AS PST_TIME_CONV_AMT,
  PST_TIME_CONV_HRS AS PST_TIME_CONV_HRS
FROM
  DAYS""")

df_5.createOrReplaceTempView("Shortcut_To_DAYS1_5")

# COMMAND ----------
# DBTITLE 1, SQ_MA_DC_COST_ADJ_CTRL_UPDATES_6


df_6 = spark.sql("""SELECT
  M.MA_EVENT_ID AS MA_EVENT_ID,
  D.START_DT AS START_DT,
  D.END_DT AS END_DT,
  M.MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  11 AS MA_EVENT_SOURCE_ID,
  D.FISCAL_MO AS FISCAL_MO,
  'DC Cost Adj: Fiscal Mo=' || MDCAC.FISCAL_MO:: VARCHAR (10) AS MA_EVENT_DESC,
  1 AS MA_PCT_IND,
  MDCAC.DC_COST_ADJ_PCT * 100 AS NEW_MA_AMT,
  M.MA_AMT AS ORIG_MA_AMT,
  'U' AS INS_UPD_FLAG,
  M.LOAD_DT AS LOAD_DT,
  monotonically_increasing_id() AS Monotonically_Increasing_Id
FROM
  Shortcut_to_MA_DC_COST_ADJ_CTRL1_1 MDCAC
  JOIN (
    SELECT
      FISCAL_MO,
      MIN(DAY_DT) START_DT,
      MAX(DAY_DT) END_DT
    FROM
      Shortcut_To_DAYS1_5
    GROUP BY
      FISCAL_MO
  ) D ON MDCAC.FISCAL_MO = D.FISCAL_MO
  JOIN Shortcut_to_MA_EVENT11_3 M ON MDCAC.MA_EVENT_TYPE_ID = M.MA_EVENT_TYPE_ID
  AND MDCAC.FISCAL_MO = M.FISCAL_MO
  AND M.MA_EVENT_SOURCE_ID = 11
WHERE
  NEW_MA_AMT <> M.MA_AMT""")

df_6.createOrReplaceTempView("SQ_MA_DC_COST_ADJ_CTRL_UPDATES_6")

# COMMAND ----------
# DBTITLE 1, EXP_ORIG_7


df_7 = spark.sql("""SELECT
  MA_EVENT_ID AS MA_EVENT_ID,
  START_DT AS START_DT,
  END_DT AS END_DT,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  FISCAL_MO AS FISCAL_MO,
  MA_EVENT_DESC AS MA_EVENT_DESC,
  MA_PCT_IND AS MA_PCT_IND,
  NEW_MA_AMT AS NEW_MA_AMT,
  ORIG_MA_AMT AS ORIG_MA_AMT,
  INS_UPD_FLAG AS INS_UPD_FLAG,
  now() AS UPDATE_DT,
  LOAD_DT AS LOAD_DT,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  SQ_MA_DC_COST_ADJ_CTRL_UPDATES_6""")

df_7.createOrReplaceTempView("EXP_ORIG_7")

# COMMAND ----------
# DBTITLE 1, Shortcut_To_DAYS_8


df_8 = spark.sql("""SELECT
  DAY_DT AS DAY_DT,
  BUSINESS_DAY_FLAG AS BUSINESS_DAY_FLAG,
  HOLIDAY_FLAG AS HOLIDAY_FLAG,
  DAY_OF_WK_NAME AS DAY_OF_WK_NAME,
  DAY_OF_WK_NAME_ABBR AS DAY_OF_WK_NAME_ABBR,
  DAY_OF_WK_NBR AS DAY_OF_WK_NBR,
  CAL_DAY_OF_MO_NBR AS CAL_DAY_OF_MO_NBR,
  CAL_DAY_OF_YR_NBR AS CAL_DAY_OF_YR_NBR,
  CAL_WK AS CAL_WK,
  CAL_WK_NBR AS CAL_WK_NBR,
  CAL_MO AS CAL_MO,
  CAL_MO_NBR AS CAL_MO_NBR,
  CAL_MO_NAME AS CAL_MO_NAME,
  CAL_MO_NAME_ABBR AS CAL_MO_NAME_ABBR,
  CAL_QTR AS CAL_QTR,
  CAL_QTR_NBR AS CAL_QTR_NBR,
  CAL_HALF AS CAL_HALF,
  CAL_YR AS CAL_YR,
  FISCAL_DAY_OF_MO_NBR AS FISCAL_DAY_OF_MO_NBR,
  FISCAL_DAY_OF_YR_NBR AS FISCAL_DAY_OF_YR_NBR,
  FISCAL_WK AS FISCAL_WK,
  FISCAL_WK_NBR AS FISCAL_WK_NBR,
  FISCAL_MO AS FISCAL_MO,
  FISCAL_MO_NBR AS FISCAL_MO_NBR,
  FISCAL_MO_NAME AS FISCAL_MO_NAME,
  FISCAL_MO_NAME_ABBR AS FISCAL_MO_NAME_ABBR,
  FISCAL_QTR AS FISCAL_QTR,
  FISCAL_QTR_NBR AS FISCAL_QTR_NBR,
  FISCAL_HALF AS FISCAL_HALF,
  FISCAL_YR AS FISCAL_YR,
  LYR_WEEK_DT AS LYR_WEEK_DT,
  LWK_WEEK_DT AS LWK_WEEK_DT,
  WEEK_DT AS WEEK_DT,
  EST_TIME_CONV_AMT AS EST_TIME_CONV_AMT,
  EST_TIME_CONV_HRS AS EST_TIME_CONV_HRS,
  ES0_TIME_CONV_AMT AS ES0_TIME_CONV_AMT,
  ES0_TIME_CONV_HRS AS ES0_TIME_CONV_HRS,
  CST_TIME_CONV_AMT AS CST_TIME_CONV_AMT,
  CST_TIME_CONV_HRS AS CST_TIME_CONV_HRS,
  CS0_TIME_CONV_AMT AS CS0_TIME_CONV_AMT,
  CS0_TIME_CONV_HRS AS CS0_TIME_CONV_HRS,
  MST_TIME_CONV_AMT AS MST_TIME_CONV_AMT,
  MST_TIME_CONV_HRS AS MST_TIME_CONV_HRS,
  MS0_TIME_CONV_AMT AS MS0_TIME_CONV_AMT,
  MS0_TIME_CONV_HRS AS MS0_TIME_CONV_HRS,
  PST_TIME_CONV_AMT AS PST_TIME_CONV_AMT,
  PST_TIME_CONV_HRS AS PST_TIME_CONV_HRS
FROM
  DAYS""")

df_8.createOrReplaceTempView("Shortcut_To_DAYS_8")

# COMMAND ----------
# DBTITLE 1, SQ_MA_DC_COST_ADJ_CTRL_INSERTS_9


df_9 = spark.sql("""SELECT
  D.START_DT AS START_DT,
  D.END_DT AS END_DT,
  MDCAC.MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  11 AS MA_EVENT_SOURCE_ID,
  MDCAC.FISCAL_MO AS FISCAL_MO,
  'DC Cost Adj: Fiscal Mo=' || MDCAC.FISCAL_MO:: VARCHAR (10) AS MA_EVENT_DESC,
  1 AS MA_PCT_IND,
  MDCAC.DC_COST_ADJ_PCT * 100 AS NEW_MA_AMT,
  NEW_MA_AMT AS ORIG_MA_AMT,
  'I' AS INS_UPD_FLAG,
  monotonically_increasing_id() AS Monotonically_Increasing_Id
FROM
  Shortcut_to_MA_DC_COST_ADJ_CTRL_2 MDCAC
  JOIN (
    SELECT
      FISCAL_MO,
      MIN(DAY_DT) START_DT,
      MAX(DAY_DT) END_DT
    FROM
      Shortcut_To_DAYS_8
    GROUP BY
      FISCAL_MO
  ) D ON MDCAC.FISCAL_MO = D.FISCAL_MO
  LEFT JOIN (
    SELECT
      *
    FROM
      Shortcut_to_MA_EVENT1_4
    WHERE
      MA_EVENT_SOURCE_ID = 11
  ) M ON MDCAC.MA_EVENT_TYPE_ID = M.MA_EVENT_TYPE_ID
  AND MDCAC.FISCAL_MO = M.FISCAL_MO
WHERE
  M.MA_EVENT_ID IS NULL""")

df_9.createOrReplaceTempView("SQ_MA_DC_COST_ADJ_CTRL_INSERTS_9")

# COMMAND ----------
# DBTITLE 1, EXP_NEW_10


df_10 = spark.sql("""SELECT
  NEXTVAL AS MA_EVENT_ID,
  START_DT AS START_DT,
  END_DT AS END_DT,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  FISCAL_MO AS FISCAL_MO,
  MA_EVENT_DESC AS MA_EVENT_DESC,
  MA_PCT_IND AS MA_PCT_IND,
  NEW_MA_AMT AS NEW_MA_AMT,
  ORIG_MA_AMT AS ORIG_MA_AMT,
  now() AS UPDATE_DT,
  now() AS LOAD_DT,
  INS_UPD_FLAG AS INS_UPD_FLAG,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  SQ_MA_DC_COST_ADJ_CTRL_INSERTS_9""")

df_10.createOrReplaceTempView("EXP_NEW_10")

spark.sql("""UPDATE SEQ_MA_EVENT_ID SET CURRVAL = (SELECT MAX(MA_EVENT_ID) FROM EXP_NEW_10) , NEXTVAL = (SELECT MAX(MA_EVENT_ID) FROM EXP_NEW_10) + (SELECT Increment_By FROM EXP_NEW_10)""")

# COMMAND ----------
# DBTITLE 1, UNI_NEW_ORIG_11


df_11 = spark.sql("""SELECT
  MA_EVENT_ID AS MA_EVENT_ID,
  START_DT AS START_DT,
  END_DT AS END_DT,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  FISCAL_MO AS FISCAL_MO,
  MA_EVENT_DESC AS MA_EVENT_DESC,
  MA_PCT_IND AS MA_PCT_IND,
  NEW_MA_AMT AS NEW_MA_AMT,
  ORIG_MA_AMT AS ORIG_MA_AMT,
  UPDATE_DT AS UPDATE_DT,
  LOAD_DT AS LOAD_DT,
  INS_UPD_FLAG AS INS_UPD_FLAG,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  EXP_ORIG_7
UNION ALL
SELECT
  MA_EVENT_ID AS MA_EVENT_ID,
  START_DT AS START_DT,
  END_DT AS END_DT,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  FISCAL_MO AS FISCAL_MO,
  MA_EVENT_DESC AS MA_EVENT_DESC,
  MA_PCT_IND AS MA_PCT_IND,
  NEW_MA_AMT AS NEW_MA_AMT,
  ORIG_MA_AMT AS ORIG_MA_AMT,
  UPDATE_DT AS UPDATE_DT,
  LOAD_DT AS LOAD_DT,
  INS_UPD_FLAG AS INS_UPD_FLAG,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  EXP_NEW_10""")

df_11.createOrReplaceTempView("UNI_NEW_ORIG_11")

# COMMAND ----------
# DBTITLE 1, EXP_INS_UPD_12


df_12 = spark.sql("""SELECT
  TRUNC(now()) AS LOAD_DT,
  MA_EVENT_ID AS MA_EVENT_ID,
  START_DT AS START_DT,
  END_DT AS END_DT,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  FISCAL_MO AS FISCAL_MO,
  MA_EVENT_DESC AS MA_EVENT_DESC,
  MA_PCT_IND AS MA_PCT_IND,
  ORIG_MA_AMT AS ORIG_MA_AMT,
  UPDATE_DT AS UPDATE_DT,
  LOAD_DT AS LOAD_DT1,
  INS_UPD_FLAG AS INS_UPD_DEL_FLAG,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  UNI_NEW_ORIG_11""")

df_12.createOrReplaceTempView("EXP_INS_UPD_12")

# COMMAND ----------
# DBTITLE 1, UPD_STRATEGY_13


df_13 = spark.sql("""SELECT
  MA_EVENT_ID AS MA_EVENT_ID,
  START_DT AS START_DT,
  END_DT AS END_DT,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  FISCAL_MO AS FISCAL_MO,
  MA_EVENT_DESC AS MA_EVENT_DESC,
  MA_PCT_IND AS MA_PCT_IND,
  NEW_MA_AMT AS NEW_MA_AMT,
  UPDATE_DT AS UPDATE_DT,
  LOAD_DT AS LOAD_DT,
  INS_UPD_FLAG AS INS_UPD_FLAG,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id,
  IFF(
    INS_UPD_FLAG = 'I',
    'DD_INSERT',
    IFF(INS_UPD_FLAG = 'U', 'DD_UPDATE', 'DD_REJECT')
  ) AS UPDATE_STRATEGY_FLAG
FROM
  UNI_NEW_ORIG_11""")

df_13.createOrReplaceTempView("UPD_STRATEGY_13")

# COMMAND ----------
# DBTITLE 1, MA_EVENT


spark.sql("""MERGE INTO MA_EVENT AS TARGET
USING
  UPD_STRATEGY_13 AS SOURCE ON TARGET.MA_EVENT_ID = SOURCE.MA_EVENT_ID
  WHEN MATCHED
  AND SOURCE.UPDATE_STRATEGY_FLAG = "DD_UPDATE" THEN
UPDATE
SET
  TARGET.MA_EVENT_ID = SOURCE.MA_EVENT_ID,
  TARGET.START_DT = SOURCE.START_DT,
  TARGET.END_DT = SOURCE.END_DT,
  TARGET.MA_EVENT_TYPE_ID = SOURCE.MA_EVENT_TYPE_ID,
  TARGET.MA_EVENT_SOURCE_ID = SOURCE.MA_EVENT_SOURCE_ID,
  TARGET.FISCAL_MO = SOURCE.FISCAL_MO,
  TARGET.MA_EVENT_DESC = SOURCE.MA_EVENT_DESC,
  TARGET.MA_PCT_IND = SOURCE.MA_PCT_IND,
  TARGET.MA_AMT = SOURCE.NEW_MA_AMT,
  TARGET.UPDATE_DT = SOURCE.UPDATE_DT,
  TARGET.LOAD_DT = SOURCE.LOAD_DT
  WHEN MATCHED
  AND SOURCE.UPDATE_STRATEGY_FLAG = "DD_DELETE"
  AND TARGET.START_DT = SOURCE.START_DT
  AND TARGET.END_DT = SOURCE.END_DT
  AND TARGET.MA_EVENT_TYPE_ID = SOURCE.MA_EVENT_TYPE_ID
  AND TARGET.MA_EVENT_SOURCE_ID = SOURCE.MA_EVENT_SOURCE_ID
  AND TARGET.FISCAL_MO = SOURCE.FISCAL_MO
  AND TARGET.MA_EVENT_DESC = SOURCE.MA_EVENT_DESC
  AND TARGET.MA_PCT_IND = SOURCE.MA_PCT_IND
  AND TARGET.MA_AMT = SOURCE.NEW_MA_AMT
  AND TARGET.UPDATE_DT = SOURCE.UPDATE_DT
  AND TARGET.LOAD_DT = SOURCE.LOAD_DT THEN DELETE
  WHEN NOT MATCHED
  AND SOURCE.UPDATE_STRATEGY_FLAG = "DD_INSERT" THEN
INSERT
  (
    TARGET.MA_EVENT_ID,
    TARGET.START_DT,
    TARGET.END_DT,
    TARGET.MA_EVENT_TYPE_ID,
    TARGET.MA_EVENT_SOURCE_ID,
    TARGET.FISCAL_MO,
    TARGET.MA_EVENT_DESC,
    TARGET.MA_PCT_IND,
    TARGET.MA_AMT,
    TARGET.UPDATE_DT,
    TARGET.LOAD_DT
  )
VALUES
  (
    SOURCE.MA_EVENT_ID,
    SOURCE.START_DT,
    SOURCE.END_DT,
    SOURCE.MA_EVENT_TYPE_ID,
    SOURCE.MA_EVENT_SOURCE_ID,
    SOURCE.FISCAL_MO,
    SOURCE.MA_EVENT_DESC,
    SOURCE.MA_PCT_IND,
    SOURCE.NEW_MA_AMT,
    SOURCE.UPDATE_DT,
    SOURCE.LOAD_DT
  )""")

# COMMAND ----------
# DBTITLE 1, MA_EVENT_RESTATE_HIST


spark.sql("""INSERT INTO
  MA_EVENT_RESTATE_HIST
SELECT
  LOAD_DT AS LOAD_DT,
  LOAD_DT AS LOAD_DT,
  LOAD_DT AS LOAD_DT,
  LOAD_DT AS LOAD_DT,
  MA_EVENT_ID AS MA_EVENT_ID,
  MA_EVENT_ID AS MA_EVENT_ID,
  MA_EVENT_ID AS MA_EVENT_ID,
  MA_EVENT_ID AS MA_EVENT_ID,
  NULL AS OFFER_ID,
  NULL AS SAP_DEPT_ID,
  PRODUCT_ID AS PRODUCT_ID,
  NULL AS COUNTRY_CD,
  START_DT AS START_DT,
  START_DT AS START_DT,
  START_DT AS START_DT,
  START_DT AS START_DT,
  END_DT AS END_DT,
  END_DT AS END_DT,
  END_DT AS END_DT,
  END_DT AS END_DT,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  NULL AS LOCATION_ID,
  NULL AS MOVEMENT_ID,
  NULL AS VALUATION_CLASS_CD,
  NULL AS GL_ACCT_NBR,
  NULL AS LOCATION_TYPE_ID,
  ROYALTY_BRAND_ID AS ROYALTY_BRAND_ID,
  BRAND_CD AS BRAND_CD,
  MA_FORMULA_CD AS MA_FORMULA_CD,
  FISCAL_MO AS FISCAL_MO,
  FISCAL_MO AS FISCAL_MO,
  FISCAL_MO AS FISCAL_MO,
  NULL AS SAP_CATEGORY_ID,
  FROM_LOCATION_ID AS FROM_LOCATION_ID,
  NULL AS SOURCE_VENDOR_ID,
  NULL AS COMPANY_ID,
  MA_EVENT_DESC AS MA_EVENT_DESC,
  MA_EVENT_DESC AS MA_EVENT_DESC,
  MA_EVENT_DESC AS MA_EVENT_DESC,
  MA_EVENT_DESC AS MA_EVENT_DESC,
  NULL AS EM_VENDOR_FUNDING_ID,
  NULL AS EM_COMMENT,
  NULL AS EM_BILL_ALT_VENDOR_FLAG,
  NULL AS EM_ALT_VENDOR_ID,
  NULL AS EM_ALT_VENDOR_NAME,
  NULL AS EM_ALT_VENDOR_COUNTRY_CD,
  NULL AS EM_VENDOR_ID,
  NULL AS EM_VENDOR_NAME,
  NULL AS EM_VENDOR_COUNTRY_CD,
  NULL AS VENDOR_NAME_TXT,
  MA_PCT_IND AS MA_PCT_IND,
  MA_PCT_IND AS MA_PCT_IND,
  MA_PCT_IND AS MA_PCT_IND,
  ORIG_MA_AMT AS MA_AMT,
  MA_AMT AS MA_AMT,
  MA_AMT AS MA_AMT,
  ORIG_MA_AMT AS MA_AMT,
  MA_MAX_AMT AS MA_MAX_AMT,
  INS_UPD_DEL_FLAG AS INS_UPD_DEL_FLAG,
  INS_UPD_DEL_FLAG AS INS_UPD_DEL_FLAG,
  o_LOAD_FLG AS INS_UPD_DEL_FLAG,
  INS_UPD_DEL_FLAG AS INS_UPD_DEL_FLAG
FROM
  EXP_INS_UPD_12""")