def checkOneAway(one,two):
    one = one.lower()
    two = two.lower()
    counter = 0
    oneArr = [0]*128
    twoArr = [0]*128
    for x in one:
        if(oneArr[ord(x)]):
            oneArr[ord(x)] +=1
        else:
            oneArr[ord(x)] =1

    for x in two:
        if(twoArr[ord(x)]):
            twoArr[ord(x)] +=1
        else:
            twoArr[ord(x)] =1

    if ( one == two):
        return True
    else:
        for x in one:
            if not oneArr[ord(x)] == twoArr[ord(x)]:
                counter += 1
    return [False,True][counter<=1]


print(checkOneAway(input("Enter String one\n"),input("Enter string two\n")))

