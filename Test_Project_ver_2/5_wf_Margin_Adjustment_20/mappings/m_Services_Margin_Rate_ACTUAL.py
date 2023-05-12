# Databricks notebook source
# MAGIC %run "./udf_informatica"

# COMMAND ----------


from pyspark.sql.types import *

spark.sql("use DELTA_TRAINING")
spark.sql("set spark.sql.legacy.timeParserPolicy = LEGACY")


# COMMAND ----------
# DBTITLE 1, Shortcut_to_SERVICES_MARGIN_RATE_PRE_0


df_0 = spark.sql("""SELECT
  WEEK_DT AS WEEK_DT,
  LOCATION_ID AS LOCATION_ID,
  SAP_DEPT_ID AS SAP_DEPT_ID,
  MARGIN_RATE AS MARGIN_RATE
FROM
  SERVICES_MARGIN_RATE_PRE""")

df_0.createOrReplaceTempView("Shortcut_to_SERVICES_MARGIN_RATE_PRE_0")

# COMMAND ----------
# DBTITLE 1, SQ_Shortcut_to_SERVICES_MARGIN_RATE_PRE_1


df_1 = spark.sql("""SELECT
  WEEK_DT AS WEEK_DT,
  LOCATION_ID AS LOCATION_ID,
  SAP_DEPT_ID AS SAP_DEPT_ID,
  MARGIN_RATE AS MARGIN_RATE,
  monotonically_increasing_id() AS Monotonically_Increasing_Id
FROM
  Shortcut_to_SERVICES_MARGIN_RATE_PRE_0""")

df_1.createOrReplaceTempView("SQ_Shortcut_to_SERVICES_MARGIN_RATE_PRE_1")

# COMMAND ----------
# DBTITLE 1, Shortcut_to_SERVICES_MARGIN_RATE_2


df_2 = spark.sql("""SELECT
  WEEK_DT AS WEEK_DT,
  LOCATION_ID AS LOCATION_ID,
  SAP_DEPT_ID AS SAP_DEPT_ID,
  MARGIN_RATE AS MARGIN_RATE,
  UPDATE_TSTMP AS UPDATE_TSTMP,
  LOAD_TSTMP AS LOAD_TSTMP
FROM
  SERVICES_MARGIN_RATE""")

df_2.createOrReplaceTempView("Shortcut_to_SERVICES_MARGIN_RATE_2")

# COMMAND ----------
# DBTITLE 1, SQ_Shortcut_to_SERVICES_MARGIN_RATE_3


df_3 = spark.sql("""SELECT
  WEEK_DT AS WEEK_DT,
  LOCATION_ID AS LOCATION_ID,
  SAP_DEPT_ID AS SAP_DEPT_ID,
  MARGIN_RATE AS MARGIN_RATE,
  UPDATE_TSTMP AS UPDATE_TSTMP,
  LOAD_TSTMP AS LOAD_TSTMP,
  monotonically_increasing_id() AS Monotonically_Increasing_Id
FROM
  Shortcut_to_SERVICES_MARGIN_RATE_2
WHERE
  Shortcut_to_SERVICES_MARGIN_RATE_2.WEEK_DT IN (
    SELECT
      DISTINCT WEEK_DT
    FROM
      SERVICES_MARGIN_RATE_PRE
  )""")

df_3.createOrReplaceTempView("SQ_Shortcut_to_SERVICES_MARGIN_RATE_3")

# COMMAND ----------
# DBTITLE 1, JNR_SERVICES_MARGIN_4


df_4 = spark.sql("""SELECT
  MASTER.WEEK_DT AS WEEK_DT,
  MASTER.LOCATION_ID AS LOCATION_ID,
  MASTER.SAP_DEPT_ID AS SAP_DEPT_ID,
  MASTER.MARGIN_RATE AS MARGIN_RATE,
  DETAIL.WEEK_DT AS WEEK_DT_OLD,
  DETAIL.LOCATION_ID AS LOCATION_ID_OLD,
  DETAIL.SAP_DEPT_ID AS SAP_DEPT_ID_OLD,
  DETAIL.MARGIN_RATE AS MARGIN_RATE_OLD,
  DETAIL.LOAD_TSTMP AS LOAD_TSTMP_OLD,
  nvl(
    MASTER.Monotonically_Increasing_Id,
    DETAIL.Monotonically_Increasing_Id
  ) AS Monotonically_Increasing_Id
FROM
  SQ_Shortcut_to_SERVICES_MARGIN_RATE_PRE_1 MASTER
  FULL OUTER JOIN SQ_Shortcut_to_SERVICES_MARGIN_RATE_3 DETAIL ON MASTER.WEEK_DT = DETAIL.WEEK_DT
  AND MASTER.LOCATION_ID = DETAIL.LOCATION_ID
  AND MASTER.SAP_DEPT_ID = DETAIL.SAP_DEPT_ID""")

df_4.createOrReplaceTempView("JNR_SERVICES_MARGIN_4")

# COMMAND ----------
# DBTITLE 1, EXP_MARGIN_RATE_5


df_5 = spark.sql("""SELECT
  IFF(ISNULL(WEEK_DT), WEEK_DT_OLD, WEEK_DT) AS WEEK_DT_OUT,
  IFF(ISNULL(LOCATION_ID), LOCATION_ID_OLD, LOCATION_ID) AS LOCATION_ID_OUT,
  IFF(ISNULL(SAP_DEPT_ID), SAP_DEPT_ID_OLD, SAP_DEPT_ID) AS SAP_DEPT_ID_OUT,
  IFF(ISNULL(MARGIN_RATE), 0, MARGIN_RATE) AS MARGIN_RATE_OUT,
  now() AS UPDATE_TSTMP,
  IFF(ISNULL(LOAD_TSTMP_OLD), now(), LOAD_TSTMP_OLD) AS LOAD_TSTMP,
  IFF(
    ISNULL(WEEK_DT_OLD),
    'DD_INSERT',
    IFF(
      IFF(ISNULL(MARGIN_RATE_OLD), -1, MARGIN_RATE_OLD) <> IFF(ISNULL(MARGIN_RATE), -1, MARGIN_RATE),
      'DD_UPDATE',
      'DD_REJECT'
    )
  ) AS UPDATE_STRATEGY,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  JNR_SERVICES_MARGIN_4""")

df_5.createOrReplaceTempView("EXP_MARGIN_RATE_5")

# COMMAND ----------
# DBTITLE 1, FIL_REJECTED_6


df_6 = spark.sql("""SELECT
  WEEK_DT_OUT AS WEEK_DT,
  LOCATION_ID_OUT AS LOCATION_ID,
  SAP_DEPT_ID_OUT AS SAP_DEPT_ID,
  MARGIN_RATE_OUT AS MARGIN_RATE,
  UPDATE_TSTMP AS UPDATE_TSTMP,
  LOAD_TSTMP AS LOAD_TSTMP,
  UPDATE_STRATEGY AS UPDATE_STRATEGY,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id
FROM
  EXP_MARGIN_RATE_5
WHERE
  UPDATE_STRATEGY <> 'DD_REJECT'""")

df_6.createOrReplaceTempView("FIL_REJECTED_6")

# COMMAND ----------
# DBTITLE 1, UPD_STRATEGY_7


df_7 = spark.sql("""SELECT
  WEEK_DT AS WEEK_DT,
  LOCATION_ID AS LOCATION_ID,
  SAP_DEPT_ID AS SAP_DEPT_ID,
  MARGIN_RATE AS MARGIN_RATE,
  UPDATE_TSTMP AS UPDATE_TSTMP,
  LOAD_TSTMP AS LOAD_TSTMP,
  UPDATE_STRATEGY AS UPDATE_STRATEGY,
  Monotonically_Increasing_Id AS Monotonically_Increasing_Id,
  UPDATE_STRATEGY AS UPDATE_STRATEGY_FLAG
FROM
  FIL_REJECTED_6""")

df_7.createOrReplaceTempView("UPD_STRATEGY_7")

# COMMAND ----------
# DBTITLE 1, SERVICES_MARGIN_RATE


spark.sql("""MERGE INTO SERVICES_MARGIN_RATE AS TARGET
USING
  UPD_STRATEGY_7 AS SOURCE ON TARGET.WEEK_DT = SOURCE.WEEK_DT
  AND TARGET.SAP_DEPT_ID = SOURCE.SAP_DEPT_ID
  AND TARGET.LOCATION_ID = SOURCE.LOCATION_ID
  WHEN MATCHED
  AND SOURCE.UPDATE_STRATEGY_FLAG = "DD_UPDATE" THEN
UPDATE
SET
  TARGET.WEEK_DT = SOURCE.WEEK_DT,
  TARGET.LOCATION_ID = SOURCE.LOCATION_ID,
  TARGET.SAP_DEPT_ID = SOURCE.SAP_DEPT_ID,
  TARGET.MARGIN_RATE = SOURCE.MARGIN_RATE,
  TARGET.UPDATE_TSTMP = SOURCE.UPDATE_TSTMP,
  TARGET.LOAD_TSTMP = SOURCE.LOAD_TSTMP
  WHEN MATCHED
  AND SOURCE.UPDATE_STRATEGY_FLAG = "DD_DELETE"
  AND TARGET.MARGIN_RATE = SOURCE.MARGIN_RATE
  AND TARGET.UPDATE_TSTMP = SOURCE.UPDATE_TSTMP
  AND TARGET.LOAD_TSTMP = SOURCE.LOAD_TSTMP THEN DELETE
  WHEN NOT MATCHED
  AND SOURCE.UPDATE_STRATEGY_FLAG = "DD_INSERT" THEN
INSERT
  (
    TARGET.WEEK_DT,
    TARGET.LOCATION_ID,
    TARGET.SAP_DEPT_ID,
    TARGET.MARGIN_RATE,
    TARGET.UPDATE_TSTMP,
    TARGET.LOAD_TSTMP
  )
VALUES
  (
    SOURCE.WEEK_DT,
    SOURCE.LOCATION_ID,
    SOURCE.SAP_DEPT_ID,
    SOURCE.MARGIN_RATE,
    SOURCE.UPDATE_TSTMP,
    SOURCE.LOAD_TSTMP
  )""")