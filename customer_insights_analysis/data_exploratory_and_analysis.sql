-- Data Exploration

-- How many known users do we have? (Only looking at those within the users table)
-- Answer: 100,000
SELECT COUNT(*), COUNT(DISTINCT user_id)
FROM users;

-- In what country do we have the most known users?
-- Answer: China
SELECT country, COUNT(user_id) AS "#_of_Users"
FROM users
GROUP BY country
ORDER BY "#_of_Users" DESC
LIMIT 1;

-- What % of all known users are from that particular country?
-- Answer: 34.2%
SELECT
    country,
    COUNT(user_id) AS "#_of_Users",
    ROUND((COUNT(user_id) / 100000) * 100, 1) AS "%_of_Known_Users"
FROM users
GROUP BY country
ORDER BY "#_of_Users" DESC
LIMIT 1;

-- What % of known US users are from Wisconsin?
-- Answer: 1.2%
SELECT 
    state,
    COUNT(CASE WHEN country = 'United States' THEN 1 END) AS "#_of_Users",
    SUM("#_of_Users") OVER () AS Total_US_Users,
    ROUND(("#_of_Users" / Total_US_Users) * 100, 1) AS "%_of_US_Users"
FROM users
WHERE country = 'United States'
GROUP BY state
ORDER BY state DESC;

-- What is the average age of our known users?
-- Answer: 40.9
SELECT ROUND(SUM(age) / COUNT(user_id), 1) AS Avg_Age
FROM users;

-- What % of our known users are female?
-- Answer: 50.0
SELECT
    COUNT(CASE WHEN gender = 'F' THEN 1 END) AS Female_Users,
    COUNT(user_id) AS Total_Users,
    ROUND((Female_Users / Total_Users) * 100, 1) AS "%_of_Female Users"
FROM users;

-- What was the largest traffic source of known users?
-- Answer: Search

SELECT traffic_source, COUNT(user_id) AS "#_of_Known_Users"
FROM users
GROUP BY traffic_source
ORDER BY "#_of_Known_Users" DESC;

-- How many new users registered in 2023?
-- Answer: 18,653
SELECT 
    COUNT(CASE WHEN YEAR(created_at) = '2023' THEN 1 END) AS New_Users_2023
FROM users;

-- Answering The Business Questions

-- What % of registered (or "known") users had a purchase?
-- Answer: 79.9%
SELECT
    COUNT(DISTINCT o.user_id) AS "#_of_User_Purchases",
    (SELECT COUNT(*) FROM users) AS "#_of_Registered_Users",
    ROUND(("#_of_User_Purchases" / "#_of_Registered_Users") * 100, 1) AS "%_of_User_Purchases"
FROM users u
INNER JOIN orders o
ON u.user_id = o.user_id;

-- Who were our highest spending customers? (Select three.)
-- Answer: 99148, 82305, 48605
SELECT
    u.user_id,
    SUM(oi.sale_price) AS Spending_Total
FROM users u
INNER JOIN orders o ON u.user_id = o.user_id
INNER JOIN order_items oi ON o.order_id = oi.order_id

GROUP BY u.user_id
ORDER BY Spending_Total DESC
LIMIT 3;

-- Are males or females spending more per order?
-- Answer: Male ($91.4); Female ($81.1)
SELECT
    u.gender,
    ROUND(SUM(oi.sale_price) / COUNT(DISTINCT o.order_id), 1) AS Spending_Total
FROM users u
INNER JOIN orders o ON u.user_id = o.user_id
INNER JOIN order_items oi ON o.order_id = oi.order_id

WHERE u.gender IN ('M', 'F')
GROUP BY u.gender;

-- What demographic segments spent the most total money? (Choose Two)
/* Customers should be segmented by generation (see below) AND gender:

Silent Generation: 78 or older.
Baby Boomer: 58 to 77.
Gen X: 42 to 57.
Millennial: 26 to 41.
Gen Z: 10 to 25.
Gen Alpha: 9 or younger.

Include all orders in the calculation, even if they were returned or canceled. 
Answer: Millennial Men and Gen X Men */

SELECT
CASE
    WHEN u.age >= 78 THEN 'Silent Generation'
    WHEN u.age BETWEEN 58 AND 77 THEN 'Baby Boomer'
    WHEN u.age BETWEEN 42 AND 57 THEN 'Gen X'
    WHEN u.age BETWEEN 26 AND 41 THEN 'Millennial'
    WHEN u.age BETWEEN 10 AND 25 THEN 'Gen Z'
    ELSE 'Gen Alpha'
END AS Age_Demographics,
u.gender,
SUM(oi.sale_price) AS Spending_Total

FROM users u
INNER JOIN orders o ON u.user_id = o.user_id
INNER JOIN order_items oi ON o.order_id = oi.order_id

GROUP BY Age_Demographics, u.gender
ORDER BY Spending_Total DESC;

-- What demographic segments have the most orders? (Choose two.)
-- Use the segments mentioned in the previous question.
-- Answer: Millennial Women and Gen X Women

SELECT
CASE
    WHEN u.age >= 78 THEN 'Silent Generation'
    WHEN u.age BETWEEN 58 AND 77 THEN 'Baby Boomer'
    WHEN u.age BETWEEN 42 AND 57 THEN 'Gen X'
    WHEN u.age BETWEEN 26 AND 41 THEN 'Millennial'
    WHEN u.age BETWEEN 10 AND 25 THEN 'Gen Z'
    ELSE 'Gen Alpha'
END AS Age_Demographics,
u.gender,
COUNT(DISTINCT o.order_id) AS "#_of_Orders"

FROM users u
INNER JOIN orders o 
ON u.user_id = o.user_id

GROUP BY Age_Demographics, u.gender
ORDER BY "#_of_Orders" DESC;

-- Within each segment, which two product categories are most popular? 
-- Measure popularity by the number of orders that include that product category.
-- Include all orders in the calculation, even if they were returned or canceled

WITH CategoryCounts AS (
  SELECT
    CASE
      WHEN u.age >= 78 THEN 'Silent Generation'
      WHEN u.age BETWEEN 58 AND 77 THEN 'Baby Boomer'
      WHEN u.age BETWEEN 42 AND 57 THEN 'Gen X'
      WHEN u.age BETWEEN 26 AND 41 THEN 'Millennial'
      WHEN u.age BETWEEN 10 AND 25 THEN 'Gen Z'
      ELSE 'Gen Alpha'
    END AS Age_Demographics,
    u.gender,
    p.category,
    COUNT(*) AS Category_Count,
    ROW_NUMBER() OVER (
      PARTITION BY 
        CASE
          WHEN u.age >= 78 THEN 'Silent Generation'
          WHEN u.age BETWEEN 58 AND 77 THEN 'Baby Boomer'
          WHEN u.age BETWEEN 42 AND 57 THEN 'Gen X'
          WHEN u.age BETWEEN 26 AND 41 THEN 'Millennial'
          WHEN u.age BETWEEN 10 AND 25 THEN 'Gen Z'
          ELSE 'Gen Alpha'
        END,
        u.gender
      ORDER BY COUNT(*) DESC
    ) AS rn
  FROM users u
  INNER JOIN orders o ON u.user_id = o.user_id
  INNER JOIN order_items oi ON oi.order_id = o.order_id
  INNER JOIN products p ON p.product_id = oi.product_id
  GROUP BY Age_Demographics, u.gender, p.category
)

SELECT
  Age_Demographics,
  gender,
  category,
  Category_Count
FROM CategoryCounts
WHERE rn <= 2
ORDER BY Age_Demographics, gender, Category_Count DESC;
