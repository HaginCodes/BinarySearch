binarySearch(List, Item)
firstItem = 0
lastItem = len(lastItem)-1
found = False

while first <= last and not found:
    MiddlePoint = (first + last)//2
    if List == [MiddlePoint] == item: 
       found = True 
    elif: item < List[MiddlePoint] == item
    found = False
    lastItem = MiddlePoint -1 
else:
    first = MiddlePoint +1
    
return found 

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))