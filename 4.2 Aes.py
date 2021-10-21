import pyaes
aes=pyaes.AESModeOfOperationCTR(b'DESCRYPTDESCRYPT')
a=input("Enter Text:")
ciphertext=aes.encrypt(a)
print("Encrypted Text:",ciphertext)
aes=pyaes.AESModeOfOperationCTR(b'DESCRYPTDESCRYPT')
plaintext=aes.decrypt(ciphertext)
print("Decrypted Text:",a)
