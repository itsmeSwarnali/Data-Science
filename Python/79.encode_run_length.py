#Given a string, return its run-length encoding — consecutive repeated characters compressed into count+character format. 
# Example: "aaabbc" → "3a2b1c". "aabccc" → "2a1b3c"
def encode_run_length(string):
    string2 = string + " "
    count = 0
    a = []
    for i in range(len(string2)-1):
        if string2[i] == string2[i+1]:
            count += 1

        elif string2[i] != string2[i+1]:
            count += 1
            a.append(''.join(str(count) + string2[i]))
            count = 0
    return ''.join(a)
            



string = "aaabbc"
result = encode_run_length(string)
print(result)


    
        
        


        
