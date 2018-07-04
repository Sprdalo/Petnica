import pandas as pdb;
from pandas import read_csv
from pandas import DataFrame

products = read_csv("instacart_2017_05_01/products.csv");
orders = read_csv("instacart_2017_05_01/orders.csv");
print("Proizvoda ima: ", end = "");
print(products.count()["product_id"]);

users = orders.drop_duplicates();
print("Korisnika ima: ", end = "");
print(users.count()["user_id"]);

print("Narudzbina ima: ", end = "");
print(users.count()["order_id"]);


