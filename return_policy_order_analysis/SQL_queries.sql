/* What % of orders were returned? (This is the "return rate".)
An order was returned, if it has a "returned" status.
Round to one decimal place. For example, 13.76% should be entered as 13.8.
Answer: 10.0 or 10% */

SELECT status, COUNT(order_id) AS Num_of_Returned_Orders, ROUND((COUNT(order_id) / 124877) * 100, 1) AS Return_Rate
FROM orders
WHERE status = 'Returned'
GROUP BY status;

/* Has the return rate increased between 2019 and 2023? Yes */
SELECT 
    EXTRACT(YEAR FROM created_at) AS "Year",
    COUNT(order_id) AS Total_Orders,
    COUNT(CASE WHEN status = 'Returned' THEN 1 END) AS Returned_Orders,
    ROUND(Returned_Orders / COUNT(order_id) * 100, 1) AS Return_Rate
FROM orders
GROUP BY "Year"
ORDER BY "Year";

/* Which three product categories have the highest return rates? Pants, Leggings, Socks & Hosiery */
SELECT
p.category,
COUNT(ot.order_id) AS Total_Orders,
COUNT(CASE WHEN o.status = 'Returned' THEN 1 END) AS Returned_Orders,
ROUND((Returned_Orders / Total_Orders) * 100, 1) AS Return_Rate


FROM products p
INNER JOIN order_items ot ON p.product_id = ot.product_id
INNER JOIN orders o ON ot.order_id = o.order_id

GROUP BY p.category
ORDER BY Return_Rate DESC;

/* How much revenue was lost on returns? $1,088,903.82 */
SELECT
SUM(ot.sale_price) AS Lost_Revenue

FROM order_items ot
INNER JOIN orders o 
ON ot.order_id = o.order_id

WHERE o.status = 'Returned';
