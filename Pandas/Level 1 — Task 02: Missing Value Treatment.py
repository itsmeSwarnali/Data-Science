import pandas as pd

data = {
    "employee_id": [101, 102, 103, 104, 105],
    "name":        ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "department":  ["Sales", "Engineering", "Sales", "HR", None],
    "salary":      [52000, 78000, 61000, 45000, None],
    "join_date":   ["2021-03-15", "2020-07-01", "2019-11-20", "2022-01-10", "2021-06-30"]
}

df = pd.DataFrame(data)
print(df)




# Fill Eve's missing salary with the mean salary of all other employees

df["salary"] = df["salary"].fillna(value = df["salary"].mean(), inplace=False)
print(df)

print("\n")

#Fill Eve's missing department with the string "Unknown"
string = "Unknown"
df["department"] = df["department"].fillna(value = string)
print(df)

print("\n")

# - Confirm no missing values remain
print(df.isnull().sum())

