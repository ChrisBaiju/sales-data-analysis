# 📊 Sales Data Analysis

A data analytics project using **Python + SQL**: loads 250 sales records into SQLite, runs analytical queries, and generates a formatted business report.

## What's inside

| File | Purpose |
|------|---------|
| `data/sales.csv` | 250 sample sales records (product, category, region, quantity, price) |
| `analysis.sql` | 6 analytical SQL queries |
| `analyze.py` | Loads the CSV into SQLite and prints a full report |

## Queries answered

- 💰 Total revenue
- 🏷️ Revenue by category
- 🏆 Top 5 products by revenue
- 📈 Monthly revenue trend
- 🗺️ Revenue by region (+ average order value)
- 🥇 Best-selling product per category (window functions!)

## Usage

```bash
python analyze.py
```

```
====================================================
               📊 SALES ANALYSIS REPORT
====================================================
Loaded 250 orders.

▶ Total revenue
  total_revenue
  ----------------------------------------------
  24532.5
...
```

## What I learned

- SQL aggregations: `GROUP BY`, `SUM`, `AVG`
- Window functions (`ROW_NUMBER() OVER (PARTITION BY ...)`)
- Loading CSV data into SQLite with Python
- Turning raw data into a readable report

## Tech

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
