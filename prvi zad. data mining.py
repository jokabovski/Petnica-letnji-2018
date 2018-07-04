import pandas as pd

Porudzbine = pd.read_csv("files/orders.csv")
Proizvodi = pd.read_csv("files/products.csv")

brProizvoda = len(set(Proizvodi["product_id"]))
brNarudzbina = len(set(Porudzbine["order_id"]))
brKorisnika = len(set(Porudzbine["user_id"]))
print("Br korisnika: " + str(brKorisnika) + " br proizvoda:" + str(brProizvoda) + " br narudzbina: " + str(brNarudzbina))