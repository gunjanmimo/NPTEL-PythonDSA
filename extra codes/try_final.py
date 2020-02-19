def consecutive_find(Array):
    l = []
    c = []
    i = 0
    if len(Array)<2:
        print(Array)


    while i < len(Array)-1:
        c.append(Array[i])
        j = i + 1
        while j < len(Array) and Array[i] == Array[j] + j-i:
            c.append(Array[j]) 
            j += 1

        i = j

        if len(c) > len(l):
            l = c
        c = [] #clearning last elements
    return l

##taking input from user
LIST=list(map(int,input().split()))
print(consecutive_find(LIST))