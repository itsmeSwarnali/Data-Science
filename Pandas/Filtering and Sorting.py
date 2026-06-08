# Level 1 — Task 03: Filtering and Sorting
- Filter employees whose salary is above 60000
- Filter employees in the Sales department
- Filter employees in Sales AND salary above 55000
- Sort the full DataFrame by salary in descending order


import pandas as pd

data = {
    "employee_id": [101, 102, 103, 104, 105, 106, 107],
    "name":        ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace"],
    "department":  ["Sales", "Engineering", "Sales", "HR", "HR", "Engineering", "Sales"],
    "salary":      [52000, 78000, 61000, 45000, 47000, 85000, 58000],
    "join_date":   ["2021-03-15", "2020-07-01", "2019-11-20", "2022-01-10", 
                    "2021-06-30", "2018-04-12", "2023-08-01"]
}

df = pd.DataFrame(data)
print(df)


# Filter employees whose salary is above 60000
condition = df[df["salary"] > 60000] 
print(condition)


# Filter employees in Sales department
df[df["department"]=="Sales"]


# Filter Sales employees with salary above 55000
df_sales = df[df["department"]=="Sales"]
df_sales[df_sales["salary"]>55000]

or 

df[(df["department"]=="Sales") & (df["salary"] > 55000)]


# Sort full DataFrame by salary descending
df.sort_values(by= "salary", ascending=False)

