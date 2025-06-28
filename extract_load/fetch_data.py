import requests
import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

#Load API key
load_dotenv()
api_key = os.getenv("CMC_API_KEY")


headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key
}

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

#Optional parameters

params = {
    'start': '1',
    'limit': '50',
    'convert': 'USD'
}

#Get the API response
response = requests.get(url,headers=headers, params=params)
data = response.json()['data']

#Convert data to a dataframe

df = pd.json_normalize(data)

#Set up database connection

engine = create_engine ("postgresql://postgres:12345678@localhost:5432/crypto_data")

#load data into PostGres
df.to_sql("crypto_raw", engine, if_exists="replace", index = False)

print("data loaded successfully. ")