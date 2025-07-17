-- What was the growth in sales between 2022 and 2023?
-- Include all orders in the calculation, even if they were returned or canceled.
-- Answer: 90.7%
WITH year_sales AS (
    SELECT
        YEAR(o.created_at) AS "Year",
        SUM(oi.sale_price) AS "Total Sales"
    FROM
        orders o
    INNER JOIN
        order_items oi ON oi.order_id = o.order_id
    WHERE
        "Year" IN (2022, 2023)
    GROUP BY
        "Year"
)

SELECT
    ROUND(
        (MAX(CASE WHEN "Year" = 2023 THEN "Total Sales" END) -
         MAX(CASE WHEN "Year" = 2022 THEN "Total Sales" END))
        /MAX(CASE WHEN "Year" = 2022 THEN "Total Sales" END) * 100, 1
    ) AS "% Growth (2022 to 2023)"
    
FROM year_sales
;

-- Generate a line chart showing sales by year.
SELECT YEAR(o.created_at) AS "Year", SUM(oi.sale_price) AS Sales

FROM orders o
INNER JOIN order_items oi ON oi.order_id = o.order_id

WHERE "Year" != 2024
GROUP BY "Year"
ORDER BY "Year";

-- How many products are we losing money on?
-- In other words, the unit cost is higher than the price. 
-- Answer: 0
SELECT COUNT_IF(unit_cost > retail_price)
FROM products;

-- How many products deviate from our cost-plus pricing policy?
-- * We expect to markup each product by at least 50% above cost (i.e., "cost-plus").
SELECT COUNT(*)
FROM products
WHERE retail_price < unit_cost * 1.5;
