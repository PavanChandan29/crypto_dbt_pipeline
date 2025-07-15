<<<<<<< HEAD
# 🚀 dbt-Powered Crypto Data Dashboard

A fully integrated crypto analytics dashboard powered by **dbt**, **PostgreSQL**, and **Streamlit**. This project demonstrates how raw API data can be transformed into reliable insights using modern data stack principles.

![Dashboard Preview](dbt_logo.jpg)

---

## 📌 Project Overview

This project includes the full data lifecycle:
- **Extract**: Crypto data fetched via API (e.g., CoinMarketCap)
- **Load**: Data loaded into PostgreSQL using `pandas.to_sql()`
- **Transform**: Cleaned and modeled using **dbt**
- **Test**: Data validated using built-in **dbt tests**
- **Visualize**: Front-end dashboard built with **Streamlit**

---

## 📊 Dashboard Features

- **Top 10 Cryptocurrencies** by market cap (log scale bar chart + pie chart)
- **Tracked Tokens View**: Detailed table for AVAX, BTC, ETH, SOL
- **Database Explorer**: List of available tables and views
- **Test Results Viewer**: Run and display dbt test output inside UI
- **Data Flow Tab**: Visual representation of the pipeline steps

---

## 🧱 Technologies Used

| Layer         | Tool            |
|---------------|------------------|
| **ETL**        | Python (pandas, requests) |
| **Database**   | PostgreSQL       |
| **Transform**  | dbt              |
| **Testing**    | dbt tests        |
| **Dashboard**  | Streamlit + Plotly |

---

## 🧪 Data Tests Implemented

- `not_null` on `market_cap`
- `accepted_values` on `symbol` fields (for tracked tokens and top 10)

---

## 🚀 Getting Started

### 1. Clone this Repo
```bash
git clone https://github.com/AashayBharadwaj/crypto_pipeline_project_dbt.git
cd crypto_pipeline_project_dbt
=======
# crypto_dbt_pipeline
>>>>>>> 367abac6fc72a7ef2243c690f64c5291785c89b6
