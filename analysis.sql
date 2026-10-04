-- Total revenue
SELECT ROUND(SUM(quantity * unit_price), 2) AS total_revenue
FROM sales;

-- Revenue by category
SELECT category,
       COUNT(*) AS orders,
       ROUND(SUM(quantity * unit_price), 2) AS revenue
FROM sales
GROUP BY category
ORDER BY revenue DESC;

-- Top 5 products by revenue
SELECT product,
       SUM(quantity) AS units_sold,
       ROUND(SUM(quantity * unit_price), 2) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC
LIMIT 5;

-- Monthly revenue trend
SELECT substr(date, 1, 7) AS month,
       ROUND(SUM(quantity * unit_price), 2) AS revenue
FROM sales
GROUP BY month
ORDER BY month;

-- Revenue by region
SELECT region,
       ROUND(SUM(quantity * unit_price), 2) AS revenue,
       ROUND(AVG(quantity * unit_price), 2) AS avg_order_value
FROM sales
GROUP BY region
ORDER BY revenue DESC;

-- Best-selling product per category
SELECT category, product, revenue FROM (
    SELECT category, product,
           ROUND(SUM(quantity * unit_price), 2) AS revenue,
           ROW_NUMBER() OVER (PARTITION BY category ORDER BY SUM(quantity * unit_price) DESC) AS rn
    FROM sales
    GROUP BY category, product
)
WHERE rn = 1;
