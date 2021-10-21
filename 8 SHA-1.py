
import hashlib
def sha(m):
    hash1 = hashlib.sha1(m.encode())
    print("SHA-1 Signature of your message is:", hash1.hexdigest())    
pt = input("Enter your message:")
sha(pt)
