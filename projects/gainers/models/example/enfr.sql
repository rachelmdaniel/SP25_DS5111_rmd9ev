{{ config(materialized='table') }}

SELECT EN,FR
FROM DATA_SCIENCE.ABC1234_RAW.NUMBERS
