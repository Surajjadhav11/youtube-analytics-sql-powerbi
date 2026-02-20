import pandas as pd

df = pd.read_csv("CAvideos.csv", encoding="latin1")
df.to_csv("CAvideos_utf8.csv", index=False, encoding="utf-8")

print("Conversion complete")
