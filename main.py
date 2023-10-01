"""
ETL-Query script
"""

from mylib.create import extract
from mylib.transform_load import load
from mylib.read import query

# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()

# Query
print("Querying data...")
query()