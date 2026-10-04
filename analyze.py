#!/usr/bin/env python3
"""
Sales Data Analysis
-------------------
Loads sales.csv into SQLite, runs the queries in analysis.sql,
and prints a formatted business report.

Usage:
    python analyze.py
"""

import sqlite3
from pathlib import Path

BASE = Path(__file__).parent


def load_data(conn: sqlite3.Connection):
    """Create the sales table and import the CSV."""
    import csv

    conn.execute("DROP TABLE IF EXISTS sales")
    conn.execute(
        """CREATE TABLE sales (
               order_id INTEGER,
               date TEXT,
               product TEXT,
               category TEXT,
               region TEXT,
               quantity INTEGER,
               unit_price REAL
           )"""
    )
    with open(BASE / "data" / "sales.csv", newline="") as f:
        rows = list(csv.DictReader(f))
    conn.executemany(
        "INSERT INTO sales VALUES (:order_id, :date, :product, :category,"
        " :region, :quantity, :unit_price)",
        rows,
    )
    conn.commit()
    return len(rows)


def run_queries(conn: sqlite3.Connection):
    """Split analysis.sql into statements and run each one."""
    sql = (BASE / "analysis.sql").read_text()
    statements = [s.strip() for s in sql.split(";") if s.strip()]
    results = []
    for stmt in statements:
        # Use the first comment line as the report heading
        lines = stmt.splitlines()
        heading = next(
            (ln.lstrip("- ").strip() for ln in lines if ln.strip().startswith("--")),
            "Query",
        )
        query = "\n".join(ln for ln in lines if not ln.strip().startswith("--"))
        cur = conn.execute(query)
        results.append((heading, [d[0] for d in cur.description], cur.fetchall()))
    return results


def print_report(results):
    print("=" * 52)
    print("📊 SALES ANALYSIS REPORT".center(52))
    print("=" * 52)
    for heading, columns, rows in results:
        print(f"\n▶ {heading}")
        print("  " + " | ".join(columns))
        print("  " + "-" * 46)
        for row in rows:
            print("  " + " | ".join(str(v) for v in row))
    print("\n" + "=" * 52)


def main():
    conn = sqlite3.connect(":memory:")
    count = load_data(conn)
    print(f"Loaded {count} orders.\n")
    results = run_queries(conn)
    print_report(results)
    conn.close()


if __name__ == "__main__":
    main()
