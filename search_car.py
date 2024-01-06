import pandas as pd
import requests
import json
import sys
import re
import collections

args_list = []

for arg_index in range(len(sys.argv)):
    args_list.append(sys.argv[arg_index].lower())



df = pd.read_csv("cars.csv")

result = df.to_json(orient="records")
r = requests.put('https://dsci5512022-default-rtdb.firebaseio.com//HW1/cars.json', data = result)

data = r.json()




car_dict = collections.defaultdict(list)

for k in range(len(data)):
    car_name = data[k]["CarName"]
    
    keywords = re.split('\W+', car_name)
    car_id = data[k]["car_ID"]
    for word in keywords:
        car_dict[word].append(car_id)


result1=set()
for i in range(1,len(args_list)):
    if args_list[i] in car_dict:
        for r in car_dict[args_list[i]]:
            result1.add(r)

print(result1)  



