import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Baza = pd.read_csv("files/orders.csv")

n = len(set(Baza["order_id"]))
t = len(set(Baza["user_id"]))
print("Prosecno: " + str(n/t))
niz = [0] * 3 * n
for i in Baza["user_id"]:
    niz[i] += 1
a = np.array(niz)
b = np.array(range(0, 3*n))

plt.plot(b, a)
plt.show()
