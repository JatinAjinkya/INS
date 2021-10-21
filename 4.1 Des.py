from pyDes import *
data = input("Enter encryption data:")
k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
charset = "utf-8"
encrypted = k.encrypt(data.encode(charset))
print ("Encrypted: " + repr(encrypted))
decrypted = k.decrypt(encrypted).decode(charset)
print ("Decrypted: " + decrypted)
