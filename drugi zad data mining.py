import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Mesovita = pd.read_csv("files/order_products__prior.csv")
n = len(set(Mesovita["order_id"]))
t = len(set(Mesovita["product_id"]))
print("Prosecno: " + str(n/t))
niz = [0] * 3 * n
for i in Mesovita["order_id"]:
    niz[i] += 1
a = np.array(niz)
b = np.array(range(0, 3*n))

plt.plot(b, a)
plt.show()

