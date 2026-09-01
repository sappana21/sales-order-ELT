# Databricks notebook source
import dlt

# COMMAND ----------

@dlt.table(name="sales_silver")
def sales_silver():
    return(
        dlt.read("sales_bronze")
        .select(
            "Order_ID",
            "Customer",
            "Product",
            "Category",
            "Quantity",
            "Unit_price",
            "Total",
            "Region",
            "Status"
        ).dropDuplicates(["Order_ID"])
    )