WITH raw AS (
    SELECT
        "GeoName" AS region,
        "IndustrYDescription" AS industry,
        cast(nullif("DataValue", '') AS numeric) AS gdp_value,
        "Year" :: int AS year
    FROM
        {{ source ('bea', 'gdp') }}
)
SELECT
    *
FROM
    raw
WHERE
    gdp_value IS NOT NULL
