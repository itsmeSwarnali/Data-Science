# Given a list of dictionaries (each with a "value" key), 
# return only the dictionaries where "value" is greater than a given threshold.
# data = [{"value": 10}, {"value": 50}, {"value": 30}], threshold = 20
# [{"value": 50}, {"value": 30}]

def filter_by_threshold(data, threshold):
    a = []
    for i in data:
        if i["value"]>threshold:
            a.append(i)
    return a

data = [{"value": 10}, {"value": 50}, {"value": 30}]
threshold = 20

result = filter_by_threshold(data, threshold)
print(result)
