def encrypt(string,key):
    alpha='abcdefghijklmnopqrstuvwxyz'
    encr=''
    for i in string.lower():
        k=(alpha.index(i)+key)%26
        encr+=alpha[k]
    print("Encrypted text:",encr)
string=input("Enter some text:")
key=int(input("Enter a key:"))
encrypt(string,key)

#DECRYPTION
def decrypt(string,key):
    alpha='abcdefghijklmnopqrstuvwxyz'
    decr=''
    for i in string.lower():
        k=(alpha.index(i)-key)%26
        decr+=alpha[k]
    print("Decrypted text:",decr)
string=input("Enter some text:")
key=int(input("Enter a key:"))
decrypt(string,key)


