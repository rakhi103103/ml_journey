import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os

load_dotenv()
password = quote_plus(os.getenv("DB_PASSWORD"))

orders = pd.read_csv("olist_orders_dataset.csv")
customers = pd.read_csv("olist_customers_dataset.csv")
payments = pd.read_csv("olist_order_payments_dataset.csv")

print("Orders loaded:", len(orders), "rows")
print("Customers loaded:", len(customers), "rows")
print("payments loaded:", len(payments), "rows")

engine = create_engine(f"mysql+mysqlconnector://root:{password}@localhost/ecommerce")

orders.to_sql("orders", con=engine, if_exists="replace", index=False)
print("Orders imported!")

customers.to_sql("customers", con=engine, if_exists="replace", index=False)
print("Customers imported!")
payments.to_sql("payments", con=engine, if_exists="replace", index=False)
print("payments imported!")

print("All done!")
print(f"\n\norder column:\n {orders.columns}")
print(f"\n\customers column:\n {customers.columns}")
print(f"\n\payments column:\n {payments.columns}")

