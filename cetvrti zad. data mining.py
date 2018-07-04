Mesovita = pd.read_csv("files/order_products__prior.csv")
n = len(set(Mesovita["order_id"]))
t = len(set(Mesovita["product_id"]))

niz = [0] * 3 * t

for i in Mesovita["product_id"]:
    niz[i] += 1
niz.sort()

x = niz[-10:]

for i in x:
    print(i)