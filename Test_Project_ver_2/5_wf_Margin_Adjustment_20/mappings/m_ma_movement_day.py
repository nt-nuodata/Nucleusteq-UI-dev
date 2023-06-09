# Databricks notebook source
# MAGIC %run "./udf_informatica"

# COMMAND ----------


from pyspark.sql.types import *

spark.sql("use DELTA_TRAINING")
spark.sql("set spark.sql.legacy.timeParserPolicy = LEGACY")


# COMMAND ----------
# DBTITLE 1, Shortcut_to_MA_MOVEMENT_PRE_0


df_0 = spark.sql("""SELECT
  DAY_DT AS DAY_DT,
  PRODUCT_ID AS PRODUCT_ID,
  LOCATION_ID AS LOCATION_ID,
  MOVEMENT_ID AS MOVEMENT_ID,
  PO_NBR AS PO_NBR,
  PO_LINE_NBR AS PO_LINE_NBR,
  MA_EVENT_ID AS MA_EVENT_ID,
  STO_TYPE_ID AS STO_TYPE_ID,
  MA_TRANS_AMT AS MA_TRANS_AMT,
  MA_TRANS_COST AS MA_TRANS_COST,
  MA_TRANS_QTY AS MA_TRANS_QTY,
  EXCH_RATE_PCT AS EXCH_RATE_PCT,
  UPDATE_DT AS UPDATE_DT,
  LOAD_DT AS LOAD_DT,
  INS_UPD_FLAG AS INS_UPD_FLAG
FROM
  MA_MOVEMENT_PRE""")

df_0.createOrReplaceTempView("Shortcut_to_MA_MOVEMENT_PRE_0")

# COMMAND ----------
# DBTITLE 1, SQ_Shortcut_to_MA_MOVEMENT_PRE_1


df_1 = spark.sql("""SELECT
  DAY_DT AS DAY_DT,
  PRODUCT_ID AS PRODUCT_ID,
  LOCATION_ID AS LOCATION_ID,
  MOVEMENT_ID AS MOVEMENT_ID,
  PO_NBR AS PO_NBR,
  PO_LINE_NBR AS PO_LINE_NBR,
  MA_EVENT_ID AS MA_EVENT_ID,
  STO_TYPE_ID AS STO_TYPE_ID,
  MA_TRANS_AMT AS MA_TRANS_AMT,
  MA_TRANS_COST AS MA_TRANS_COST,
  MA_TRANS_QTY AS MA_TRANS_QTY,
  EXCH_RATE_PCT AS EXCH_RATE_PCT,
  UPDATE_DT AS UPDATE_DT,
  LOAD_DT AS LOAD_DT,
  INS_UPD_FLAG AS INS_UPD_FLAG,
  monotonically_increasing_id() AS Monotonically_Increasing_Id
FROM
  Shortcut_to_MA_MOVEMENT_PRE_0""")

df_1.createOrReplaceTempView("SQ_Shortcut_to_MA_MOVEMENT_PRE_1")

# COMMAND ----------
# DBTITLE 1, UPD_MA_MOVEMENT_DAY_2


df_2 = spark.sql("""SELECT
  DAY_DT AS DAY_DT,
  PRODUCT_ID AS PRODUCT_ID,
  LOCATION_ID AS LOCATION_ID,
  MOVEMENT_ID AS MOVEMENT_ID,
  PO_NBR AS PO_NBR,
  PO_LINE_NBR AS PO_LINE_NBR,
  MA_EVENT_ID AS MA_EVENT_ID,
  STO_TYPE_ID AS STO_TYPE_ID,
  MA_TRANS_AMT AS MA_TRANS_AMT,
  MA_TRANS_COST AS MA_TRANS_COST,
  MA_TRANS_QTY AS MA_TRANS_QTY,
  EXCH_RATE_PCT AS EXCH_RATE_PCT,
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
  SQ_Shortcut_to_MA_MOVEMENT_PRE_1""")

df_2.createOrReplaceTempView("UPD_MA_MOVEMENT_DAY_2")

# COMMAND ----------
# DBTITLE 1, MA_MOVEMENT_DAY


spark.sql("""MERGE INTO MA_MOVEMENT_DAY AS TARGET
USING
  UPD_MA_MOVEMENT_DAY_2 AS SOURCE ON TARGET.PRODUCT_ID = SOURCE.PRODUCT_ID
  AND TARGET.LOCATION_ID = SOURCE.LOCATION_ID
  AND TARGET.MOVEMENT_ID = SOURCE.MOVEMENT_ID
  AND TARGET.DAY_DT = SOURCE.DAY_DT
  AND TARGET.PO_NBR = SOURCE.PO_NBR
  AND TARGET.PO_LINE_NBR = SOURCE.PO_LINE_NBR
  AND TARGET.MA_EVENT_ID = SOURCE.MA_EVENT_ID
  WHEN MATCHED
  AND SOURCE.UPDATE_STRATEGY_FLAG = "DD_UPDATE" THEN
UPDATE
SET
  TARGET.DAY_DT = SOURCE.DAY_DT,
  TARGET.PRODUCT_ID = SOURCE.PRODUCT_ID,
  TARGET.LOCATION_ID = SOURCE.LOCATION_ID,
  TARGET.MOVEMENT_ID = SOURCE.MOVEMENT_ID,
  TARGET.PO_NBR = SOURCE.PO_NBR,
  TARGET.PO_LINE_NBR = SOURCE.PO_LINE_NBR,
  TARGET.MA_EVENT_ID = SOURCE.MA_EVENT_ID,
  TARGET.STO_TYPE_ID = SOURCE.STO_TYPE_ID,
  TARGET.MA_TRANS_AMT = SOURCE.MA_TRANS_AMT,
  TARGET.MA_TRANS_COST = SOURCE.MA_TRANS_COST,
  TARGET.MA_TRANS_QTY = SOURCE.MA_TRANS_QTY,
  TARGET.EXCH_RATE_PCT = SOURCE.EXCH_RATE_PCT,
  TARGET.UPDATE_DT = SOURCE.UPDATE_DT,
  TARGET.LOAD_DT = SOURCE.LOAD_DT
  WHEN MATCHED
  AND SOURCE.UPDATE_STRATEGY_FLAG = "DD_DELETE"
  AND TARGET.STO_TYPE_ID = SOURCE.STO_TYPE_ID
  AND TARGET.MA_TRANS_AMT = SOURCE.MA_TRANS_AMT
  AND TARGET.MA_TRANS_COST = SOURCE.MA_TRANS_COST
  AND TARGET.MA_TRANS_QTY = SOURCE.MA_TRANS_QTY
  AND TARGET.EXCH_RATE_PCT = SOURCE.EXCH_RATE_PCT
  AND TARGET.UPDATE_DT = SOURCE.UPDATE_DT
  AND TARGET.LOAD_DT = SOURCE.LOAD_DT THEN DELETE
  WHEN NOT MATCHED
  AND SOURCE.UPDATE_STRATEGY_FLAG = "DD_INSERT" THEN
INSERT
  (
    TARGET.DAY_DT,
    TARGET.PRODUCT_ID,
    TARGET.LOCATION_ID,
    TARGET.MOVEMENT_ID,
    TARGET.PO_NBR,
    TARGET.PO_LINE_NBR,
    TARGET.MA_EVENT_ID,
    TARGET.STO_TYPE_ID,
    TARGET.MA_TRANS_AMT,
    TARGET.MA_TRANS_COST,
    TARGET.MA_TRANS_QTY,
    TARGET.EXCH_RATE_PCT,
    TARGET.UPDATE_DT,
    TARGET.LOAD_DT
  )
VALUES
  (
    SOURCE.DAY_DT,
    SOURCE.PRODUCT_ID,
    SOURCE.LOCATION_ID,
    SOURCE.MOVEMENT_ID,
    SOURCE.PO_NBR,
    SOURCE.PO_LINE_NBR,
    SOURCE.MA_EVENT_ID,
    SOURCE.STO_TYPE_ID,
    SOURCE.MA_TRANS_AMT,
    SOURCE.MA_TRANS_COST,
    SOURCE.MA_TRANS_QTY,
    SOURCE.EXCH_RATE_PCT,
    SOURCE.UPDATE_DT,
    SOURCE.LOAD_DT
  )""")