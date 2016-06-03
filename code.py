def BinarySearch(List, target):
    List = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~';

    upper = len(List)
    
    while List < upper: 
        a = List + (upper - List ) //2
        value = List[a]
        print(value)
        if target == value:
            return a
        elif target > value:
            if List == a: 
                break 
            List = a
        elif target < value:
            upper = a

print(BinarySearch([1,5,8,10], 8))

