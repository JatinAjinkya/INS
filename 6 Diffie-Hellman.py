Q=int(input("enter value of Prime Number Q:"))#p(Q)
ALP=int(input("Enter value of Alpha:"))#g(alpha)
l=[]
count=0
for i in range(1,Q):
    l.append((ALP**i)%Q)
    print(l)
for i in range(1,Q):
    if(i in l):
        count=count+1
    if(count==Q-1):
        print("this is a primitive root")
Xa=int(input("Enter value of private key:"))#a(sender)
Xb=int(input("Enter value of public key:"))#b(receiver)
print("Publicly Shared Variables:")
print("\t Publicly Shared Prime:",Q)
print("\t Publicly Shared Base:",ALP)

Ya=(ALP**Xa)%Q
print("\tEmmanuel sends over public chanel:",Ya)
      
Yb=(ALP**Xb)%Q
print("\tBob sends over public chanel:",Yb)
      
print("\n-----------------\n")
print("Privately Calculated Shared Secret:")

A=(Yb**Xa)%Q
print("\tEmmanuel Shared Secret:",A)

B=(Ya**Xb)%Q
if True:
    print("\tBob Shared Secret:",B)
else:
    print("this is not primitive root")
