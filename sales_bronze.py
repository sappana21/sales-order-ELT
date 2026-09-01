# Databricks notebook source
import dlt
from pyspark.sql.functions import current_timestamp


# COMMAND ----------

source_path="/Volumes/sapana_catalog/data/datav"
@dlt.table(name="sales_bronze")
def sales_bronze():
    return(
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format","csv")
        .option("header","true")
        .option("inferSchema","true")
        .load(source_path)
        .withColumn("ingestion_time",current_timestamp())
    )