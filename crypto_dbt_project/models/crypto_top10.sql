
SELECT
    name,
    symbol,
    cmc_rank,
    "quote.USD.price" AS price_usd,
    "quote.USD.market_cap" AS market_cap
FROM {{ source('crypto_data', 'crypto_raw') }}
WHERE cmc_rank <= 10
ORDER BY cmc_rank

