# one string is permutation of other
# abc cab bac acb cba bca 
def sortString(tosortStirng):
    arr = list() 
    for x in tosortStirng:
        arr.append(x)
    arr.sort()
    return arr
    
def isPermutation(one,two):
    if(not len(one).__eq__(len(two))):
        return False
    else:
        if(sortString(one).__eq__(sortString(two))):
            return True

isperm = isPermutation(input("enter first string \n"),input("Enter 2nd string \n"))
print(isperm)