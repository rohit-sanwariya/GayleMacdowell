
def stringCompression(str):
    strCounterArray = [0]*256
    arrCharOriginal = list(set([x for x in str]))
    arrCharOriginal.sort()
    result = ""
    isResultGreater = bool()

    for x in str:
        if (strCounterArray[ord(x)]):
            strCounterArray[ord(x)] +=1
        else:
            strCounterArray[ord(x)] = 1
    

    for x in arrCharOriginal:
        result = result+ x + f"{strCounterArray[ord(x)]}"
        
    
    return [result,str][len(result)>len(str)]
    

print(stringCompression("abcde"))

