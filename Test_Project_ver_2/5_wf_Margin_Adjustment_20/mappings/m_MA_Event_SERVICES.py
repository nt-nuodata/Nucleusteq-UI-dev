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
# DBTITLE 1, Shortcut_to_SERVICES_MARGIN_RATE_1


df_1 = spark.sql("""SELECT
  WEEK_DT AS WEEK_DT,
  LOCATION_ID AS LOCATION_ID,
  SAP_DEPT_ID AS SAP_DEPT_ID,
  MARGIN_RATE AS MARGIN_RATE,
  UPDATE_TSTMP AS UPDATE_TSTMP,
  LOAD_TSTMP AS LOAD_TSTMP
FROM
  SERVICES_MARGIN_RATE""")

df_1.createOrReplaceTempView("Shortcut_to_SERVICES_MARGIN_RATE_1")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_SERVICES_MARGIN_RATE1_2


df_2 = spark.sql("""SELECT
  WEEK_DT AS WEEK_DT,
  LOCATION_ID AS LOCATION_ID,
  SAP_DEPT_ID AS SAP_DEPT_ID,
  MARGIN_RATE AS MARGIN_RATE,
  UPDATE_TSTMP AS UPDATE_TSTMP,
  LOAD_TSTMP AS LOAD_TSTMP
FROM
  SERVICES_MARGIN_RATE""")

df_2.createOrReplaceTempView("Shortcut_to_SERVICES_MARGIN_RATE1_2")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_MA_EVENT1_3


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

df_3.createOrReplaceTempView("Shortcut_to_MA_EVENT1_3")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_MA_EVENT11_4


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

df_4.createOrReplaceTempView("Shortcut_to_MA_EVENT11_4")

# COMMAND ----------
# DBTITLE 1, Shortcut_To_DAYS_5


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

df_5.createOrReplaceTempView("Shortcut_To_DAYS_5")

# COMMAND ----------
# DBTITLE 1, Shortcut_To_DAYS1_6


df_6 = spark.sql("""SELECT
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

df_6.createOrReplaceTempView("Shortcut_To_DAYS1_6")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_SAP_DEPT_7


df_7 = spark.sql("""SELECT
  SAP_DEPT_ID AS SAP_DEPT_ID,
  SAP_DEPT_DESC AS SAP_DEPT_DESC,
  SAP_DIVISION_ID AS SAP_DIVISION_ID,
  MERCH_DIVISIONAL_ID AS MERCH_DIVISIONAL_ID,
  BUYER_ID AS BUYER_ID
FROM
  SAP_DEPT""")

df_7.createOrReplaceTempView("Shortcut_to_SAP_DEPT_7")

# COMMAND ----------
# DBTITLE 1, SQ_Shortcut_to_SERVICES_MARGIN_RATE_Ins_8


df_8 = spark.sql("""SELECT
  NULL AS OFFER_ID,
  S.SAP_DEPT_ID AS SAP_DEPT_ID,
  NULL AS PRODUCT_ID,
  NULL AS COUNTRY_CD,
  W.START_DT AS START_DT,
  W.END_DT AS END_DT,
  30 AS MA_EVENT_TYPE_ID,
  7 AS MA_EVENT_SOURCE_ID,
  S.LOCATION_ID AS LOCATION_ID,
  'Services Margin - ' || TRIM(SAP_DEPT_DESC) || ' - Week=' || TO_CHAR(S.WEEK_DT, 'MM/DD/YYYY') || ' - Location ID=' || S.LOCATION_ID AS MA_EVENT_DESC,
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
  1 AS MA_PCT_IND,
  S.MARGIN_RATE * 100 * -1 AS MA_AMT,
  NULL AS MA_MAX_AMT,
  'I' AS LOAD_FLAG,
  monotonically_increasing_id() AS Monotonically_Increasing_Id
FROM
  Shortcut_to_SERVICES_MARGIN_RATE_1 S
  JOIN Shortcut_to_SAP_DEPT_7 D ON S.SAP_DEPT_ID = D.SAP_DEPT_ID
  JOIN (
    SELECT
      WEEK_DT,
      MIN(DAY_DT) AS START_DT,
      MAX(DAY_DT) AS END_DT
    FROM
      Shortcut_To_DAYS_5
    WHERE
      CAL_YR >= 2014
    GROUP BY
      WEEK_DT
  ) W ON S.WEEK_DT = W.WEEK_DT
  LEFT JOIN Shortcut_to_MA_EVENT1_3 M ON S.LOCATION_ID = M.LOCATION_ID
  AND S.SAP_DEPT_ID = M.SAP_DEPT_ID
  AND W.START_DT = M.START_DT
  AND W.END_DT = M.END_DT
  AND M.MA_EVENT_TYPE_ID = 30
  AND M.MA_EVENT_SOURCE_ID = 7
WHERE
  S.UPDATE_TSTMP > CURRENT_DATE - 2
  AND M.MA_EVENT_ID IS NULL""")

df_8.createOrReplaceTempView("SQ_Shortcut_to_SERVICES_MARGIN_RATE_Ins_8")

# COMMAND ----------
# DBTITLE 1, EXP_INS_UPD_9


df_9 = spark.sql("""SELECT
  NEXTVAL AS MA_EVENT_ID,
  OFFER_ID AS OFFER_ID,
  SAP_DEPT_ID AS SAP_DEPT_ID,
  PRODUCT_ID AS PRODUCT_ID,
  COUNTRY_CD AS COUNTRY_CD,
  START_DT AS START_DT,
  END_DT AS END_DT,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  LOCATION_ID AS LOCATION_ID,
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
  now() AS UPDATE_DT,
  now() AS LOAD_DT,
  LOAD_FLAG AS LOAD_FLAG,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  SQ_Shortcut_to_SERVICES_MARGIN_RATE_Ins_8""")

df_9.createOrReplaceTempView("EXP_INS_UPD_9")

spark.sql("""UPDATE SEQ_MA_EVENT_ID SET CURRVAL = (SELECT MAX(MA_EVENT_ID) FROM EXP_INS_UPD_9) , NEXTVAL = (SELECT MAX(MA_EVENT_ID) FROM EXP_INS_UPD_9) + (SELECT Increment_By FROM EXP_INS_UPD_9)""")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_SAP_DEPT1_10


df_10 = spark.sql("""SELECT
  SAP_DEPT_ID AS SAP_DEPT_ID,
  SAP_DEPT_DESC AS SAP_DEPT_DESC,
  SAP_DIVISION_ID AS SAP_DIVISION_ID,
  MERCH_DIVISIONAL_ID AS MERCH_DIVISIONAL_ID,
  BUYER_ID AS BUYER_ID
FROM
  SAP_DEPT""")

df_10.createOrReplaceTempView("Shortcut_to_SAP_DEPT1_10")

# COMMAND ----------
# DBTITLE 1, SQ_Shortcut_to_SERVICES_MARGIN_RATE_Upd_11


df_11 = spark.sql("""SELECT
  M.MA_EVENT_ID AS MA_EVENT_ID,
  NULL AS OFFER_ID,
  M.SAP_DEPT_ID AS SAP_DEPT_ID,
  NULL AS PRODUCT_ID,
  NULL AS COUNTRY_CD,
  M.START_DT AS START_DT,
  M.END_DT AS END_DT,
  M.MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  M.MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  M.LOCATION_ID AS LOCATION_ID,
  M.MA_EVENT_DESC AS MA_EVENT_DESC,
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
  M.MA_PCT_IND AS MA_PCT_IND,
  S.MARGIN_RATE * 100 * -1 AS MA_AMT,
  NULL AS MA_MAX_AMT,
  M.LOAD_DT AS LOAD_DT,
  'R' AS LOAD_FLAG,
  monotonically_increasing_id() AS Monotonically_Increasing_Id
FROM
  Shortcut_to_SERVICES_MARGIN_RATE1_2 S
  JOIN Shortcut_to_SAP_DEPT1_10 D ON S.SAP_DEPT_ID = D.SAP_DEPT_ID
  JOIN (
    SELECT
      WEEK_DT,
      MIN(DAY_DT) AS START_DT,
      MAX(DAY_DT) AS END_DT
    FROM
      Shortcut_To_DAYS1_6
    WHERE
      CAL_YR >= 2014
    GROUP BY
      WEEK_DT
  ) W ON S.WEEK_DT = W.WEEK_DT
  JOIN Shortcut_to_MA_EVENT11_4 M ON S.LOCATION_ID = M.LOCATION_ID
  AND S.SAP_DEPT_ID = M.SAP_DEPT_ID
  AND W.START_DT = M.START_DT
  AND W.END_DT = M.END_DT
  AND M.MA_EVENT_TYPE_ID = 30
  AND M.MA_EVENT_SOURCE_ID = 7
WHERE
  S.UPDATE_TSTMP > CURRENT_DATE - 2
  AND M.MA_AMT <> S.MARGIN_RATE * 100 * -1""")

df_11.createOrReplaceTempView("SQ_Shortcut_to_SERVICES_MARGIN_RATE_Upd_11")

# COMMAND ----------
# DBTITLE 1, EXP_UPD_12


df_12 = spark.sql("""SELECT
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
  now() AS UPDATE_DT,
  LOAD_DT AS LOAD_DT,
  LOAD_FLAG AS LOAD_FLAG,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  SQ_Shortcut_to_SERVICES_MARGIN_RATE_Upd_11""")

df_12.createOrReplaceTempView("EXP_UPD_12")

# COMMAND ----------
# DBTITLE 1, UNI_SERVICES_MARGIN_RATE_13


df_13 = spark.sql("""SELECT
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
  LOAD_DT AS LOAD_DT,
  LOAD_FLAG AS LOAD_FLAG,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  EXP_UPD_12
UNION ALL
SELECT
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
  LOAD_DT AS LOAD_DT,
  LOAD_FLAG AS LOAD_FLAG,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  EXP_INS_UPD_9""")

df_13.createOrReplaceTempView("UNI_SERVICES_MARGIN_RATE_13")

# COMMAND ----------
# DBTITLE 1, UPD_STRATEGY_14


df_14 = spark.sql("""SELECT
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
  LOAD_DT AS LOAD_DT,
  LOAD_FLAG AS LOAD_FLAG,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id,
  IFF(LOAD_FLAG = 'I', 'DD_INSERT', 'DD_UPDATE') AS UPDATE_STRATEGY_FLAG
FROM
  UNI_SERVICES_MARGIN_RATE_13""")

df_14.createOrReplaceTempView("UPD_STRATEGY_14")

# COMMAND ----------
# DBTITLE 1, EXP_INS_15


df_15 = spark.sql("""SELECT
  TRUNC(now()) AS LOAD_DT,
  MA_EVENT_ID AS MA_EVENT_ID,
  PRODUCT_ID AS PRODUCT_ID,
  COUNTRY_CD AS COUNTRY_CD,
  START_DT AS START_DT,
  END_DT AS END_DT,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  LOCATION_ID AS LOCATION_ID,
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
  MA_AMT AS MA_AMT,
  MA_MAX_AMT AS MA_MAX_AMT,
  IFF(LOAD_FLAG = 'R', 'U', LOAD_FLAG) AS LOAD_FLAG,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  UNI_SERVICES_MARGIN_RATE_13""")

df_15.createOrReplaceTempView("EXP_INS_15")

# COMMAND ----------
# DBTITLE 1, MA_EVENT_RESTATE_HIST


spark.sql("""INSERT INTO
  MA_EVENT_RESTATE_HIST
SELECT
  LOAD_DT AS LOAD_DT,
  LOAD_DT AS LOAD_DT,
  LOAD_DT AS LOAD_DT,
  LOAD_DT AS LOAD_DT,
  LOAD_DT AS LOAD_DT,
  LOAD_DT AS LOAD_DT,
  MA_EVENT_ID AS MA_EVENT_ID,
  MA_EVENT_ID AS MA_EVENT_ID,
  MA_EVENT_ID AS MA_EVENT_ID,
  MA_EVENT_ID AS MA_EVENT_ID,
  MA_EVENT_ID AS MA_EVENT_ID,
  MA_EVENT_ID AS MA_EVENT_ID,
  NULL AS OFFER_ID,
  NULL AS SAP_DEPT_ID,
  PRODUCT_ID AS PRODUCT_ID,
  PRODUCT_ID AS PRODUCT_ID,
  PRODUCT_ID AS PRODUCT_ID,
  COUNTRY_CD AS COUNTRY_CD,
  COUNTRY_CD AS COUNTRY_CD,
  START_DT AS START_DT,
  START_DT AS START_DT,
  START_DT AS START_DT,
  START_DT AS START_DT,
  START_DT AS START_DT,
  START_DT AS START_DT,
  END_DT AS END_DT,
  END_DT AS END_DT,
  END_DT AS END_DT,
  END_DT AS END_DT,
  END_DT AS END_DT,
  END_DT AS END_DT,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  LOCATION_ID AS LOCATION_ID,
  LOCATION_ID AS LOCATION_ID,
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
  MA_EVENT_DESC AS MA_EVENT_DESC,
  MA_EVENT_DESC AS MA_EVENT_DESC,
  EM_VENDOR_FUNDING_ID AS EM_VENDOR_FUNDING_ID,
  EM_VENDOR_FUNDING_ID AS EM_VENDOR_FUNDING_ID,
  EM_COMMENT AS EM_COMMENT,
  EM_COMMENT AS EM_COMMENT,
  EM_BILL_ALT_VENDOR_FLAG AS EM_BILL_ALT_VENDOR_FLAG,
  EM_BILL_ALT_VENDOR_FLAG AS EM_BILL_ALT_VENDOR_FLAG,
  EM_ALT_VENDOR_ID AS EM_ALT_VENDOR_ID,
  EM_ALT_VENDOR_ID AS EM_ALT_VENDOR_ID,
  EM_ALT_VENDOR_NAME AS EM_ALT_VENDOR_NAME,
  EM_ALT_VENDOR_NAME AS EM_ALT_VENDOR_NAME,
  EM_ALT_VENDOR_COUNTRY_CD AS EM_ALT_VENDOR_COUNTRY_CD,
  EM_ALT_VENDOR_COUNTRY_CD AS EM_ALT_VENDOR_COUNTRY_CD,
  EM_VENDOR_ID AS EM_VENDOR_ID,
  EM_VENDOR_ID AS EM_VENDOR_ID,
  EM_VENDOR_NAME AS EM_VENDOR_NAME,
  EM_VENDOR_NAME AS EM_VENDOR_NAME,
  EM_VENDOR_COUNTRY_CD AS EM_VENDOR_COUNTRY_CD,
  EM_VENDOR_COUNTRY_CD AS EM_VENDOR_COUNTRY_CD,
  NULL AS VENDOR_NAME_TXT,
  MA_PCT_IND AS MA_PCT_IND,
  MA_PCT_IND AS MA_PCT_IND,
  MA_PCT_IND AS MA_PCT_IND,
  ORIG_MA_AMT AS MA_AMT,
  MA_AMT AS MA_AMT,
  MA_AMT AS MA_AMT,
  ORIG_MA_AMT AS MA_AMT,
  MA_AMT AS MA_AMT,
  MA_AMT AS MA_AMT,
  MA_MAX_AMT AS MA_MAX_AMT,
  MA_MAX_AMT AS MA_MAX_AMT,
  MA_MAX_AMT AS MA_MAX_AMT,
  INS_UPD_DEL_FLAG AS INS_UPD_DEL_FLAG,
  INS_UPD_DEL_FLAG AS INS_UPD_DEL_FLAG,
  o_LOAD_FLG AS INS_UPD_DEL_FLAG,
  INS_UPD_DEL_FLAG AS INS_UPD_DEL_FLAG,
  INS_UPD_DEL_FLAG_out AS INS_UPD_DEL_FLAG,
  LOAD_FLAG AS INS_UPD_DEL_FLAG
FROM
  EXP_INS_15""")

# COMMAND ----------
# DBTITLE 1, MA_EVENT


spark.sql("""MERGE INTO MA_EVENT AS TARGET
USING
  UPD_STRATEGY_14 AS SOURCE ON TARGET.MA_EVENT_ID = SOURCE.MA_EVENT_ID
  WHEN MATCHED
  AND SOURCE.UPDATE_STRATEGY_FLAG = "DD_UPDATE" THEN
UPDATE
SET
  TARGET.MA_EVENT_ID = SOURCE.MA_EVENT_ID,
  TARGET.OFFER_ID = SOURCE.OFFER_ID,
  TARGET.SAP_DEPT_ID = SOURCE.SAP_DEPT_ID,
  TARGET.PRODUCT_ID = SOURCE.PRODUCT_ID,
  TARGET.COUNTRY_CD = SOURCE.COUNTRY_CD,
  TARGET.START_DT = SOURCE.START_DT,
  TARGET.END_DT = SOURCE.END_DT,
  TARGET.MA_EVENT_TYPE_ID = SOURCE.MA_EVENT_TYPE_ID,
  TARGET.MA_EVENT_SOURCE_ID = SOURCE.MA_EVENT_SOURCE_ID,
  TARGET.LOCATION_ID = SOURCE.LOCATION_ID,
  TARGET.MA_EVENT_DESC = SOURCE.MA_EVENT_DESC,
  TARGET.EM_VENDOR_FUNDING_ID = SOURCE.EM_VENDOR_FUNDING_ID,
  TARGET.EM_COMMENT = SOURCE.EM_COMMENT,
  TARGET.EM_BILL_ALT_VENDOR_FLAG = SOURCE.EM_BILL_ALT_VENDOR_FLAG,
  TARGET.EM_ALT_VENDOR_ID = SOURCE.EM_ALT_VENDOR_ID,
  TARGET.EM_ALT_VENDOR_NAME = SOURCE.EM_ALT_VENDOR_NAME,
  TARGET.EM_ALT_VENDOR_COUNTRY_CD = SOURCE.EM_ALT_VENDOR_COUNTRY_CD,
  TARGET.EM_VENDOR_ID = SOURCE.EM_VENDOR_ID,
  TARGET.EM_VENDOR_NAME = SOURCE.EM_VENDOR_NAME,
  TARGET.EM_VENDOR_COUNTRY_CD = SOURCE.EM_VENDOR_COUNTRY_CD,
  TARGET.VENDOR_NAME_TXT = SOURCE.VENDOR_NAME_TXT,
  TARGET.MA_PCT_IND = SOURCE.MA_PCT_IND,
  TARGET.MA_AMT = SOURCE.MA_AMT,
  TARGET.MA_MAX_AMT = SOURCE.MA_MAX_AMT,
  TARGET.UPDATE_DT = SOURCE.UPDATE_DT,
  TARGET.LOAD_DT = SOURCE.LOAD_DT
  WHEN MATCHED
  AND SOURCE.UPDATE_STRATEGY_FLAG = "DD_DELETE"
  AND TARGET.OFFER_ID = SOURCE.OFFER_ID
  AND TARGET.SAP_DEPT_ID = SOURCE.SAP_DEPT_ID
  AND TARGET.PRODUCT_ID = SOURCE.PRODUCT_ID
  AND TARGET.COUNTRY_CD = SOURCE.COUNTRY_CD
  AND TARGET.START_DT = SOURCE.START_DT
  AND TARGET.END_DT = SOURCE.END_DT
  AND TARGET.MA_EVENT_TYPE_ID = SOURCE.MA_EVENT_TYPE_ID
  AND TARGET.MA_EVENT_SOURCE_ID = SOURCE.MA_EVENT_SOURCE_ID
  AND TARGET.LOCATION_ID = SOURCE.LOCATION_ID
  AND TARGET.MA_EVENT_DESC = SOURCE.MA_EVENT_DESC
  AND TARGET.EM_VENDOR_FUNDING_ID = SOURCE.EM_VENDOR_FUNDING_ID
  AND TARGET.EM_COMMENT = SOURCE.EM_COMMENT
  AND TARGET.EM_BILL_ALT_VENDOR_FLAG = SOURCE.EM_BILL_ALT_VENDOR_FLAG
  AND TARGET.EM_ALT_VENDOR_ID = SOURCE.EM_ALT_VENDOR_ID
  AND TARGET.EM_ALT_VENDOR_NAME = SOURCE.EM_ALT_VENDOR_NAME
  AND TARGET.EM_ALT_VENDOR_COUNTRY_CD = SOURCE.EM_ALT_VENDOR_COUNTRY_CD
  AND TARGET.EM_VENDOR_ID = SOURCE.EM_VENDOR_ID
  AND TARGET.EM_VENDOR_NAME = SOURCE.EM_VENDOR_NAME
  AND TARGET.EM_VENDOR_COUNTRY_CD = SOURCE.EM_VENDOR_COUNTRY_CD
  AND TARGET.VENDOR_NAME_TXT = SOURCE.VENDOR_NAME_TXT
  AND TARGET.MA_PCT_IND = SOURCE.MA_PCT_IND
  AND TARGET.MA_AMT = SOURCE.MA_AMT
  AND TARGET.MA_MAX_AMT = SOURCE.MA_MAX_AMT
  AND TARGET.UPDATE_DT = SOURCE.UPDATE_DT
  AND TARGET.LOAD_DT = SOURCE.LOAD_DT THEN DELETE
  WHEN NOT MATCHED
  AND SOURCE.UPDATE_STRATEGY_FLAG = "DD_INSERT" THEN
INSERT
  (
    TARGET.MA_EVENT_ID,
    TARGET.OFFER_ID,
    TARGET.SAP_DEPT_ID,
    TARGET.PRODUCT_ID,
    TARGET.COUNTRY_CD,
    TARGET.START_DT,
    TARGET.END_DT,
    TARGET.MA_EVENT_TYPE_ID,
    TARGET.MA_EVENT_SOURCE_ID,
    TARGET.LOCATION_ID,
    TARGET.MA_EVENT_DESC,
    TARGET.EM_VENDOR_FUNDING_ID,
    TARGET.EM_COMMENT,
    TARGET.EM_BILL_ALT_VENDOR_FLAG,
    TARGET.EM_ALT_VENDOR_ID,
    TARGET.EM_ALT_VENDOR_NAME,
    TARGET.EM_ALT_VENDOR_COUNTRY_CD,
    TARGET.EM_VENDOR_ID,
    TARGET.EM_VENDOR_NAME,
    TARGET.EM_VENDOR_COUNTRY_CD,
    TARGET.VENDOR_NAME_TXT,
    TARGET.MA_PCT_IND,
    TARGET.MA_AMT,
    TARGET.MA_MAX_AMT,
    TARGET.UPDATE_DT,
    TARGET.LOAD_DT
  )
VALUES
  (
    SOURCE.MA_EVENT_ID,
    SOURCE.OFFER_ID,
    SOURCE.SAP_DEPT_ID,
    SOURCE.PRODUCT_ID,
    SOURCE.COUNTRY_CD,
    SOURCE.START_DT,
    SOURCE.END_DT,
    SOURCE.MA_EVENT_TYPE_ID,
    SOURCE.MA_EVENT_SOURCE_ID,
    SOURCE.LOCATION_ID,
    SOURCE.MA_EVENT_DESC,
    SOURCE.EM_VENDOR_FUNDING_ID,
    SOURCE.EM_COMMENT,
    SOURCE.EM_BILL_ALT_VENDOR_FLAG,
    SOURCE.EM_ALT_VENDOR_ID,
    SOURCE.EM_ALT_VENDOR_NAME,
    SOURCE.EM_ALT_VENDOR_COUNTRY_CD,
    SOURCE.EM_VENDOR_ID,
    SOURCE.EM_VENDOR_NAME,
    SOURCE.EM_VENDOR_COUNTRY_CD,
    SOURCE.VENDOR_NAME_TXT,
    SOURCE.MA_PCT_IND,
    SOURCE.MA_AMT,
    SOURCE.MA_MAX_AMT,
    SOURCE.UPDATE_DT,
    SOURCE.LOAD_DT
  )""")