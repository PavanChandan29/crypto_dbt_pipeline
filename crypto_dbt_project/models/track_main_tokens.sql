-- This model filters key metrics for AVAX, ETH, BTC, and SOL from crypto_raw

SELECT
    name,
    symbol,
    cmc_rank,
    "quote.USD.price" AS price_usd,
    "quote.USD.market_cap" AS market_cap
FROM {{ source('crypto_data', 'crypto_raw') }}
WHERE symbol in ('AVAX','ETH','BTC','SOL')
ORDER BY cmc_rank

