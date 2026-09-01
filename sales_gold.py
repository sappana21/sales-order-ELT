# Databricks notebook source
import dlt
import pyspark.sql.functions as F


# COMMAND ----------

@dlt.table(name="gold_summary_by_region_category")
def gold_summary_by_region_category():
    return(
        dlt.read("sales_silver")
        .groupBy("Region","Category")
        .agg(
            F.sum("Quantity").alias("Total_quantity"),
            F.sum("Total").alias("Total_Revenue"),
            F.count("Order_ID").alias("Total_orders")
        )
    )
@dlt.table(name="sales_gold_status_summary")
def sales_gold_status_summary():
    return(
        dlt.read("sales_silver")
        .groupBy("Status")
        .agg(
            F.count("Order_ID").alias("Total_orders"),
            F.sum("Total").alias("Total_Outcome")
        )
    )
@dlt.table(name="customer_wise_revenue")
def customer_wise_revenue():
    return(
        dlt.read("sales_silver")
        .groupBy("Customer")
        .agg(
            F.sum("Total").alias("Total_spent"),
            F.count("Order_ID").alias("Total_orders")
        ) .orderBy(F.desc("Total_spent"))
    )