import pandas as pd

employees = pd.DataFrame({
    "employee_id": [101, 102, 103, 104, 105],
    "name":        ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "department_id": [1, 2, 1, 3, 3]
})

departments = pd.DataFrame({
    "department_id": [1, 2, 4],
    "department_name": ["Sales", "Engineering", "Marketing"]
})

print(employees)
print(departments)


#Do an inner join — only employees who have a matching department
import pandas as p
pd.merge(employees, departments, on="department_id", how="inner")

#Do a left join — all employees, with department name where available
pd.merge(employees, departments, on="department_id", how="left")

#Do a right join — all departments, with employee names where available
pd.merge(employees, departments, on="department_id", how="right")
