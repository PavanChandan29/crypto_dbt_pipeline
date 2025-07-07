# Crypto Data Dictionary

## Source: crypto_raw

### Overview
Raw cryptocurrency data from CoinMarketCap API, containing comprehensive information about cryptocurrencies including prices, market metrics, and rankings.

### Data Source Details
- **API**: CoinMarketCap Pro API
- **Endpoint**: `/v1/cryptocurrency/listings/latest`
- **Update Frequency**: Hourly
- **Data Format**: JSON → PostgreSQL

### Schema

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| name | string | Full name of the cryptocurrency | "Bitcoin" |
| symbol | string | Trading symbol | "BTC" |
| cmc_rank | integer | CoinMarketCap ranking by market cap | 1 |
| quote.USD.price | decimal | Current price in USD | 45000.00 |
| quote.USD.market_cap | decimal | Market capitalization in USD | 850000000000 |
| quote.USD.volume_24h | decimal | 24-hour trading volume | 25000000000 |
| quote.USD.percent_change_1h | decimal | 1-hour price change % | 2.5 |
| quote.USD.percent_change_24h | decimal | 24-hour price change % | -1.2 |
| quote.USD.percent_change_7d | decimal | 7-day price change % | 5.8 |
| circulating_supply | decimal | Number of coins in circulation | 19500000 |
| total_supply | decimal | Total number of coins created | 21000000 |
| max_supply | decimal | Maximum number of coins possible | 21000000 |
| last_updated | timestamp | Last update timestamp | 2024-01-15 10:30:00 |

### Data Quality Notes
- **Price Precision**: Prices are typically accurate to 2-8 decimal places
- **Market Cap**: Calculated as price × circulating supply
- **Ranking**: Updated in real-time based on market cap
- **Missing Values**: Some fields may be null for newer cryptocurrencies

### API Parameters Used
- `start`: 1 (start from first record)
- `limit`: 50 (get top 50 cryptocurrencies)
- `convert`: USD (prices in USD)

### Data Transformation
- JSON data is flattened using pandas
- Column names are preserved from API response
- Data is loaded into PostgreSQL using SQLAlchemy

### Business Rules
- Only cryptocurrencies with valid market cap are included
- Rankings are based on market capitalization
- Prices are in USD only
- Data is refreshed hourly to maintain accuracy

### Known Limitations
- API has rate limits (10,000 calls per month on free tier)
- Historical data not included in this endpoint
- Limited to top 50 cryptocurrencies by default 