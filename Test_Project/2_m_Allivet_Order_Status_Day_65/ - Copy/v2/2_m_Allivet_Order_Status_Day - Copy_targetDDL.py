# Databricks notebook source
# COMMAND ----------

CREATE TABLE IF NOT EXISTS DELTA_TRAINING.ALLIVET_ORDER_STATUS_DAY_v2(ALLIVET_ORDER_NBR_v2 STRING,
RX_HOLD_DT DATE,
OPEN_DT_v2 DATE,
COMPLETE_DT DATE,
VOID_DT_v2 DATE,
UPDATE_TSTMP TIMESTAMP,
LOAD_TSTMP_v2 TIMESTAMP) USING DELTA;