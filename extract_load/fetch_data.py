import os
import requests
import pandas as pd
from sqlalchemy import create_engine

def get_secrets():
    """
    Dynamically load credentials (API key, DB URL) based on environment:
    - If running as a Streamlit app (web/cloud), load from Streamlit's secrets.
    - If running as a local script, load from .env file using os.getenv().
    """
    try:
        import streamlit as st
        # Detect Streamlit server by env var or Streamlit's own attribute
        if os.getenv('STREAMLIT_SERVER_RUNNING') or getattr(st, "_is_running_with_streamlit", False):
            print("🔵 [LOG] Using Streamlit secrets (cloud/Git/Streamlit deployment detected)")
            db_url = st.secrets["DB_URL"]
            api_key = st.secrets["CMC_API_KEY"]
            return db_url, api_key
    except ImportError:
        pass

    # If not in Streamlit, assume local development with .env file
    from dotenv import load_dotenv
    load_dotenv()
    print("🟢 [LOG] Using .env file (local environment detected)")
    db_url = os.getenv("DB_URL")
    api_key = os.getenv("CMC_API_KEY")
    return db_url, api_key

# --- MAIN SCRIPT STARTS HERE ---

# 1. Load secrets depending on the environment
db_url, api_key = get_secrets()

# 2. Set up API request to CoinMarketCap for latest cryptocurrency data
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key  # API key for authentication
}
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
params = {
    'start': '1',      # Start from the top coin (Bitcoin)
    'limit': '50',     # Get data for the top 50 coins
    'convert': 'USD'   # All prices in USD
}

# 3. Fetch the crypto data from CoinMarketCap API
response = requests.get(url, headers=headers, params=params)
data = response.json()['data']  # Extract only the 'data' part from the API response

# 4. Convert the crypto data (list of dictionaries) into a Pandas DataFrame for easier analysis
df = pd.json_normalize(data)

# 5. Set up a connection to the Postgres database using SQLAlchemy's engine
# The "engine" is like a bridge between Python and your database.
# It lets you send/read data to/from the database using Python code instead of manual SQL commands.
engine = create_engine(db_url)

# 6. Save the DataFrame as a SQL table in the database
# This will create or replace a table named "crypto_raw" and load the crypto data into it.
df.to_sql("crypto_raw", engine, if_exists="replace", index=False)

print("✅ Data loaded successfully.")

