def grade_cal(n):
    if n>= 80:
        return "A+"
    elif n>=70:
        return "A"
    elif n>=60:
        return "A-"
    elif n>=34:
        return "D"
    else:
        return "F"

n = int(input("Enter a number:"))

grade = grade_cal(n)
print("the grade is:", grade)
