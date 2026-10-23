import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)

# --------------------------------------------------
# Output location
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = BASE_DIR / "data" / "sales_data.csv"
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# Business data
# --------------------------------------------------
products = [
    ("P001", "Laptop Pro 15", "Technology", "Computers", 1200, 820),
    ("P002", "Laptop Air 13", "Technology", "Computers", 900, 610),
    ("P003", "Gaming Monitor", "Technology", "Monitors", 420, 275),
    ("P004", "Office Monitor", "Technology", "Monitors", 250, 155),
    ("P005", "Wireless Mouse", "Technology", "Accessories", 45, 20),
    ("P006", "Mechanical Keyboard", "Technology", "Accessories", 95, 48),
    ("P007", "USB-C Hub", "Technology", "Accessories", 65, 31),
    ("P008", "Noise Cancelling Headphones", "Technology", "Audio", 220, 125),
    ("P009", "Bluetooth Speaker", "Technology", "Audio", 130, 68),
    ("P010", "1TB SSD", "Technology", "Storage", 110, 62),

    ("P011", "Ergonomic Office Chair", "Furniture", "Chairs", 340, 205),
    ("P012", "Executive Chair", "Furniture", "Chairs", 480, 300),
    ("P013", "Standing Desk", "Furniture", "Desks", 550, 340),
    ("P014", "Office Desk", "Furniture", "Desks", 300, 175),
    ("P015", "Bookshelf", "Furniture", "Storage Furniture", 190, 105),

    ("P016", "Notebook Pack", "Office Supplies", "Paper", 18, 7),
    ("P017", "Printer Paper Box", "Office Supplies", "Paper", 32, 14),
    ("P018", "Pen Set", "Office Supplies", "Writing", 15, 5),
    ("P019", "Desk Organizer", "Office Supplies", "Organization", 28, 11),
    ("P020", "Document Folder Pack", "Office Supplies", "Organization", 22, 8),
]

locations = [
    ("India", "West", "Gujarat", "Ahmedabad"),
    ("India", "West", "Maharashtra", "Mumbai"),
    ("India", "North", "Delhi", "New Delhi"),
    ("India", "North", "Uttar Pradesh", "Noida"),
    ("India", "South", "Karnataka", "Bengaluru"),
    ("India", "South", "Tamil Nadu", "Chennai"),
    ("India", "South", "Telangana", "Hyderabad"),
    ("India", "East", "West Bengal", "Kolkata"),
    ("India", "West", "Rajasthan", "Jaipur"),
    ("India", "North", "Punjab", "Chandigarh"),
]

first_names = [
    "Aarav", "Vivaan", "Aditya", "Arjun", "Rohan",
    "Rahul", "Karan", "Neha", "Priya", "Ananya",
    "Isha", "Kavya", "Meera", "Riya", "Sneha",
]

last_names = [
    "Patel", "Shah", "Mehta", "Sharma", "Verma",
    "Singh", "Gupta", "Joshi", "Desai", "Kapoor",
]

segments = ["Consumer", "Corporate", "Small Business"]
channels = ["Website", "Mobile App", "Marketplace", "Direct Sales"]

# --------------------------------------------------
# Create customer master data
# --------------------------------------------------
customers = []

for customer_number in range(1, 1001):
    customer_id = f"C{customer_number:04d}"
    customer_name = f"{random.choice(first_names)} {random.choice(last_names)}"
    segment = random.choices(
        segments,
        weights=[55, 25, 20],
        k=1
    )[0]

    country, region, state, city = random.choice(locations)

    customers.append(
        (
            customer_id,
            customer_name,
            segment,
            country,
            region,
            state,
            city,
        )
    )

# --------------------------------------------------
# Generate sales transactions
# --------------------------------------------------
start_date = datetime(2022, 1, 1)
end_date = datetime(2025, 12, 31)

number_of_orders = 15000
rows = []

for order_number in range(1, number_of_orders + 1):

    order_id = f"ORD{order_number:06d}"

    days_range = (end_date - start_date).days
    order_date = start_date + timedelta(
        days=random.randint(0, days_range)
    )

    customer = random.choice(customers)

    (
        customer_id,
        customer_name,
        customer_segment,
        country,
        region,
        state,
        city,
    ) = customer

    (
        product_id,
        product_name,
        category,
        sub_category,
        unit_price,
        unit_cost,
    ) = random.choice(products)

    sales_channel = random.choices(
        channels,
        weights=[40, 25, 20, 15],
        k=1
    )[0]

    quantity = random.randint(1, 6)

    discount = random.choices(
        [0.00, 0.05, 0.10, 0.15, 0.20, 0.25],
        weights=[30, 20, 20, 15, 10, 5],
        k=1
    )[0]

    gross_sales = quantity * unit_price
    sales = gross_sales * (1 - discount)
    cost = quantity * unit_cost
    profit = sales - cost

    rows.append(
        [
            order_id,
            order_date.strftime("%Y-%m-%d"),
            customer_id,
            customer_name,
            customer_segment,
            country,
            region,
            state,
            city,
            product_id,
            product_name,
            category,
            sub_category,
            sales_channel,
            quantity,
            round(unit_price, 2),
            discount,
            round(sales, 2),
            round(cost, 2),
            round(profit, 2),
        ]
    )

# --------------------------------------------------
# Write CSV
# --------------------------------------------------
headers = [
    "Order ID",
    "Order Date",
    "Customer ID",
    "Customer Name",
    "Customer Segment",
    "Country",
    "Region",
    "State",
    "City",
    "Product ID",
    "Product",
    "Category",
    "Sub-Category",
    "Sales Channel",
    "Quantity",
    "Unit Price",
    "Discount",
    "Sales",
    "Cost",
    "Profit",
]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows)

print("Dataset created successfully!")
print(f"File: {OUTPUT_FILE}")
print(f"Rows: {len(rows):,}")
print(f"Customers: {len(customers):,}")
print(f"Date range: {start_date.date()} to {end_date.date()}")
print(f"Columns: {len(headers)}")