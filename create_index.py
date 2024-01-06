import pandas as pd
import requests
import json
import sys
import re
import collections

df = pd.read_csv(sys.argv[1])

result = df.to_json(orient="records")
r = requests.put('https://dsci551hw1-716d4-default-rtdb.firebaseio.com/HW1/cars.json', data = result)
print(r)
data = r.json()

unique_keywords = set()
car_dict = collections.defaultdict(list)


for k in range(len(data)):
    car_name = data[k]["CarName"]
    keywords = re.split('\W+', car_name)
    car_id = data[k]["car_ID"]
    for word in keywords:
        car_dict[word].append(car_id)
        unique_keywords.add(word)
    
unique_keywords.remove("")
car_json = json.dumps(car_dict)

index = requests.put('https://dsci5512022-default-rtdb.firebaseio.com//HW1/index.json', json = car_json)
print(index)



