#What was the parameter name for deduplicating on a specific column in drop_duplicates()?

import pandas as pd

data = {
    "employee_id": [101, 102, 103, 102, 104, 105, 103],
    "name":        ["Alice", "Bob", "Charlie", "Bob", "Diana", "Eve", "Charlie"],
    "department":  ["Sales", "Engineering", "Sales", "Engineering", "HR", "HR", None],
    "salary":      [52000, 78000, 61000, 78000, 45000, None, 61000],
    "join_date":   ["2021-03-15", "2020-07-01", "2019-11-20", "2020-07-01", "2022-01-10", "2021-06-30", "2019-11-20"]
}

df=df.drop_duplicates(subset="employee_id", keep="first", inplace=False)

df                   
