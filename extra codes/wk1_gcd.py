def gcd(m,n):
    fm=[]
    for i in range(1,m+1):
        if(m%i==0):
            fm.append(i)
    print(fm)

    fn=[]
    for i in range(1,n+1):
        if(n%i==0):
            fn.append(i)
    print(fn)

    
    fc=[]
    for f in fm:
        if(f in fn):
            fc.append(f)
    print(fc[-1])


x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
gcd(x,y)