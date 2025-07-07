# crypto_top10

## Description
This model contains the top 10 cryptocurrencies by market capitalization, filtered from the raw CoinMarketCap data.

## Business Logic
- Filters cryptocurrencies where `cmc_rank <= 10`
- Orders results by `cmc_rank` (1 = highest market cap)
- Includes key metrics: name, symbol, rank, price, and market cap

## Source
- **Table**: `crypto_raw`
- **Schema**: `public`
- **Update Frequency**: Hourly

## Columns

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| name | string | Full name of the cryptocurrency | "Bitcoin" |
| symbol | string | Trading symbol | "BTC" |
| cmc_rank | integer | CoinMarketCap ranking (1-10) | 1 |
| price_usd | decimal | Current price in USD | 45000.00 |
| market_cap | decimal | Market capitalization in USD | 850000000000 |

## Data Quality
- **Tests**: not_null, unique, accepted_values
- **Expected Symbols**: BTC, ETH, SOL, AVAX, USDT, USDC, XRP, BNB, ADA, DOGE

## Usage Examples

### Get Top 5 Cryptocurrencies
```sql
SELECT name, symbol, market_cap 
FROM {{ ref('crypto_top10') }}
WHERE cmc_rank <= 5
ORDER BY cmc_rank;
```

### Find Specific Cryptocurrency
```sql
SELECT * 
FROM {{ ref('crypto_top10') }}
WHERE symbol = 'BTC';
```

### Market Cap Analysis
```sql
SELECT 
    symbol,
    market_cap,
    ROUND(market_cap / SUM(market_cap) OVER() * 100, 2) as market_share_percent
FROM {{ ref('crypto_top10') }}
ORDER BY market_cap DESC;
```

## Dependencies
- `crypto_raw` (source table)

## Related Models
- `track_main_tokens` - Subset of main tokens from this model 