# AutoQuery: Google_Firebase_Car_Inventory_Search

## Overview

AutoQuery is a Python-based application that interacts with Firebase to manage and query a car dataset. The dataset includes information about various cars and their prices.

## Features

- Load entire car datasets into Firebase.
- Search cars by a range of prices.
- Create a keyword index based on car names.
- Search cars by keywords present in car names.

## Execution

### Loading Data
To load the car dataset into Firebase, run the following command:
```
python3 load.py cars.csv
```


### Searching by Price Range
To search for cars within a specific price range:

```
python3 search_price.py <min_price> <max_price>
```



Example:
```
python3 search_price.py 15000 16000
```


### Creating a Keyword Index
To create a keyword index for car names:
```
python3 create_index.py cars.csv
```


### Searching by Keyword
To search for cars by keywords:
```
python3 search_car.py "keyword1 keyword2"
```

Example:
```
python3 search_car.py "honda accord"
```



## Dependencies

- Firebase
- Python 3
- Python `firebase-admin` package

## Configuration

Before running the scripts, ensure you have configured Firebase in your environment and have the `firebase-admin` Python package installed.

To install:
```
pip install firebase-admin
```

## Dataset

The dataset `cars.csv` contains information about cars including name, fuel type, number of doors, and prices. Please note that the dataset IDs differ from the original Kaggle dataset.

## Notes

- Car IDs are not assumed to be one less than the row number.
- Keywords are not case-sensitive.
- If no cars are found within a given search parameter, an appropriate message is returned.


For more information about the dataset, visit the [Kaggle dataset page](https://www.kaggle.com/code/goyalshalini93/car-price-prediction-linear-regression-rfe/notebook).

