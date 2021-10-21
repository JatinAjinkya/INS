def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    if (m%n)==0:
        return n
    else:
        return(gcd(n,m%n))
#For numbers
def rsaAlgo(p,q):
    print("p=",p,"q=",q)
    n=pq
    fin=(p-1)(q-1)
    for i in range(1,fin):
        if gcd(i,fin)==1:
            e=i
    print("n=",n,"fin=",fin,"e=",e)
    for i in range(n):
        if((i*e)%fin)==1:
            d=i
    print("d=",d)

    #Encryption
    print("Enter message such that message<",n)
    message=int(input(""))
    enc=messagee%n
    print("enc=",enc)

    #Decryption
    print("Enter c such that c<",n)
    cipher=int(input(""))
    dec=cipherd%n
    print("dec=",dec)
def primeNum(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                print("Invalid")
                n=int(input("Enter a Prime Number"))
            else:
                print("Valid")
    else:
        print()
    return n
p=int(input("Enter a Prime Number:"))
p1=primeNum(p)
q=int(input("Enter another Prime number:"))
q1=primeNum(q)
rsaAlgo(p1,q1)
