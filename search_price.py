import requests
import json
import sys

# search_price.py 10000 15000

# print("arg at index 0: ",sys.argv[0])
# print("arg at index 1: ",sys.argv[1])
# print("arg at index 2: ",sys.argv[2])

lower_range = sys.argv[1]
higher_range = sys.argv[2]
cars_exist = 0

range_info = {'startAt': lower_range, 'endAt': higher_range}
r = requests.get('https://dsci5512022-default-rtdb.firebaseio.com/HW1/cars.json?orderBy="price"&', params=range_info)
data = r.json()
values = data.values()
carid_list = []

for k in data:
    cars_exist = 1
    carid = (data[k]["car_ID"])
    carid_list.append(carid)

if cars_exist == 0:
    print("No cars in the range")
else:
    print("IDs for the car price range are: \n", carid_list)