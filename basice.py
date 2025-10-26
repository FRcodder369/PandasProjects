import pandas as pd

# SERIES
list = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charizard']

series = pd.Series(list, index=range(1, 6))

print(series)
print(series.loc[1])
print(series.iloc[0])


# DATA FRAMES
data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50]
}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])

# Add a new column
df["Job"] = ["Coock", "N/A", "Cashier"]

# Add a new row
new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"},
                             {"Name": "Eugene", "Age": 60, "Job": "Manager"},],
                       index=["Employee 4", "Employee 5"])
df = pd.concat([df, new_row])

# print(df.loc["Employee 1"])
# print(df.iloc[2])
print(df)