def remdup(l):
    z=[]
    for i in l:
        if i not in z:
            z.append(i)
    return z
def sumsquare(l):
    even=[]
    odd=[]
    for i in l:
        if(i%2==0):
            even.append(i*i)
        else:
            odd.append(i*i)
    return [sum(odd),sum(even)]

def transpose(m):
    rez = [[[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]]
    for row in rez:
        return row