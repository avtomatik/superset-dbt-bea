WITH base AS (
    SELECT
        *
    FROM
        { { ref ('stg_bea_gdp') } }
),
agg AS (
    SELECT
        year,
        industry,
        sum(gdp_value) AS gdp_total
    FROM
        base
    GROUP BY
        year,
        industry
)
SELECT
    *
FROM
    agg