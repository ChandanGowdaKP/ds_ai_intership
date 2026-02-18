import pandas as pd

# Sample data
data = {
    "Price": ["$100", "$250", "$175", "$300"],
    "Date": ["2026-01-01", "2026-01-05", "2026-01-10", "2026-01-15"]
}

df = pd.DataFrame(data)

print(df)
