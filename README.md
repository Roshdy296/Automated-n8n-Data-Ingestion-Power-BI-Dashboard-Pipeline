# 🔄 Automated n8n Data Ingestion & Power BI Dashboard Pipeline

An automated ETL workflow leveraging n8n cloud orchestration to ingest, clean, and consolidate dynamic multi-table Excel datasets directly into a centralized Power BI reporting environment.

## 📌 Project Overview
Designed to eliminate manual reporting friction, this pipeline automates data ingestion whenever raw files are received, transforming raw inputs into unified datasets optimized for Power BI visualization and DAX measures.

### Key Features
* **Zero-Touch ETL Orchestration:** Automated triggers handle multi-source Excel ingestion and data cleaning without manual script execution.
* **Multi-Table Consolidation:** Merges disparate operational sheets into clean, structured outputs.
* **Power BI Dashboards:** Implements interactive visualization models backed by dynamic DAX measures for operational KPI tracking.

---

## 🛠️ Tech Stack
* **Workflow Automation:** n8n Cloud / Self-hosted n8n
* **Data Transformation:** Python / JavaScript nodes within n8n, Excel (`openpyxl`, `pandas`)
* **Business Intelligence:** Power BI Desktop, DAX

---

## 🚀 Workflow Architecture

1. **Trigger:** Webhook or file-drop monitoring for incoming raw Excel reports.
2. **Transform:** n8n execution node cleans, validates, and joins multi-table records.
3. **Load:** Automatically saves consolidated datasets to the designated local or cloud directory mapped to Power BI.

---

## 📂 Repository Structure

```text
├── workflows/
│   └── n8n_pipeline_config.json # Exported n8n automation workflow template
├── scripts/
│   └── data_cleaner.py          # Helper data transformation script
├── dashboard/
│   └── operational_kpis.pbix    # Power BI dashboard template
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
