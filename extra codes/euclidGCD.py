def gcd(m,n):
    if(m<n):
        (m,n)=(n,m)
    while(m%n!=0):
        diff=m-n
        (m,n)=(max(n,diff),min(n,diff))
    return (n)
x=int(input("Enter the first no.: "))
y=int(input("Enter the second no.: "))
print("gcd: ",gcd(x,y))
