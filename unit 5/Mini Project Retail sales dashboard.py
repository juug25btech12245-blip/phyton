import csv
import os
import random
import numpy as np
import matplotlib.pyplot as plt

if not os.path.exists("sales.csv"):
    with open("sales.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["month", "category", "units", "revenue"])
        for m in ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]:
            for cat in ["Electronics", "Clothing", "Grocery"]:
                units = random.randint(50, 200)
                w.writerow([m, cat, units, units * random.randint(100, 500)])

months_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
monthly_rev, category_rev, units_list, rev_list = {}, {}, [], []

try:
    with open("sales.csv", newline="") as f:
        for row in csv.DictReader(f):
            units, rev = int(row["units"]), float(row["revenue"])
            monthly_rev[row["month"]] = monthly_rev.get(row["month"], 0) + rev
            category_rev[row["category"]] = category_rev.get(row["category"], 0) + rev
            units_list.append(units)
            rev_list.append(rev)
except FileNotFoundError:
    print("sales.csv not found.")
    raise SystemExit

rev_arr = np.array(rev_list)
print("Total revenue :", rev_arr.sum())
print("Average sale  :", round(rev_arr.mean(), 2))
print("Highest sale  :", rev_arr.max())
print("Std deviation :", round(rev_arr.std(), 2))

months = [m for m in months_order if m in monthly_rev]
fig, axs = plt.subplots(1, 3, figsize=(16, 4))

axs[0].plot(months, [monthly_rev[m] for m in months], marker="o")
axs[0].set_title("Monthly Revenue Trend")
axs[0].set_xlabel("Month"); axs[0].set_ylabel("Revenue")

axs[1].bar(category_rev.keys(), category_rev.values(), color=["tab:blue", "tab:orange", "tab:green"])
axs[1].set_title("Revenue by Category")
axs[1].set_xlabel("Category"); axs[1].set_ylabel("Revenue")

axs[2].scatter(units_list, rev_list, color="red")
axs[2].set_title("Units Sold vs Revenue")
axs[2].set_xlabel("Units"); axs[2].set_ylabel("Revenue")

plt.suptitle("Retail Sales Dashboard")
plt.tight_layout()
plt.show()
