def rf(pt):
  pt=pt.replace("","")
  u=""
  l=""
  en=""
  de=""
  j=len(pt)//2
  for i in range(0,len(pt)):
    if(i%2==0):
       u+=pt[i]
    else:
      l+=pt[i]
  en=u+l
  print("Encrypted text is:",en)
  if(len(pt)%2==0):
     for i in range(0,j):
        de+=u[i]
        de+=l[i]
     print("Decrypted text is :",de)
  else:
     for i in range(0,j):
        de+=u[i]
        de+=l[i]
     de+=u[-1]
     print("Decryption text is:",de)
pt=input("Enter some plaintext:")
rf(pt)
