{{ config(materialized='table') }}

WITH combined_data AS (
    SELECT
        'ACN' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.ACN_HIST
    UNION ALL
    SELECT
        'AMZN' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.AMZN_HIST
    UNION ALL
    SELECT
        'APOG' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.APOG_HIST
    UNION ALL
    SELECT
        'AUR' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.AUR_HIST
    UNION ALL
    SELECT
        'BABA' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.BABA_HIST
    UNION ALL
    SELECT
        'BEKE' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.BEKE_HIST
    UNION ALL
    SELECT
        'BILI' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.BILI_HIST
    UNION ALL
    SELECT
        'BTE' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.BTE_HIST
    UNION ALL
    SELECT
        'FUTU' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.FUTU_HIST
    UNION ALL
    SELECT
        'HAL' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.HAL_HIST
    UNION ALL
    SELECT
        'HBM' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.HBM_HIST
    UNION ALL
    SELECT
        'INTC' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.INTC_HIST
    UNION ALL
    SELECT
        'IQ' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.IQ_HIST
    UNION ALL
    SELECT
        'JBLU' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.JBLU_HIST
    UNION ALL
    SELECT
        'JD' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.JD_HIST
    UNION ALL
    SELECT
        'LI' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.LI_HIST
    UNION ALL
    SELECT
        'NIO' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.NIO_HIST
    UNION ALL
    SELECT
        'NKE' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.NKE_HIST
    UNION ALL
    SELECT
        'OXY' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.OXY_HIST
    UNION ALL
    SELECT
        'PBF' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.PBF_HIST
    UNION ALL
    SELECT
        'PDD' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.PDD_HIST
    UNION ALL
    SELECT
        'PYPL' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.PYPL_HIST
    UNION ALL
    SELECT
        'RIG' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.RIG_HIST
    UNION ALL
    SELECT
        'RKLB' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.RKLB_HIST
    UNION ALL
    SELECT
        'SLB' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.SLB_HIST
    UNION ALL
    SELECT
        'TSLA' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.TSLA_HIST
    UNION ALL
    SELECT
        'WB' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.WB_HIST
    UNION ALL
    SELECT
        'XPEV' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.XPEV_HIST
    UNION ALL
    SELECT
        'YMM' AS symbol, date, open, close, high, low, volume FROM DATA_SCIENCE.STOCKS.YMM_HIST
),

final_table AS (
    SELECT
        symbol,
        date,
        open AS open_price,
        close AS close_price,
        high AS high_price,
        low AS low_price,
        volume
    FROM combined_data
)

SELECT * FROM final_table
