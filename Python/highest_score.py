# Given a list of dictionaries where each dict has keys name and score, 
# return the name of the person with the highest score.

"""students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]
→ return "Bob" because he has the highest score of 92."""



def highest_score(students):
    max = 0
    name = str()
    for i in students:
        if i["score"]>max:
            max = i["score"]
            name = i["name"]
    return name

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]


result = highest_score(students)
print(result)
