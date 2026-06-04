
def tem(temp, conversion):

    if conversion == 1:
        if temp < -273.15:
              return "invalid"
        f  = (temp * 9/5) + 32
        return f
    elif conversion == 2:
        if temp < -459.67 :
            return "invalid"
        c = (temp - 32) * 5/9
        return c
        
    else: 
        return "invalid"


temp = float(input("Enter a temperature: "))
conversion = int(input("1. c to f, 2. f to c: "))


result = tem(temp, conversion)
print("Temp: ",result)
    

