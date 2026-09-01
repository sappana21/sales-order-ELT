# Sales Data ETL Pipeline — Delta Live Tables (DLT)

End-to-end ETL pipeline built on **Databricks Delta Live Tables (DLT)**, following the **Medallion Architecture** (Bronze → Silver → Gold) to process raw sales data into business-ready aggregated tables.

---

##  Architecture

```
┌─────────────┐      ┌─────────────┐      ┌─────────────────────────┐
│   Bronze     │ ───▶ │   Silver     │ ───▶ │          Gold            │
│ (Raw Ingest) │      │ (Cleaned)    │      │  (Business Aggregates)   │
└─────────────┘      └─────────────┘      └─────────────────────────┘
   sales_bronze          sales_silver         sales_gold_region_category
   (CSV → Delta)      (dedup, selected        sales_gold_product_performance
                        columns)               sales_gold_status_summary
                                                sales_gold_customer_summary
```

| Layer | Purpose | Table(s) |
|---|---|---|
| **Bronze** | Raw ingestion of source CSV, no transformation | `sales_bronze` |
| **Silver** | Cleaned, deduplicated, relevant columns selected | `sales_silver` |
| **Gold** | Aggregated, business-ready summary tables | `sales_gold_*` |

---

##  Project Structure

```
├── pipelines/
│   ├── 01_bronze.py          # Raw data ingestion
│   ├── 02_silver.py          # Cleaning & deduplication
│   └── 03_gold.py            # Business aggregations
├── data/
│   └── sales-500.csv         # Sample source data
└── README.md
```

---

## Bronze Layer — Raw Ingestion

Ingests raw CSV data as-is into a Delta table using Databricks Autoloader (`cloudFiles`), with no transformation — single source of truth for raw data.

---

##  Silver Layer — Cleaning & Deduplication

Selects relevant columns and removes duplicate orders 

**Transformations applied:**
- Selected only business-relevant columns
- Deduplicated on `Order_ID` to ensure one record per order

---

##  Gold Layer — Business Aggregations

Three aggregated tables built on top of `sales_silver`, each serving a different business reporting need.


##  How to Run

1. Upload the pipeline files (`01_bronze.py`, `02_silver.py`, `03_gold.py`) to a Databricks Repo or Workspace folder.
2. Create a new **Delta Live Tables Pipeline** in Databricks:
   - Go to **Workflows → Delta Live Tables → Create Pipeline**
   - Set the source folder to the `pipelines/` directory
   - Choose target catalog/schema
3. Upload `data/sales-500.csv` to the Volume/path referenced in `01_bronze.py`.
4. Click **Start** to run the pipeline (Triggered or Continuous mode).
5. Query the resulting Gold tables from a SQL notebook or connect a BI tool (e.g. Databricks SQL Dashboard, Power BI).

---


##  Tech Stack
- **Databricks Delta Live Tables (DLT)**
- **PySpark** (`pyspark.sql.functions`)
- **Delta Lake** storage format
- **Medallion Architecture** (Bronze / Silver / Gold)

---

##  Notes
- Bronze layer code assumes Autoloader ingestion from a Databricks Volume — update the path to match your environment.
- Deduplication happens at Silver layer, so all Gold tables are safe from duplicate order counts.
- To enable time-based (daily/monthly) trend analysis, add the `Date` column back into `sales_silver`.
