import pandas as pd
import requests
import json
import sys


df = pd.read_csv(sys.argv[1])
print(df.head())
print("\n\n\n\n")

print(df['price'].describe)
print("\n\n\n\n")

result = df.to_json(orient="records")
r = requests.get('https://dsci5512022-default-rtdb.firebaseio.com/HW1/cars.json', data = result)
r
