# 🚀 Crypto DBT Pipeline

This project is inspired by and adapted from [Aashay Bharadwaj's crypto_pipeline_project_dbt](https://github.com/AashayBharadwaj/crypto_pipeline_project_dbt).  
Special thanks to Aashay for making his code and design open-source and providing the foundation for this work.

---

## About This Project

**crypto_dbt_pipeline** is a crypto analytics pipeline that demonstrates the end-to-end workflow:
- **Extract:** Fetches cryptocurrency data from public APIs (e.g., CoinMarketCap).
- **Load:** Loads the data into a PostgreSQL database.
- **Transform:** Cleans and models data using [dbt](https://www.getdbt.com/).
- **Test:** Validates with built-in dbt tests.
- **Visualize:** Presents insights and data health in a Streamlit dashboard.

---

## Technologies Used

- **ETL:** Python (`requests`, `pandas`)
- **Database:** PostgreSQL (Supabase)
- **Data Modeling:** dbt
- **Testing:** dbt tests
- **Visualization:** Streamlit + Plotly

---

## Attribution

Parts of the data pipeline, model structure, and dashboard design are based on  
[Aashay Bharadwaj's crypto_pipeline_project_dbt](https://github.com/AashayBharadwaj/crypto_pipeline_project_dbt).

