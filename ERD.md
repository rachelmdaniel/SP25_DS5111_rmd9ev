```mermaid
erDiagram

    STOCK ||--o{ AVERAGE-GAIN : "has"
    STOCK ||--o{ TOTAL-GAIN : "has"
    STOCK ||--o{ BIGGEST-GAINER-PER-DAY : "recorded as"
    STOCK ||--o{ SMALLEST-GAINER-PER-DAY : "experiences"
    STOCK ||--o{ MARKET-CORRELATION : "correlates with"
     STOCK ||--o{ PRICE-DISTRIBUTION : "follows"

    STOCK {
        string symbol
    }

    AVERAGE-GAIN {
        string symbol
        float average_percent_increase
    }

    TOTAL-GAIN {
        string symbol
        float total_sum_increase
    }

    BIGGEST-GAINER-PER-DAY {
        date date
        string symbol
        float price_change
        int count
    }

    SMALLEST-GAINER-PER-DAY  {
        date date
        string symbol
        float price_change
        int count
    }

    MARKET-CORRELATION {
        string symbol
        string correlation_type
    }

    PRICE-DISTRIBUTION {
        string symbol
        date date
        float open_price
        float close_price
        float high_price
        float low_price
        float volume
    }
```

* Description of design:
    - I designed my ER diagram this way because I am looking for the best performing, yet stable stocks. I would like to see how much the stocks increase on average and 
      how much they increase in total over time. I am also interested in which stock gains the most each day and which stock has the least amount of change per day to compare.
      It would also be interesting to see if there is a stock that is positively correlated with the overall market, yet is very stable and experiences little changes. 
      Finally, it would be very helpful to visualize price distributions, while also taking into account closing, opening, highest, and lowest prices along with volume.



* Use Cases:
    - Picking stocks that gain the most on average or have the largest total gain.
    - Picking stocks that constantly gain the most or experience the smallest increases, but appear often so they might be the most stable
    - Percent of stocks that are correlated with overall market to understand if it is helpful to choose stocks that are correlated with it
    - Look at the distribution of prices to identify stocks that commonly perform well.
