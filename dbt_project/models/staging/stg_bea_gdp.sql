with
    raw
    as
    (

        select
            "GeoName" as region,
            "Industry" as industry,
            cast(nullif("DataValue", '') as numeric) as gdp_value,
            "TimePeriod"::int as year
        from {{ source
    ('bea', 'gdp') }}

)

select *
from raw
where gdp_value is not null
