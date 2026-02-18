import pandas as pd

data = {
    "Location": [" New York", "new york", "NEW YORK ", "Los Angeles", "los angeles "]
}

df = pd.DataFrame(data)

print(df["Location"].unique())
