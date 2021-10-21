import hashlib
def file_check(filename):
    hash1=hashlib.md5()
    with open(filename,'rb') as open_file:
        content=open_file.read();
        hash1.update(content)
    print(hash1.hexdigest())

def pass_check(pw):
    hash1=hashlib.md5(pw.encode('utf-8'))
    print("Your md5 password is",hash1.hexdigest())

print("___MD5___")
print("1.File_check \n2.password_check")
choice=int(input("Please enter your choice:"))
if(choice==1):
    print("File Check")
    fn='hello.txt'
    file_check(fn)
elif(choice==2):
    print("Password Check")
    pw=input("Enter a password:")
    pass_check(pw)
else:
    print("Wrong Choice")
