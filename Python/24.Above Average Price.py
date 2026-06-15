# Given a dictionary of items and prices, return items that cost more than the average price.


def func(item):
    sum = 0
    for keys, values in item.items():
        sum += values
    avg = sum/len(item)
    a = []
    for keys, values in item.items():
        if values>avg:
            a.append(keys)
    return a

item = {
    "apple": 1.5,
    "laptop": 999,
    "pen": 2.0,
    "phone": 699,
    "notebook": 5.0
}

result = func(item)
print(result)

