import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Hvala Bebicu za pomoc
#Pokidao sam mu zivce vrv

base = pd.read_csv("files/orders.csv");

tmp = len(set(base["order_id"]));
test = len(set(base["user_id"]));
print("Average: " + str(tmp/test));

ar = [0] * 3 * tmp;
for i in base["user_id"]:
    ar[i] += 1;

a = np.array(ar);
b = np.array(range(0, 3 * tmp));

plt.plot(b, a);
plt.show();
