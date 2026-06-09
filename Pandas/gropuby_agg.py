import pandas as pd

data = {
    "employee_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "name":        ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry"],
    "department":  ["Sales", "Engineering", "Sales", "HR", "HR", "Engineering", "Sales", "Engineering"],
    "salary":      [52000, 78000, 61000, 45000, 47000, 85000, 58000, 72000],
    "join_year":   [2021, 2020, 2019, 2022, 2021, 2018, 2023, 2020]
}

df = pd.DataFrame(data)
print(df)

# Find the average salary per department
df.groupby("department")["salary"].mean()

# Find the number of employees per department
df.groupby("department")["employee_id"].count()

# Find the maximum salary per department
df.groupby("department")["salary"].max()

# Combine all three into a single summary table
df.groupby("department")["salary"].agg(["mean", "max", "count"])
