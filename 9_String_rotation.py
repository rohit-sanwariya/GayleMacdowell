def isSubstring(parent,child):
    parent2 = parent*2
    return (parent2.__contains__(child) and len(child) == len(parent))

    

        

print(isSubstring("water","erwat"))
print(isSubstring("waterbottle","bottlewater"))
print(isSubstring("water","erw"))
