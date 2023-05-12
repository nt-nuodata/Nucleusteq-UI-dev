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
# DBTITLE 1, Shortcut_to_MA_EVENT_SOURCE_1


df_1 = spark.sql("""SELECT
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  MA_EVENT_SOURCE_DESC AS MA_EVENT_SOURCE_DESC,
  TARGET_TABLE AS TARGET_TABLE,
  UPDATE_DT AS UPDATE_DT,
  LOAD_DT AS LOAD_DT
FROM
  MA_EVENT_SOURCE""")

df_1.createOrReplaceTempView("Shortcut_to_MA_EVENT_SOURCE_1")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_MA_EVENT11_2


df_2 = spark.sql("""SELECT
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

df_2.createOrReplaceTempView("Shortcut_to_MA_EVENT11_2")

# COMMAND ----------
# DBTITLE 1, ASQ_MA_EVENT_NEW_3


df_3 = spark.sql("""SELECT
  sp.product_id AS PRODUCT_ID,
  c.country_cd AS COUNTRY_CD,
  CURRENT_DATE - 1 AS START_DT,
  TO_DATE('12/31/9999', 'mm/dd/yyyy') AS END_DT,
  1 AS MA_EVENT_TYPE_ID,
  mes.ma_event_source_id AS MA_EVENT_SOURCE_ID,
  mes.ma_event_source_desc || ' - SKU=' || CAST(sp.sku_nbr AS CHARACTER (7)) || ' - Country=' || c.country_cd AS MA_EVENT_DESC,
  -.25 AS MA_AMT,
  CURRENT_DATE AS UPDATE_DT,
  CURRENT_DATE AS LOAD_DT,
  'I' AS INS_UPD_FLAG,
  monotonically_increasing_id() AS Monotonically_Increasing_Id
FROM
  sku_profile sp,
  country c,
  (
    SELECT
      *
    FROM
      ma_event_source
    WHERE
      ma_event_source_id IN (4, 5)
  ) mes
WHERE
  sp.sap_dept_id IN (3117, 3007, 18, 28)
  AND c.country_cd IN ('CA', 'US')
  AND (
    sp.product_id,
    c.country_cd,
    mes.ma_event_source_id
  ) NOT IN (
    SELECT
      e.product_id,
      e.country_cd,
      e.ma_event_source_id
    FROM
      Shortcut_to_MA_EVENT11_2 e
    WHERE
      e.ma_event_source_id IN (4, 5)
      AND e.ma_event_type_id = 1
      AND e.end_dt = TO_DATE('12/31/9999', 'mm/dd/yyyy')
  )""")

df_3.createOrReplaceTempView("ASQ_MA_EVENT_NEW_3")

# COMMAND ----------
# DBTITLE 1, EXP_NEW_4


df_4 = spark.sql("""SELECT
  NEXTVAL AS MA_EVENT_ID,
  PRODUCT_ID AS PRODUCT_ID,
  COUNTRY_CD AS COUNTRY_CD,
  START_DT AS START_DT,
  END_DT AS END_DT,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  MA_EVENT_DESC AS MA_EVENT_DESC,
  MA_AMT AS MA_AMT,
  UPDATE_DT AS UPDATE_DT,
  LOAD_DT AS LOAD_DT,
  INS_UPD_FLAG AS INS_UPD_FLAG,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  ASQ_MA_EVENT_NEW_3""")

df_4.createOrReplaceTempView("EXP_NEW_4")

spark.sql("""UPDATE SEQ_MA_EVENT_ID SET CURRVAL = (SELECT MAX(MA_EVENT_ID) FROM EXP_NEW_4) , NEXTVAL = (SELECT MAX(MA_EVENT_ID) FROM EXP_NEW_4) + (SELECT Increment_By FROM EXP_NEW_4)""")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_MA_EVENT1_5


df_5 = spark.sql("""SELECT
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

df_5.createOrReplaceTempView("Shortcut_to_MA_EVENT1_5")

# COMMAND ----------
# DBTITLE 1, ASQ_MA_EVENT_EXISTING_6


df_6 = spark.sql("""SELECT
  e.ma_event_id AS MA_EVENT_ID,
  e.product_id AS PRODUCT_ID,
  e.country_cd AS COUNTRY_CD,
  e.start_dt AS START_DT,
  CURRENT_DATE - 1 AS END_DT,
  e.ma_event_type_id AS MA_EVENT_TYPE_ID,
  e.ma_event_source_id AS MA_EVENT_SOURCE_ID,
  e.ma_event_desc AS MA_EVENT_DESC,
  e.ma_amt AS MA_AMT,
  CURRENT_DATE AS UPDATE_DT,
  e.load_dt AS LOAD_DT,
  'U' AS INS_UPD_FLAG,
  monotonically_increasing_id() AS Monotonically_Increasing_Id
FROM
  Shortcut_to_MA_EVENT1_5 e
WHERE
  e.ma_event_source_id IN (4, 5)
  AND e.ma_event_type_id = 1
  AND e.end_dt = TO_DATE('12/31/9999', 'mm/dd/yyyy')
  AND (product_id, country_cd, ma_event_source_id) NOT IN (
    SELECT
      product_id,
      c.country_cd,
      mes.ma_event_source_id
    FROM
      sku_profile sp,
      country c,
      (
        SELECT
          *
        FROM
          ma_event_source
        WHERE
          ma_event_source_id IN (4, 5)
      ) mes
    WHERE
      sp.sap_dept_id IN (3117, 3007, 18, 28)
      AND c.country_cd IN ('CA', 'US')
  )""")

df_6.createOrReplaceTempView("ASQ_MA_EVENT_EXISTING_6")

# COMMAND ----------
# DBTITLE 1, UNI_RX_7


df_7 = spark.sql("""SELECT
  MA_EVENT_ID AS MA_EVENT_ID,
  PRODUCT_ID AS PRODUCT_ID,
  COUNTRY_CD AS COUNTRY_CD,
  START_DT AS START_DT,
  END_DT AS END_DT,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  MA_EVENT_DESC AS MA_EVENT_DESC,
  MA_AMT AS MA_AMT,
  UPDATE_DT AS UPDATE_DT,
  LOAD_DT AS LOAD_DT,
  INS_UPD_FLAG AS INS_UPD_FLAG,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  ASQ_MA_EVENT_EXISTING_6
UNION ALL
SELECT
  MA_EVENT_ID AS MA_EVENT_ID,
  PRODUCT_ID AS PRODUCT_ID,
  COUNTRY_CD AS COUNTRY_CD,
  START_DT AS START_DT,
  END_DT AS END_DT,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  MA_EVENT_DESC AS MA_EVENT_DESC,
  MA_AMT AS MA_AMT,
  UPDATE_DT AS UPDATE_DT,
  LOAD_DT AS LOAD_DT,
  INS_UPD_FLAG AS INS_UPD_FLAG,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  EXP_NEW_4""")

df_7.createOrReplaceTempView("UNI_RX_7")

# COMMAND ----------
# DBTITLE 1, UPD_MA_EVENT_8


df_8 = spark.sql("""SELECT
  MA_EVENT_ID AS MA_EVENT_ID,
  PRODUCT_ID AS PRODUCT_ID,
  COUNTRY_CD AS COUNTRY_CD,
  START_DT AS START_DT,
  END_DT AS END_DT,
  MA_EVENT_TYPE_ID AS MA_EVENT_TYPE_ID,
  MA_EVENT_SOURCE_ID AS MA_EVENT_SOURCE_ID,
  MA_EVENT_DESC AS MA_EVENT_DESC,
  MA_AMT AS MA_AMT,
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
  UNI_RX_7""")

df_8.createOrReplaceTempView("UPD_MA_EVENT_8")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_COUNTRY_9


df_9 = spark.sql("""SELECT
  COUNTRY_CD AS COUNTRY_CD,
  COUNTRY_NAME AS COUNTRY_NAME
FROM
  COUNTRY""")

df_9.createOrReplaceTempView("Shortcut_to_COUNTRY_9")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_SKU_PROFILE_10


df_10 = spark.sql("""SELECT
  PRODUCT_ID AS PRODUCT_ID,
  SKU_NBR AS SKU_NBR,
  SKU_TYPE AS SKU_TYPE,
  PRIMARY_UPC_ID AS PRIMARY_UPC_ID,
  STATUS_ID AS STATUS_ID,
  SUBS_HIST_FLAG AS SUBS_HIST_FLAG,
  SUBS_CURR_FLAG AS SUBS_CURR_FLAG,
  SKU_DESC AS SKU_DESC,
  ALT_DESC AS ALT_DESC,
  SAP_CATEGORY_ID AS SAP_CATEGORY_ID,
  SAP_CLASS_ID AS SAP_CLASS_ID,
  SAP_DEPT_ID AS SAP_DEPT_ID,
  SAP_DIVISION_ID AS SAP_DIVISION_ID,
  PRIMARY_VENDOR_ID AS PRIMARY_VENDOR_ID,
  PARENT_VENDOR_ID AS PARENT_VENDOR_ID,
  COUNTRY_CD AS COUNTRY_CD,
  IMPORT_FLAG AS IMPORT_FLAG,
  HTS_CODE_ID AS HTS_CODE_ID,
  CONTENTS AS CONTENTS,
  CONTENTS_UNITS AS CONTENTS_UNITS,
  WEIGHT_NET_AMT AS WEIGHT_NET_AMT,
  WEIGHT_UOM_CD AS WEIGHT_UOM_CD,
  SIZE_DESC AS SIZE_DESC,
  BUM_QTY AS BUM_QTY,
  UOM_CD AS UOM_CD,
  UNIT_NUMERATOR AS UNIT_NUMERATOR,
  UNIT_DENOMINATOR AS UNIT_DENOMINATOR,
  BUYER_ID AS BUYER_ID,
  PURCH_GROUP_ID AS PURCH_GROUP_ID,
  PURCH_COST_AMT AS PURCH_COST_AMT,
  NAT_PRICE_US_AMT AS NAT_PRICE_US_AMT,
  TAX_CLASS_ID AS TAX_CLASS_ID,
  VALUATION_CLASS_CD AS VALUATION_CLASS_CD,
  BRAND_CD AS BRAND_CD,
  BRAND_CLASSIFICATION_ID AS BRAND_CLASSIFICATION_ID,
  OWNBRAND_FLAG AS OWNBRAND_FLAG,
  STATELINE_FLAG AS STATELINE_FLAG,
  SIGN_TYPE_CD AS SIGN_TYPE_CD,
  OLD_ARTICLE_NBR AS OLD_ARTICLE_NBR,
  VENDOR_ARTICLE_NBR AS VENDOR_ARTICLE_NBR,
  INIT_MKDN_DT AS INIT_MKDN_DT,
  DISC_START_DT AS DISC_START_DT,
  ADD_DT AS ADD_DT,
  DELETE_DT AS DELETE_DT,
  UPDATE_DT AS UPDATE_DT,
  FIRST_SALE_DT AS FIRST_SALE_DT,
  LAST_SALE_DT AS LAST_SALE_DT,
  FIRST_INV_DT AS FIRST_INV_DT,
  LAST_INV_DT AS LAST_INV_DT,
  LOAD_DT AS LOAD_DT,
  BASE_NBR AS BASE_NBR,
  BP_COLOR_ID AS BP_COLOR_ID,
  BP_SIZE_ID AS BP_SIZE_ID,
  BP_BREED_ID AS BP_BREED_ID,
  BP_ITEM_CONCATENATED AS BP_ITEM_CONCATENATED,
  BP_AEROSOL_FLAG AS BP_AEROSOL_FLAG,
  BP_HAZMAT_FLAG AS BP_HAZMAT_FLAG,
  CANADIAN_HTS_CD AS CANADIAN_HTS_CD,
  NAT_PRICE_CA_AMT AS NAT_PRICE_CA_AMT,
  NAT_PRICE_PR_AMT AS NAT_PRICE_PR_AMT,
  RTV_DEPT_CD AS RTV_DEPT_CD,
  GL_ACCT_NBR AS GL_ACCT_NBR,
  ARTICLE_CATEGORY_ID AS ARTICLE_CATEGORY_ID,
  COMPONENT_FLAG AS COMPONENT_FLAG,
  ZDISCO_SCHED_TYPE_ID AS ZDISCO_SCHED_TYPE_ID,
  ZDISCO_MKDN_SCHED_ID AS ZDISCO_MKDN_SCHED_ID,
  ZDISCO_PID_DT AS ZDISCO_PID_DT,
  ZDISCO_START_DT AS ZDISCO_START_DT,
  ZDISCO_INIT_MKDN_DT AS ZDISCO_INIT_MKDN_DT,
  ZDISCO_DC_DT AS ZDISCO_DC_DT,
  ZDISCO_STR_DT AS ZDISCO_STR_DT,
  ZDISCO_STR_OWNRSHP_DT AS ZDISCO_STR_OWNRSHP_DT,
  ZDISCO_STR_WRT_OFF_DT AS ZDISCO_STR_WRT_OFF_DT
FROM
  SKU_PROFILE""")

df_10.createOrReplaceTempView("Shortcut_to_SKU_PROFILE_10")

# COMMAND ----------
# DBTITLE 1, MA_EVENT


spark.sql("""MERGE INTO MA_EVENT AS TARGET
USING
  UPD_MA_EVENT_8 AS SOURCE ON TARGET.MA_EVENT_ID = SOURCE.MA_EVENT_ID
  WHEN MATCHED
  AND SOURCE.UPDATE_STRATEGY_FLAG = "DD_UPDATE" THEN
UPDATE
SET
  TARGET.MA_EVENT_ID = SOURCE.MA_EVENT_ID,
  TARGET.PRODUCT_ID = SOURCE.PRODUCT_ID,
  TARGET.COUNTRY_CD = SOURCE.COUNTRY_CD,
  TARGET.START_DT = SOURCE.START_DT,
  TARGET.END_DT = SOURCE.END_DT,
  TARGET.MA_EVENT_TYPE_ID = SOURCE.MA_EVENT_TYPE_ID,
  TARGET.MA_EVENT_SOURCE_ID = SOURCE.MA_EVENT_SOURCE_ID,
  TARGET.MA_EVENT_DESC = SOURCE.MA_EVENT_DESC,
  TARGET.MA_AMT = SOURCE.MA_AMT,
  TARGET.UPDATE_DT = SOURCE.UPDATE_DT,
  TARGET.LOAD_DT = SOURCE.LOAD_DT
  WHEN MATCHED
  AND SOURCE.UPDATE_STRATEGY_FLAG = "DD_DELETE"
  AND TARGET.PRODUCT_ID = SOURCE.PRODUCT_ID
  AND TARGET.COUNTRY_CD = SOURCE.COUNTRY_CD
  AND TARGET.START_DT = SOURCE.START_DT
  AND TARGET.END_DT = SOURCE.END_DT
  AND TARGET.MA_EVENT_TYPE_ID = SOURCE.MA_EVENT_TYPE_ID
  AND TARGET.MA_EVENT_SOURCE_ID = SOURCE.MA_EVENT_SOURCE_ID
  AND TARGET.MA_EVENT_DESC = SOURCE.MA_EVENT_DESC
  AND TARGET.MA_AMT = SOURCE.MA_AMT
  AND TARGET.UPDATE_DT = SOURCE.UPDATE_DT
  AND TARGET.LOAD_DT = SOURCE.LOAD_DT THEN DELETE
  WHEN NOT MATCHED
  AND SOURCE.UPDATE_STRATEGY_FLAG = "DD_INSERT" THEN
INSERT
  (
    TARGET.MA_EVENT_ID,
    TARGET.PRODUCT_ID,
    TARGET.COUNTRY_CD,
    TARGET.START_DT,
    TARGET.END_DT,
    TARGET.MA_EVENT_TYPE_ID,
    TARGET.MA_EVENT_SOURCE_ID,
    TARGET.MA_EVENT_DESC,
    TARGET.MA_AMT,
    TARGET.UPDATE_DT,
    TARGET.LOAD_DT
  )
VALUES
  (
    SOURCE.MA_EVENT_ID,
    SOURCE.PRODUCT_ID,
    SOURCE.COUNTRY_CD,
    SOURCE.START_DT,
    SOURCE.END_DT,
    SOURCE.MA_EVENT_TYPE_ID,
    SOURCE.MA_EVENT_SOURCE_ID,
    SOURCE.MA_EVENT_DESC,
    SOURCE.MA_AMT,
    SOURCE.UPDATE_DT,
    SOURCE.LOAD_DT
  )""")