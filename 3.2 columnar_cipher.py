def plainText(text,key):
    text=text.lower()
    text=text.replace(" ","")
    for i in range(len(text)):
        if len(text)%len(key)!=0:
            text+="x"
    return text
def keyList(key):
    list1=list()
    for i in range(len(key)):
        list1.append(key[i])
    return list1
#Encryption Starts here!!!!
def matrix_encrypt(text,list1):
    m=[]
    index=0
    for i in range(len(text)//len(list1)):
        a=[]
        for j in range(len(list1)):
            if index<len(text):
                a.append(text[index])
                index=index+1
        m.append(a)
    print("matrix:")
    for i in range(len(text)//len(list1)):
        for j in range(len(list1)):
            print(m[i][j],end=" ")
        print()
    return m
def encrypt(m, list1,list2, text):
    en=""
    row=(len(text)//len(list1))
    for k in range(len(list1)):
        num=list1.index(min(list2))
        list2.remove(min(list2))
        for i in range(row):
            for j in range(len(list1)):
                #print(m[i])
                #print(num)
                en+=m[i][num]
                break
    print(" ")
    print("Cipher Text: ",en)
    return en
def encryptionAlgo(text, key):
    plain_text=plainText(text,key)
    key_list1=keyList(key)
    key_list2=keyList(key)
    print(plain_text)
    print(key_list1)
    m_plain=matrix_encrypt(plain_text,key_list1)
    cipher=encrypt(m_plain,key_list1, key_list2, plain_text)
    return cipher
#Decryption Starts here!!!!
def keyList(key):
    list1=list()
    for i in range(len(key)):
        list1.append(key[i])
    return list1
def matrix_list(cipher, list1):
    a=[]
    matrix_list=list()
    var=len(cipher)//len(list1)
    index=0
    for i in range(len(list1)):
        if index<len(list1):
            letter=list1[i]
            letter=int(letter)
            num=(letter*var)-var
            for j in range(num,num+var):
                a.append(cipher[j])
        else:
            break
    print("list of matrix characters: ",a)
    return a
def matrix_decrypt(mat_list,list1):
    m=[]
    index=0
    for i in range(len(list1)):
        a=[]
        for j in range(len(mat_list)//len(list1)):
            if index<len(mat_list):
                a.append(mat_list[index])
                index=index+1
        m.append(a)
    print("columnwise groups of matrix characters: ",m)
    print("matrix:")
    for i in range(len(mat_list)//len(list1)):#
        for j in range(len(list1)):#
            print(m[j][i],end=" ")
        print()
    return m
def decryption(m,mat_list,list1):
    de=""
    for i in range(len(mat_list)//len(list1)):#
        for j in range(len(list1)):#
            de+=m[j][i]
    print(" ")
    print("Plain text: ",de)
    return de
def decryptionAlgo(cipher, key):
    list1=keyList(key)
    mat_list=matrix_list(cipher, list1)
    m=matrix_decrypt(mat_list,list1)
    plain=decryption(m,mat_list,list1)
    return plain
text=input("Enter plain text:")
key=input("Enter key:")
print("encryption goes here!!!")
print(" ")
cipher=encryptionAlgo(text, key)
print(" ")
print("decryption goes here!!!")
print(" ")
plain=decryptionAlgo(cipher, key)
