from math import log
def threesquares(m):
    start = int(log(m, 4))
    for i in range(start):
        for j in range(m):
            a = (4 ** i) * (8 * j + 7)
            if a == m:
                return False

    return True

def repfree(s):

    a = set(s)
    return len(a) == len(s)

def hillvalley(l):
    
    if l==[]: 
        return False
    stop=-1
    i=1
    found=1
    if l[0]>l[1]:
        i=1
        for i in range(i, len (l)):
            if l[i-1]<l[1]:
                stop=1
                break
        if stop==-1:
            return False
        i=stop
        for i in range (i,len(l)):
            if l[i-1]>l[i]:
                found=0
                break
        return bool(found)
    elif l[0]<l[1]:
        for i in range(1,len(l)):
            if l[i-1]>l[1]:
                stop=i
                break
        if stop==-1:
            return False
        for i in range(i,len(l)):
            if l[i-1]<l[i]:
                found=0
                break
        return bool(found)
    else:
        return False
print(threesquares(7))
print(repfree("abcd"))
print(hillvalley([1,2,3,4,5,4]))


        