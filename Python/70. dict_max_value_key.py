# Given a dictionary of product names and their sales numbers, return the name of the product with the highest sales. If there's a tie, return any one.
# sales = {"Laptop": 500, "Phone": 800, "Tablet": 300}
# Phone

def dic_max_key(sales):
    max = 0
    key = 0
    for keys, values in sales.items():
        if values>max:
            max = values
            key = keys
    return key

sales = {"Laptop": 500, "Phone": 800, "Tablet": 300}
result = dic_max_key(sales)
print(result)


