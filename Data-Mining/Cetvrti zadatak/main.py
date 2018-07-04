import pandas as pd

mix = pd.read_csv("files/order_products__prior.csv");
n = len(set(mix["order_id"]));
t = len(set(mix["product_id"]));

ar = [0] * 3 * t;

for i in mix["product_id"]:
    ar[i] += 1;


ar.sort();

x = ar[-10:];

for i in x:
    print(i);
