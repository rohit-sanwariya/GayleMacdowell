

def replaceSpace(str):
    
    result = ""
    arr_of_char = list()
    for x in str:
        arr_of_char.append(x)
    for i in range(len(str)):
        
        
        if str[i] == " ":
            arr_of_char[i] = "%"
        result += arr_of_char[i]
    return result

print(replaceSpace(input("Please enter the string \n")))
