#check if string has all unique characters

char_arr = [False]*256
def isStringUnique(str):
    char_dict = {}
    for x in str:
        if(char_arr[ord(x)]):
            return False
        else:
            char_arr[ord(x)] = True
    
    return True


boolIsString = isStringUnique(input("enter you string \n"))
print(["Not unique","String has Unique characters"][boolIsString])

        
