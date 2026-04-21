# Sales Data Cleaner & Monthly Report

Python pipeline for sales data cleaning and automated monthly reports with professional Excel formatting. Built for small businesses that receive messy CSVs from their platforms (Shopify, WooCommerce, ERP exports) and need fast monthly insights.

## Problem it solves

Real sales data arrives messy: duplicates from sync errors, dates in inconsistent formats (`2024-01-15`, `15/01/2024`, `01-15-2024`), category variations with capitalization and spacing issues (`Electronics`, `ELECTRONICS`, `electronics `), and null values. Cleaning this manually in Excel takes hours every month.

This pipeline does it in seconds.

## What it does

1. **Loads** any sales CSV with columns: date, product, category, quantity, unit price, customer
2. **Cleans**: removes duplicates, normalizes categories, parses mixed-format dates, imputes nulls with median
3. **Analyzes**: calculates revenue, groups by month and category, identifies top products
4. **Reports**: generates stacked bar chart (PNG) and Excel with 3 sheets (clean data, monthly summary, top products)
5. **Summarizes**: prints key metrics to console (total revenue, average ticket, leading category)

## Professional Excel output

The exported Excel includes:
- Currency formatting (`$1,234.56`) on revenue columns
- Clean date formatting (`2024-06-21`, no timestamps)
- Auto-adjusted column widths
- Styled headers (bold, white text, blue background)
- Frozen header row for easy scrolling

This is what separates a "data dump" from a report a client can actually use.

## Tech stack

- Python 3.12
- pandas (data manipulation)
- matplotlib (visualization)
- openpyxl (multi-sheet Excel export with formatting)

## Usage

```bash
# Create virtual environment and install dependencies
python3.12 -m venv venv
source venv/bin/activate
pip install pandas matplotlib openpyxl numpy

# Generate sample data (optional)
python generate_data.py

# Run pipeline
python clean_and_report.py messy_sales.csv
```

Output in the `report/` folder:
- `monthly_revenue.png` — stacked bar chart, month × category
- `sales_report.xlsx` — Excel with clean data, monthly summary, and top 10 products

## Sample output

Processing 515 rows with 15 duplicates and 39 null values:

[1/5] Data loaded: 515 rows, 6 columns
[2/5] Duplicates removed: 15
[3/5] Cleaning complete: 500 final rows
[4/5] Chart saved: report/monthly_revenue.png
[5/5] Excel saved: report/sales_report.xlsx
EXECUTIVE SUMMARY
Total revenue: $730,347.14
Average ticket: $1,460.69
Period: 2024-01-01 to 2024-12-31
Leading category: Clothing

## Customization for your business

The pipeline is adaptable. Contact me if you need:
- Additional columns from your ERP
- API integrations (Shopify, WooCommerce, Stripe)
- Automated email reports
- Interactive dashboards

## Author

Ibrahim Adippe — Data analyst specialized in data cleaning and automated reporting with Python and R.
