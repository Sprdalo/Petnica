import pandas as pd

#Neispavana noc iza ovog cuda
#Ali sam ponosan!

mix = pd.read_csv("files/orders.csv")

def Day(cnt): 
    if cnt == 1:
        return "Monday";
    if cnt == 2:
        return "Tuesday";
    if cnt == 3:
        return "Wednesday";
    if cnt == 4:
        return "Thursday";
    if cnt == 5:
        return "Friday";
    if cnt == 6:
        return "Saturday";
    if cnt == 7:
        return "Sunday";

ar = [0] * 8;

for i in mix["order_dow"]:
    ar[i] += 1;

sol = 0; cur = 0;

for i in range(0, 8):
   if ar[i] > sol:
       sol = ar[i];
       ind = i;
ar[ind] = 0;

res = 0;
ind = 0;

for i in range(0, 8):
   if ar[i] > res:
       res = ar[i];
       ind = i;

print("Most efficient days: " + str(Day(ind + 1)) + " and " + str(Day(cur + 1)));
