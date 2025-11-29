WITH raw AS (
    SELECT
        "GeoName" AS region,
        "Industry" AS industry,
        cast(nullif("DataValue", '') AS numeric) AS gdp_value,
        "TimePeriod" :: int AS year
    FROM
        {{ source ('bea', 'gdp') }}
)
SELECT
    *
FROM
    raw
WHERE
    gdp_value IS NOT NULL
