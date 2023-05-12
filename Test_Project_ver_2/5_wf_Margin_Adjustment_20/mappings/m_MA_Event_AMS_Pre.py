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
# DBTITLE 1, Shortcut_to_AMS_OFFER_CHARGEBACK_1


df_1 = spark.sql("""SELECT
  OFFER_CHARGEBACK_ID AS OFFER_CHARGEBACK_ID,
  OFFER_CHARGEBACK_DESC AS OFFER_CHARGEBACK_DESC,
  ITEM_DISC_IND AS ITEM_DISC_IND,
  POS_DISCOUNT_TYPE_CD AS POS_DISCOUNT_TYPE_CD,
  POS_DISCOUNT_TYPE_ID AS POS_DISCOUNT_TYPE_ID,
  UPDATE_TSTMP AS UPDATE_TSTMP,
  LOAD_TSTMP AS LOAD_TSTMP
FROM
  AMS_OFFER_CHARGEBACK""")

df_1.createOrReplaceTempView("Shortcut_to_AMS_OFFER_CHARGEBACK_1")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_AMS_OFFER_CHARGEBACK1_2


df_2 = spark.sql("""SELECT
  OFFER_CHARGEBACK_ID AS OFFER_CHARGEBACK_ID,
  OFFER_CHARGEBACK_DESC AS OFFER_CHARGEBACK_DESC,
  ITEM_DISC_IND AS ITEM_DISC_IND,
  POS_DISCOUNT_TYPE_CD AS POS_DISCOUNT_TYPE_CD,
  POS_DISCOUNT_TYPE_ID AS POS_DISCOUNT_TYPE_ID,
  UPDATE_TSTMP AS UPDATE_TSTMP,
  LOAD_TSTMP AS LOAD_TSTMP
FROM
  AMS_OFFER_CHARGEBACK""")

df_2.createOrReplaceTempView("Shortcut_to_AMS_OFFER_CHARGEBACK1_2")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_AMS_OFFER_DISCOUNT_3


df_3 = spark.sql("""SELECT
  OFFER_ID AS OFFER_ID,
  TIER_ID AS TIER_ID,
  DISCOUNT_TYPE_ID AS DISCOUNT_TYPE_ID,
  OFFER_CHARGEBACK_ID AS OFFER_CHARGEBACK_ID,
  DISCOUNT_AMT_TYPE_ID AS DISCOUNT_AMT_TYPE_ID,
  DISCOUNT_AMT AS DISCOUNT_AMT,
  DISCOUNT_LIMIT_QTY AS DISCOUNT_LIMIT_QTY,
  DISCOUNT_LIMIT_WEIGHT AS DISCOUNT_LIMIT_WEIGHT,
  DISCOUNT_LIMIT_AMT AS DISCOUNT_LIMIT_AMT,
  DISCOUNT_RECEIPT_TXT AS DISCOUNT_RECEIPT_TXT,
  DISCOUNT_UP_TO_AMT AS DISCOUNT_UP_TO_AMT,
  ALLOW_MARKUP_IND AS ALLOW_MARKUP_IND,
  FLEX_NEGATIVE_IND AS FLEX_NEGATIVE_IND,
  PRODUCT_GROUP_ID AS PRODUCT_GROUP_ID,
  EXCLUDED_PRODUCT_GROUP_ID AS EXCLUDED_PRODUCT_GROUP_ID,
  UPDATE_TSTMP AS UPDATE_TSTMP,
  LOAD_TSTMP AS LOAD_TSTMP
FROM
  AMS_OFFER_DISCOUNT""")

df_3.createOrReplaceTempView("Shortcut_to_AMS_OFFER_DISCOUNT_3")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_AMS_OFFER_4


df_4 = spark.sql("""SELECT
  OFFER_ID AS OFFER_ID,
  IS_TEMPLATE_IND AS IS_TEMPLATE_IND,
  FROM_TEMPLATE_IND AS FROM_TEMPLATE_IND,
  OFFER_NAME AS OFFER_NAME,
  OFFER_DESC AS OFFER_DESC,
  OFFER_CATEGORY_ID AS OFFER_CATEGORY_ID,
  OFFER_PRIORITY AS OFFER_PRIORITY,
  OFFER_START_DT AS OFFER_START_DT,
  OFFER_END_DT AS OFFER_END_DT,
  OFFER_LIMIT_TYPE_ID AS OFFER_LIMIT_TYPE_ID,
  OFFER_LIMIT_QTY AS OFFER_LIMIT_QTY,
  OFFER_LIMIT_PERIOD_DAYS AS OFFER_LIMIT_PERIOD_DAYS,
  SYS_CREATE_TSTMP AS SYS_CREATE_TSTMP,
  SYS_UPDATE_TSTMP AS SYS_UPDATE_TSTMP,
  DELETE_FLAG AS DELETE_FLAG,
  STATUS_FLAG AS STATUS_FLAG,
  OFFER_STATUS_ID AS OFFER_STATUS_ID,
  EMPLOYEES_ONLY_IND AS EMPLOYEES_ONLY_IND,
  EMPLOYEES_EXCLUDED_IND AS EMPLOYEES_EXCLUDED_IND,
  SEND_ISSUANCE_IND AS SEND_ISSUANCE_IND,
  VENDOR_COUPON_CD AS VENDOR_COUPON_CD,
  TIER_LEVEL_CNT AS TIER_LEVEL_CNT,
  DISC_EVAL_TYPE_ID AS DISC_EVAL_TYPE_ID,
  UPDATE_TSTMP AS UPDATE_TSTMP,
  LOAD_TSTMP AS LOAD_TSTMP
FROM
  AMS_OFFER""")

df_4.createOrReplaceTempView("Shortcut_to_AMS_OFFER_4")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_AMS_OFFER1_5


df_5 = spark.sql("""SELECT
  OFFER_ID AS OFFER_ID,
  IS_TEMPLATE_IND AS IS_TEMPLATE_IND,
  FROM_TEMPLATE_IND AS FROM_TEMPLATE_IND,
  OFFER_NAME AS OFFER_NAME,
  OFFER_DESC AS OFFER_DESC,
  OFFER_CATEGORY_ID AS OFFER_CATEGORY_ID,
  OFFER_PRIORITY AS OFFER_PRIORITY,
  OFFER_START_DT AS OFFER_START_DT,
  OFFER_END_DT AS OFFER_END_DT,
  OFFER_LIMIT_TYPE_ID AS OFFER_LIMIT_TYPE_ID,
  OFFER_LIMIT_QTY AS OFFER_LIMIT_QTY,
  OFFER_LIMIT_PERIOD_DAYS AS OFFER_LIMIT_PERIOD_DAYS,
  SYS_CREATE_TSTMP AS SYS_CREATE_TSTMP,
  SYS_UPDATE_TSTMP AS SYS_UPDATE_TSTMP,
  DELETE_FLAG AS DELETE_FLAG,
  STATUS_FLAG AS STATUS_FLAG,
  OFFER_STATUS_ID AS OFFER_STATUS_ID,
  EMPLOYEES_ONLY_IND AS EMPLOYEES_ONLY_IND,
  EMPLOYEES_EXCLUDED_IND AS EMPLOYEES_EXCLUDED_IND,
  SEND_ISSUANCE_IND AS SEND_ISSUANCE_IND,
  VENDOR_COUPON_CD AS VENDOR_COUPON_CD,
  TIER_LEVEL_CNT AS TIER_LEVEL_CNT,
  DISC_EVAL_TYPE_ID AS DISC_EVAL_TYPE_ID,
  UPDATE_TSTMP AS UPDATE_TSTMP,
  LOAD_TSTMP AS LOAD_TSTMP
FROM
  AMS_OFFER""")

df_5.createOrReplaceTempView("Shortcut_to_AMS_OFFER1_5")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_AMS_OFFER_SUBMISSION_6


df_6 = spark.sql("""SELECT
  AMS_OFFER_SUBMISSION_ID AS AMS_OFFER_SUBMISSION_ID,
  BUSINESS_OWNER AS BUSINESS_OWNER,
  APPROVER AS APPROVER,
  OFFER_DEPT_AND_DIV AS OFFER_DEPT_AND_DIV,
  OFFER_NAME AS OFFER_NAME,
  OFFER_DESC AS OFFER_DESC,
  DEFERRED_REVENUE AS DEFERRED_REVENUE,
  LEGACY_PB_OFFER_IND AS LEGACY_PB_OFFER_IND,
  VENDOR_FUNDED_TYPE AS VENDOR_FUNDED_TYPE,
  VENDOR_FUNDED_VALUE AS VENDOR_FUNDED_VALUE,
  VENDOR_FUNDED_LIMIT AS VENDOR_FUNDED_LIMIT,
  MFG_VENDOR_BRAND_NAME AS MFG_VENDOR_BRAND_NAME,
  OFFER_MEDIA AS OFFER_MEDIA,
  OFFER_PATH AS OFFER_PATH,
  PLANNER_PERIOD AS PLANNER_PERIOD,
  START_DT AS START_DT,
  EXP_DT AS EXP_DT,
  OFFER_TIME_BASED_IND AS OFFER_TIME_BASED_IND,
  OFFER_TIME_DESC AS OFFER_TIME_DESC,
  US_OFFER_IND AS US_OFFER_IND,
  PR_OFFER_IND AS PR_OFFER_IND,
  CA_OFFER_IND AS CA_OFFER_IND,
  STORE_LIST AS STORE_LIST,
  CUSTOMER_GROUP AS CUSTOMER_GROUP,
  QUALIFYING_PRODUCT AS QUALIFYING_PRODUCT,
  QUALIFYING_PRODUCT_DTL AS QUALIFYING_PRODUCT_DTL,
  QUALIFYING_PRODUCT_CONDITION AS QUALIFYING_PRODUCT_CONDITION,
  BUY_SPEND_REQ AS BUY_SPEND_REQ,
  BUY_SPEND_REQ_DTL AS BUY_SPEND_REQ_DTL,
  MIN_UNIT_PRICE AS MIN_UNIT_PRICE,
  TIERED_OFFER_IND AS TIERED_OFFER_IND,
  TIERED_OFFER_DESC AS TIERED_OFFER_DESC,
  OFFER_QUALIFICATION_TIMEFRAME AS OFFER_QUALIFICATION_TIMEFRAME,
  OFFER_QUALIFICATION_TIMEFRAME_DTL AS OFFER_QUALIFICATION_TIMEFRAME_DTL,
  REWARD_PRODUCT AS REWARD_PRODUCT,
  REWARD_PRODUCT_DTL AS REWARD_PRODUCT_DTL,
  REWARD AS REWARD,
  REWARD_DTL AS REWARD_DTL,
  REWARD_LEVEL AS REWARD_LEVEL,
  REWARD_ITEM_QTY AS REWARD_ITEM_QTY,
  MAX_DISC AS MAX_DISC,
  OFFER_LIMITATION AS OFFER_LIMITATION,
  OFFER_LIMITATION_DTL AS OFFER_LIMITATION_DTL,
  MUTUALLY_EXCLUSIVE_OFFER_IND AS MUTUALLY_EXCLUSIVE_OFFER_IND,
  RECEIPT_TXT AS RECEIPT_TXT,
  ISSUANCE_MESSAGE AS ISSUANCE_MESSAGE,
  OFFER_STATUS AS OFFER_STATUS,
  UAT_TEST_STATUS AS UAT_TEST_STATUS,
  CANCELLED_IND AS CANCELLED_IND,
  SCHED_OFFER_DEPLOYMENT_DT AS SCHED_OFFER_DEPLOYMENT_DT,
  APPROVAL_DTL AS APPROVAL_DTL,
  UPCA_NBR_TXT AS UPCA_NBR_TXT,
  CATEGORY_CD_AND_NAME AS CATEGORY_CD_AND_NAME,
  AMS_OFFER_ID AS AMS_OFFER_ID,
  AMS_TEMPLATE AS AMS_TEMPLATE,
  CREATED_BY AS CREATED_BY,
  MODIFIED_BY AS MODIFIED_BY,
  UPDATE_TSTMP AS UPDATE_TSTMP,
  LOAD_TSTMP AS LOAD_TSTMP
FROM
  AMS_OFFER_SUBMISSION""")

df_6.createOrReplaceTempView("Shortcut_to_AMS_OFFER_SUBMISSION_6")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_AMS_OFFER_SUBMISSION1_7


df_7 = spark.sql("""SELECT
  AMS_OFFER_SUBMISSION_ID AS AMS_OFFER_SUBMISSION_ID,
  BUSINESS_OWNER AS BUSINESS_OWNER,
  APPROVER AS APPROVER,
  OFFER_DEPT_AND_DIV AS OFFER_DEPT_AND_DIV,
  OFFER_NAME AS OFFER_NAME,
  OFFER_DESC AS OFFER_DESC,
  DEFERRED_REVENUE AS DEFERRED_REVENUE,
  LEGACY_PB_OFFER_IND AS LEGACY_PB_OFFER_IND,
  VENDOR_FUNDED_TYPE AS VENDOR_FUNDED_TYPE,
  VENDOR_FUNDED_VALUE AS VENDOR_FUNDED_VALUE,
  VENDOR_FUNDED_LIMIT AS VENDOR_FUNDED_LIMIT,
  MFG_VENDOR_BRAND_NAME AS MFG_VENDOR_BRAND_NAME,
  OFFER_MEDIA AS OFFER_MEDIA,
  OFFER_PATH AS OFFER_PATH,
  PLANNER_PERIOD AS PLANNER_PERIOD,
  START_DT AS START_DT,
  EXP_DT AS EXP_DT,
  OFFER_TIME_BASED_IND AS OFFER_TIME_BASED_IND,
  OFFER_TIME_DESC AS OFFER_TIME_DESC,
  US_OFFER_IND AS US_OFFER_IND,
  PR_OFFER_IND AS PR_OFFER_IND,
  CA_OFFER_IND AS CA_OFFER_IND,
  STORE_LIST AS STORE_LIST,
  CUSTOMER_GROUP AS CUSTOMER_GROUP,
  QUALIFYING_PRODUCT AS QUALIFYING_PRODUCT,
  QUALIFYING_PRODUCT_DTL AS QUALIFYING_PRODUCT_DTL,
  QUALIFYING_PRODUCT_CONDITION AS QUALIFYING_PRODUCT_CONDITION,
  BUY_SPEND_REQ AS BUY_SPEND_REQ,
  BUY_SPEND_REQ_DTL AS BUY_SPEND_REQ_DTL,
  MIN_UNIT_PRICE AS MIN_UNIT_PRICE,
  TIERED_OFFER_IND AS TIERED_OFFER_IND,
  TIERED_OFFER_DESC AS TIERED_OFFER_DESC,
  OFFER_QUALIFICATION_TIMEFRAME AS OFFER_QUALIFICATION_TIMEFRAME,
  OFFER_QUALIFICATION_TIMEFRAME_DTL AS OFFER_QUALIFICATION_TIMEFRAME_DTL,
  REWARD_PRODUCT AS REWARD_PRODUCT,
  REWARD_PRODUCT_DTL AS REWARD_PRODUCT_DTL,
  REWARD AS REWARD,
  REWARD_DTL AS REWARD_DTL,
  REWARD_LEVEL AS REWARD_LEVEL,
  REWARD_ITEM_QTY AS REWARD_ITEM_QTY,
  MAX_DISC AS MAX_DISC,
  OFFER_LIMITATION AS OFFER_LIMITATION,
  OFFER_LIMITATION_DTL AS OFFER_LIMITATION_DTL,
  MUTUALLY_EXCLUSIVE_OFFER_IND AS MUTUALLY_EXCLUSIVE_OFFER_IND,
  RECEIPT_TXT AS RECEIPT_TXT,
  ISSUANCE_MESSAGE AS ISSUANCE_MESSAGE,
  OFFER_STATUS AS OFFER_STATUS,
  UAT_TEST_STATUS AS UAT_TEST_STATUS,
  CANCELLED_IND AS CANCELLED_IND,
  SCHED_OFFER_DEPLOYMENT_DT AS SCHED_OFFER_DEPLOYMENT_DT,
  APPROVAL_DTL AS APPROVAL_DTL,
  UPCA_NBR_TXT AS UPCA_NBR_TXT,
  CATEGORY_CD_AND_NAME AS CATEGORY_CD_AND_NAME,
  AMS_OFFER_ID AS AMS_OFFER_ID,
  AMS_TEMPLATE AS AMS_TEMPLATE,
  CREATED_BY AS CREATED_BY,
  MODIFIED_BY AS MODIFIED_BY,
  UPDATE_TSTMP AS UPDATE_TSTMP,
  LOAD_TSTMP AS LOAD_TSTMP
FROM
  AMS_OFFER_SUBMISSION""")

df_7.createOrReplaceTempView("Shortcut_to_AMS_OFFER_SUBMISSION1_7")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_MA_EVENT_8


df_8 = spark.sql("""SELECT
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

df_8.createOrReplaceTempView("Shortcut_to_MA_EVENT_8")

# COMMAND ----------
# DBTITLE 1, MA_EVENT_EXISTING_9


df_9 = spark.sql("""WITH AMS_OFFER_VF AS (
  SELECT
    O.AMS_OFFER_ID,
    O.MFG_VENDOR_BRAND_NAME,
    O.VENDOR_FUNDED_VALUE,
    O.VENDOR_FUNDED_LIMIT,
    CASE
      WHEN TRIM(O.VENDOR_FUNDED_TYPE) = '%' THEN 1
      ELSE 0
    END AS MA_PCT_IND,
    MAX(O.UPDATE_TSTMP) AS UPDATE_TSTMP
  FROM
    Shortcut_to_AMS_OFFER_SUBMISSION_6 O,
    (
      SELECT
        OFFER_ID,
        MAX(OFFER_CHARGEBACK_ID) AS OFFER_CHARGEBACK_ID
      FROM
        ams_offer_discount
      WHERE
        OFFER_CHARGEBACK_ID IS NOT NULL
      GROUP BY
        OFFER_ID
    ) R,
    Shortcut_to_AMS_OFFER_CHARGEBACK_1 C
  WHERE
    R.OFFER_ID = O.AMS_OFFER_ID
    AND R.OFFER_CHARGEBACK_ID = C.OFFER_CHARGEBACK_ID
    AND C.ITEM_DISC_IND = 1
    AND TRIM(O.VENDOR_FUNDED_TYPE) IN ('%', '$')
    AND O.VENDOR_FUNDED_VALUE IS NOT NULL
    AND O.CANCELLED_IND = 0
  GROUP BY
    O.AMS_OFFER_ID,
    O.MFG_VENDOR_BRAND_NAME,
    O.VENDOR_FUNDED_VALUE,
    O.VENDOR_FUNDED_LIMIT,
    CASE
      WHEN TRIM(O.VENDOR_FUNDED_TYPE) = '%' THEN 1
      ELSE 0
    END
  HAVING
    COUNT(*) = 1
)
SELECT
  E.MA_EVENT_ID AS MA_EVENT_ID,
  A.OFFER_ID AS OFFER_ID,
  A.OFFER_START_DT AS OFFER_START_DT,
  A.OFFER_END_DT AS OFFER_END_DT,
  2 AS MA_EVENT_TYPE_ID,
  6 AS MA_EVENT_SOURCE_ID,
  A.OFFER_NAME AS MA_EVENT_DESC,
  TT.MA_PCT_IND AS MA_PCT_IND,
  TT.VENDOR_FUNDED_VALUE AS MA_AMT,
  TT.VENDOR_FUNDED_LIMIT AS MA_MAX_AMT,
  CASE
    WHEN TT.AMS_OFFER_ID IS NOT NULL THEN 1
    ELSE 0
  END AS OFFER_AS_DISC_IND,
  CASE
    WHEN TT.AMS_OFFER_ID IS NOT NULL THEN 1
    ELSE 0
  END AS VENDOR_FUNDED_IND,
  TT.MFG_VENDOR_BRAND_NAME AS VENDOR_NAME_TXT,
  0 AS INSERT_FLAG,
  A.DELETE_FLAG AS DELETE_FLAG,
  monotonically_increasing_id() AS Monotonically_Increasing_Id
FROM
  Shortcut_to_AMS_OFFER_4 A
  JOIN Shortcut_to_MA_EVENT_8 E ON A.OFFER_ID = E.OFFER_ID
  LEFT JOIN AMS_OFFER_VF TT ON A.OFFER_ID = TT.AMS_OFFER_ID
WHERE
  (
    A.UPDATE_TSTMP > CURRENT_DATE - 2
    OR TT.UPDATE_TSTMP > CURRENT_DATE - 2
  )
  AND A.OFFER_ID <> 3949""")

df_9.createOrReplaceTempView("MA_EVENT_EXISTING_9")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_MA_EVENT1_10


df_10 = spark.sql("""SELECT
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

df_10.createOrReplaceTempView("Shortcut_to_MA_EVENT1_10")

# COMMAND ----------
# DBTITLE 1, MA_EVENT_NEW_11


df_11 = spark.sql("""WITH AMS_OFFER_VF AS (
  SELECT
    O.AMS_OFFER_ID,
    O.MFG_VENDOR_BRAND_NAME,
    O.VENDOR_FUNDED_VALUE,
    O.VENDOR_FUNDED_LIMIT,
    CASE
      WHEN TRIM(O.VENDOR_FUNDED_TYPE) = '%' THEN 1
      ELSE 0
    END AS MA_PCT_IND,
    MAX(O.UPDATE_TSTMP) AS UPDATE_TSTMP
  FROM
    Shortcut_to_AMS_OFFER_SUBMISSION1_7 O,
    (
      SELECT
        OFFER_ID,
        MAX(OFFER_CHARGEBACK_ID) AS OFFER_CHARGEBACK_ID
      FROM
        ams_offer_discount
      WHERE
        OFFER_CHARGEBACK_ID IS NOT NULL
      GROUP BY
        OFFER_ID
    ) R,
    Shortcut_to_AMS_OFFER_CHARGEBACK1_2 C
  WHERE
    R.OFFER_ID = O.AMS_OFFER_ID
    AND R.OFFER_CHARGEBACK_ID = C.OFFER_CHARGEBACK_ID
    AND C.ITEM_DISC_IND = 1
    AND TRIM(O.VENDOR_FUNDED_TYPE) IN ('%', '$')
    AND O.VENDOR_FUNDED_VALUE IS NOT NULL
    AND O.CANCELLED_IND = 0
  GROUP BY
    O.AMS_OFFER_ID,
    O.MFG_VENDOR_BRAND_NAME,
    O.VENDOR_FUNDED_VALUE,
    O.VENDOR_FUNDED_LIMIT,
    CASE
      WHEN TRIM(O.VENDOR_FUNDED_TYPE) = '%' THEN 1
      ELSE 0
    END
  HAVING
    COUNT(*) = 1
)
SELECT
  A.OFFER_ID AS OFFER_ID,
  A.OFFER_START_DT AS OFFER_START_DT,
  A.OFFER_END_DT AS OFFER_END_DT,
  2 AS MA_EVENT_TYPE_ID,
  6 AS MA_EVENT_SOURCE_ID,
  A.OFFER_NAME AS MA_EVENT_DESC,
  TT.MA_PCT_IND AS MA_PCT_IND,
  TT.VENDOR_FUNDED_VALUE AS MA_AMT,
  TT.VENDOR_FUNDED_LIMIT AS MA_MAX_AMT,
  1 AS OFFER_AS_DISC_IND,
  1 AS VENDOR_FUNDED_IND,
  TT.MFG_VENDOR_BRAND_NAME AS VENDOR_NAME_TXT,
  1 AS INSERT_FLAG,
  A.DELETE_FLAG AS DELETE_FLAG,
  monotonically_increasing_id() AS Monotonically_Increasing_Id
FROM
  Shortcut_to_AMS_OFFER1_5 A
  JOIN AMS_OFFER_VF TT ON A.OFFER_ID = TT.AMS_OFFER_ID
  LEFT JOIN Shortcut_to_MA_EVENT1_10 E ON A.OFFER_ID = E.OFFER_ID
WHERE
  (
    A.UPDATE_TSTMP > CURRENT_DATE - 2
    OR TT.UPDATE_TSTMP > CURRENT_DATE - 2
  )
  AND A.DELETE_FLAG = 0
  AND E.OFFER_ID IS NULL
  AND A.OFFER_ID <> 3949""")

df_11.createOrReplaceTempView("MA_EVENT_NEW_11")

# COMMAND ----------
# DBTITLE 1, EXP_NEW_12


df_12 = spark.sql("""SELECT
  NEXTVAL AS MA_EVENT_ID,
  OFFER_ID AS OFFER_ID,
  OFFER_START_DT AS OFFER_START_DT,
  OFFER_END_DT AS OFFER_END_DT,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  MA_EVENT_DESC AS MA_EVENT_DESC,
  MA_PCT_IND AS MA_PCT_IND,
  MA_AMT AS MA_AMT,
  MA_MAX_AMT AS MA_MAX_AMT,
  OFFER_AS_DISC_IND AS OFFER_AS_DISC_IND,
  VENDOR_FUNDED_IND AS VENDOR_FUNDED_IND,
  VENDOR_NAME_TXT AS VENDOR_NAME_TXT,
  INSERT_FLAG AS INSERT_FLAG,
  DELETE_FLAG AS DELETE_FLAG,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  MA_EVENT_NEW_11""")

df_12.createOrReplaceTempView("EXP_NEW_12")

spark.sql("""UPDATE SEQ_MA_EVENT_ID SET CURRVAL = (SELECT MAX(MA_EVENT_ID) FROM EXP_NEW_12) , NEXTVAL = (SELECT MAX(MA_EVENT_ID) FROM EXP_NEW_12) + (SELECT Increment_By FROM EXP_NEW_12)""")

# COMMAND ----------
# DBTITLE 1, UNI_AMS_13


df_13 = spark.sql("""SELECT
  MA_EVENT_ID AS MA_EVENT_ID,
  OFFER_ID AS OFFER_ID,
  OFFER_START_DT AS OFFER_START_DT,
  OFFER_END_DT AS OFFER_END_DT,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  MA_EVENT_DESC AS MA_EVENT_DESC,
  MA_PCT_IND AS MA_PCT_IND,
  MA_AMT AS MA_AMT,
  MA_MAX_AMT AS MA_MAX_AMT,
  OFFER_AS_DISC_IND AS OFFER_AS_DISC_IND,
  VENDOR_FUNDED_IND AS VENDOR_FUNDED_IND,
  VENDOR_NAME_TXT AS VENDOR_NAME_TXT,
  INSERT_FLAG AS INSERT_FLAG,
  DELETE_FLAG AS DELETE_FLAG,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  MA_EVENT_EXISTING_9
UNION ALL
SELECT
  MA_EVENT_ID AS MA_EVENT_ID,
  OFFER_ID AS OFFER_ID,
  OFFER_START_DT AS OFFER_START_DT,
  OFFER_END_DT AS OFFER_END_DT,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  MA_EVENT_DESC AS MA_EVENT_DESC,
  MA_PCT_IND AS MA_PCT_IND,
  MA_AMT AS MA_AMT,
  MA_MAX_AMT AS MA_MAX_AMT,
  OFFER_AS_DISC_IND AS OFFER_AS_DISC_IND,
  VENDOR_FUNDED_IND AS VENDOR_FUNDED_IND,
  VENDOR_NAME_TXT AS VENDOR_NAME_TXT,
  INSERT_FLAG AS INSERT_FLAG,
  DELETE_FLAG AS DELETE_FLAG,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  EXP_NEW_12""")

df_13.createOrReplaceTempView("UNI_AMS_13")

# COMMAND ----------
# DBTITLE 1, MA_EVENT_AMS_PRE


spark.sql("""INSERT INTO
  MA_EVENT_AMS_PRE
SELECT
  MA_EVENT_ID AS MA_EVENT_ID,
  OFFER_ID AS OFFER_ID,
  OFFER_START_DT AS START_DT,
  OFFER_END_DT AS END_DT,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  MA_EVENT_DESC AS MA_EVENT_DESC,
  MA_PCT_IND AS MA_PCT_IND,
  MA_AMT AS MA_AMT,
  MA_MAX_AMT AS MA_MAX_AMT,
  OFFER_AS_DISC_IND AS OFFER_AS_DISC_IND,
  VENDOR_FUNDED_IND AS VENDOR_FUNDED_IND,
  VENDOR_NAME_TXT AS VENDOR_NAME_TXT,
  INSERT_FLAG AS INSERT_FLAG,
  DELETE_FLAG AS DELETE_FLAG
FROM
  UNI_AMS_13""")