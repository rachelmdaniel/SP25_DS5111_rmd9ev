{{ config(materialized='table') }}

SELECT EN,DE
FROM DATA_SCIENCE.ABC1234_RAW.NUMBERS
