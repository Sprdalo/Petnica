import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
from pandas import DataFrame

op = pd.read_csv('instacart_2017_05_01/order_products__train.csv');
op.groupby('order_id').count().reset_index().groupby('product_id').count()['order_id'].plot();
plt.show();
