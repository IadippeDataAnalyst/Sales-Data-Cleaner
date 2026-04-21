"""
Generates a messy sales CSV to simulate real client data.
Includes: duplicates, mixed date formats, null values, category typos.
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

# Config
n_rows = 500
categories = ['Electronics', 'electronics', 'Clothing', 'CLOTHING', 'Home', 'home ', 'Toys', 'Sports']
products = {
    'Electronics': ['Laptop', 'Headphones', 'Mouse', 'Keyboard', 'Monitor'],
    'Clothing': ['Shirt', 'Pants', 'Shoes', 'Jacket'],
    'Home': ['Pan', 'Lamp', 'Chair', 'Table'],
    'Toys': ['Doll', 'RC Car', 'Puzzle'],
    'Sports': ['Ball', 'Racket', 'Gloves']
}

# Generate dates in mixed formats (how real data looks)
start = datetime(2024, 1, 1)
raw_dates = []
for _ in range(n_rows):
    days = random.randint(0, 365)
    date = start + timedelta(days=days)
    fmt = random.choice(['%Y-%m-%d', '%d/%m/%Y', '%m-%d-%Y', '%d-%b-%Y'])
    raw_dates.append(date.strftime(fmt))

# Generate rows
rows = []
for i in range(n_rows):
    cat = random.choice(categories)
    clean_cat = cat.strip().capitalize()
    prod = random.choice(products.get(clean_cat, products['Electronics']))
    quantity = random.randint(1, 10) if random.random() > 0.05 else None
    price = round(random.uniform(10, 500), 2) if random.random() > 0.03 else None
    rows.append({
        'date': raw_dates[i],
        'product': prod,
        'category': cat,
        'quantity': quantity,
        'unit_price': price,
        'customer_id': f'C{random.randint(1000, 1050)}'
    })

df = pd.DataFrame(rows)

# Add intentional duplicates
duplicates = df.sample(15, random_state=42)
df = pd.concat([df, duplicates], ignore_index=True)
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

df.to_csv('messy_sales.csv', index=False)
print(f"CSV generated: messy_sales.csv ({len(df)} rows)")
print(f"Duplicates included: {df.duplicated().sum()}")
print(f"Null values in quantity: {df['quantity'].isna().sum()}")
print(f"Null values in price: {df['unit_price'].isna().sum()}")
