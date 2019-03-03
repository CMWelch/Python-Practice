import numpy as np
import pandas as pd
desired_width=320

pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 15)
eco = pd.read_csv("Ecommerce Purchases")
print(eco)

#Average, lowest, and highest purchase price
avg = eco["Purchase Price"].mean()
print(avg)

high = eco["Purchase Price"].max()
print(high)

low = eco["Purchase Price"].min()
print(low)

#English users
num_en = eco[eco["Language"] == "en"]["Language"].count()
print(num_en)

num_j = eco[eco["Job"] == "Lawyer"]["Job"].count()
print(num_j)

time = eco["AM or PM"].value_counts()
print(time)

pop_jobs = eco["Job"].value_counts().head(5)
print(pop_jobs)

pp_90 = eco[eco["Lot"] == "90 WT"]["Purchase Price"]
print(pp_90)

email = eco[eco["Credit Card"] == 4926535242672853]["Email"]
print(email)

amex = eco[(eco["CC Provider"] == "American Express") & (eco["Purchase Price"] > 95)].count()
print(amex)

def year(string):
    if "25" in string.split("/"):
        return True
    else:
        return False

exp = sum(eco["CC Exp Date"].apply(lambda x: year(x)))
print(exp)


u_add = eco["Email"].apply(lambda x: x.split("@")[1]).value_counts().head(5)
print(u_add)
