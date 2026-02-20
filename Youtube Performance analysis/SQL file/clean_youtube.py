import pandas as pd

# Read original file
df = pd.read_csv("CAvideos.csv")

# Save clean version
df.to_csv("CAvideos_clean.csv", index=False)

print("File cleaned successfully!")
