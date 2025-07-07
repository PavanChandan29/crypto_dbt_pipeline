# track_main_tokens

## Description
This model contains a curated list of main cryptocurrencies of interest, specifically focusing on BTC, ETH, SOL, and AVAX.

## Business Logic
- Filters cryptocurrencies where `symbol IN ('BTC', 'ETH', 'SOL', 'AVAX')`
- Orders results by `cmc_rank`
- Provides focused view of key cryptocurrencies for tracking

## Source
- **Table**: `crypto_raw`
- **Schema**: `public`
- **Update Frequency**: Hourly

## Columns

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| name | string | Full name of the cryptocurrency | "Bitcoin" |
| symbol | string | Trading symbol | "BTC" |
| cmc_rank | integer | CoinMarketCap ranking | 1 |
| price_usd | decimal | Current price in USD | 45000.00 |
| market_cap | decimal | Market capitalization in USD | 850000000000 |

## Included Cryptocurrencies

| Symbol | Name | Category |
|--------|------|----------|
| BTC | Bitcoin | Store of Value |
| ETH | Ethereum | Smart Contract Platform |
| SOL | Solana | Smart Contract Platform |
| AVAX | Avalanche | Smart Contract Platform |

## Data Quality
- **Tests**: not_null, unique, accepted_values
- **Expected Symbols**: BTC, ETH, SOL, AVAX only

## Usage Examples

### Get All Main Tokens
```sql
SELECT * 
FROM {{ ref('track_main_tokens') }}
ORDER BY market_cap DESC;
```

### Compare Market Caps
```sql
SELECT 
    symbol,
    name,
    market_cap,
    ROUND(market_cap / SUM(market_cap) OVER() * 100, 2) as market_share_percent
FROM {{ ref('track_main_tokens') }}
ORDER BY market_cap DESC;
```

### Price Analysis
```sql
SELECT 
    symbol,
    price_usd,
    CASE 
        WHEN price_usd >= 1000 THEN 'High Price'
        WHEN price_usd >= 100 THEN 'Medium Price'
        ELSE 'Low Price'
    END as price_category
FROM {{ ref('track_main_tokens') }}
ORDER BY price_usd DESC;
```

## Dependencies
- `crypto_raw` (source table)

## Related Models
- `crypto_top10` - Parent model containing all top 10 cryptocurrencies

## Business Use Cases
- **Portfolio Tracking**: Monitor key cryptocurrencies
- **Market Analysis**: Focus on major players
- **Risk Assessment**: Track market leaders
- **Performance Comparison**: Compare top tokens 