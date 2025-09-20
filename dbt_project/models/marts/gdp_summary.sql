with
    base
    as
    (

        select *
        from {{ ref
    ('stg_bea_gdp') }}

),

agg as
(

    select
    year,
    industry,
    sum(gdp_value) as gdp_total
from base
group by year, industry

)

select *
from agg
