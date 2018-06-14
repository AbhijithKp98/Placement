def compare(a,b,c):

    if((a<b)&(a<c)):
        return(a);
    elif(b<c):
        return(b);
    else:
        return(c);

x=int(input("Enter a:"))
y=int(input("Enter b:"))
z=int(input("Enter c:"))
s=compare(x,y,z)
print("smallest=%d"%(s))


