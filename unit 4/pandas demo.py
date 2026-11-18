import pandas as pd

df = pd.read_csv("payroll.csv")
print(df.head())
df.to_json("payroll.json", orient="records", indent=4)
print(pd.read_json("payroll.json"))
