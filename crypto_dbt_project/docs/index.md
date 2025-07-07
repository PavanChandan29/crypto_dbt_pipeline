# Crypto Pipeline Documentation

## Overview
This dbt project transforms cryptocurrency data from CoinMarketCap API into analytics-ready models for tracking and analyzing the top cryptocurrencies.

## Project Structure
```
crypto_dbt_project/
├── models/          # SQL models
├── docs/           # Documentation
├── tests/          # Custom tests
└── dbt_project.yml # Project configuration
```

## Data Sources

### crypto_raw
- **Source**: CoinMarketCap API
- **Update Frequency**: Hourly via Python script
- **Description**: Raw cryptocurrency data including prices, market cap, and rankings

## Models

### crypto_top10
- **Description**: Top 10 cryptocurrencies by market cap
- **Source**: `crypto_raw` table
- **Business Logic**: Filters cryptocurrencies where `cmc_rank <= 10`
- **Columns**:
  - `name`: Cryptocurrency name
  - `symbol`: Cryptocurrency symbol (BTC, ETH, etc.)
  - `cmc_rank`: CoinMarketCap ranking (1-10)
  - `price_usd`: Current price in USD
  - `market_cap`: Market capitalization in USD

### track_main_tokens
- **Description**: Main tokens of interest for tracking
- **Source**: `crypto_raw` table
- **Business Logic**: Filters specific tokens (BTC, ETH, SOL, AVAX)
- **Columns**: Same as crypto_top10 but only for selected tokens

## Key Metrics

### Market Cap
- **Definition**: Total value of all coins in circulation
- **Unit**: USD
- **Use Case**: Market dominance analysis

### Price (USD)
- **Definition**: Current price per coin in USD
- **Unit**: USD
- **Use Case**: Price tracking and analysis

### CMC Rank
- **Definition**: CoinMarketCap ranking by market cap
- **Unit**: Integer (1 = highest market cap)
- **Use Case**: Market position analysis

## Data Quality

### Tests Implemented
- **not_null**: Ensures required fields are not empty
- **accepted_values**: Validates symbols are in expected list
- **unique**: Ensures no duplicate symbols

### Data Freshness
- Data is updated hourly from CoinMarketCap API
- Raw data is stored in PostgreSQL database

## Usage Examples

### Query Top 10 Cryptocurrencies
```sql
SELECT * FROM {{ ref('crypto_top10') }}
ORDER BY cmc_rank;
```

### Get Main Tokens Only
```sql
SELECT * FROM {{ ref('track_main_tokens') }}
ORDER BY market_cap DESC;
```

## Maintenance

### Running Tests
```bash
dbt test
```

### Running Models
```bash
dbt run
```

### Generating Documentation
```bash
dbt docs generate
dbt docs serve
```

## Contact
For questions about this dbt project, refer to the project README or contact the data team. 