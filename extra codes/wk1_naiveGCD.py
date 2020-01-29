#1. with list and more fast
def gcd(m,n):
    cf=[]
    for i in range(1,min(m,n)+1):
        if(m%i==0) and (n%i)==0:
            cf.append(i)
    return cf[-1]
x=int(input("Enter the first no.: "))
y=int(input("Enter the second no.: "))
print("gcd: ",gcd(x,y))


#2. with no list
def gcd(m,n):
    
    for i in range(1,min(m,n)+1):
        if(m%i==0) and (n%i)==0:
            cf=i
    return cf
x=int(input("Enter the first no.: "))
y=int(input("Enter the second no.: "))
print("gcd: ",gcd(x,y))

#3. more fast by checking from backward
def gcd(m,n):
    i=min(m,n)
    while(i>0)
        if(m%i==0) and (n%i)==0:
            return i
        else:
            i-1
x=int(input("Enter the first no.: "))
y=int(input("Enter the second no.: "))
print("gcd: ",gcd(x,y))