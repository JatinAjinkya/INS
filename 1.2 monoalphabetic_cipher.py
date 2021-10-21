test_list = [] 
alpha = 'A'
for i in range(0, 26):
    test_list.append(alpha)
    alpha = chr(ord(alpha) + 1) 
print(test_list)
# since key is fixed
key =[]
alpha='Z'

for i in range(0, 26):
    key.append(alpha)
    alpha = chr(ord(alpha) - 1)
    
def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele 
    return str1

encrypted_word = []
def mono_encryption(plain_text, key):
    for i in range(len(plain_text)):
        main_index = test_list.index(plain_text[i])
        key_index = key[main_index]
        answer = key[key.index(key_index)]
        encrypted_word.append(answer)
    print(encrypted_word)
    
decrypted_word = [] 
def mono_decryption(encrypted_text, key):
    for i in range(len(encrypted_text)):
        main_index = key.index(encrypted_text[i])
        main_index = test_list[main_index]
        answer = key[key.index(main_index)]
        decrypted_word.append(answer)
    print(decrypted_word)
    
text = input("Enter your text:")
text = text.upper()
mono_encryption(text, key)
mono_decryption("SVOOL", key)
