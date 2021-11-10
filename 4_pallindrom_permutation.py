

def isPermPallindrom(str):
    str= str.lower()
    isBool = True
    arr = [0]*128
    for x in str:
            if(arr[ord(x)]):
                arr[ord(x)] +=1
            else:
                arr[ord(x)] =1
    checker = 0
    for x in str:
        
        if(arr[ord(x)]==1 and not x == " "):
            checker += 1
    if(checker>=2):
        isBool = False
    return isBool
    
    
    

print(isPermPallindrom(input("Enter the string for Test \n")))
