key = (input("Enter a key:"))
key = key.upper()


def matrix(x, y, initial):
    return [[initial for i in range(x)] for j in range(y)]


result = list()
for c in key:
    if c not in result:
        if c == 'J':
            result.append("I")
        else:
            result.append(c)

flag = 0
for i in range(65, 91):  # storing other character
    if chr(i) not in result:
        if i == 73 and chr(74) not in result:
            result.append("I")
            flag = 1
        elif flag == 0 and i == 73 or i == 74:
            pass
        else:
            result.append(chr(i))

k = 0
matrix = matrix(5, 5, 0)
for i in range(0, 5):
    for j in range(0, 5):
        matrix[i][j] = result[k]
        k += 1


def location(character):
    loc = list()
    if character == 'J':
        character = "I"
    for i, j in enumerate(matrix):
        for k, l in enumerate(j):
            if character == l:
                loc.append(i)
                loc.append(k)
                return loc


def encryption():
    msg = str(input("Enter the plain text:"))
    msg = msg.upper()
    i = 0
    for s in range(0, len(msg) + 1, 2):  # 2 --> steps
        if s < len(msg) - 1:
            if msg[s] == msg[s + 1]:
                msg = msg[:s + 1] + 'X' + msg[s + 1:]  # adding a bogus letter X
    if len(msg) % 2 != 0:  # adding bogus  if a character is alone
        msg = msg[:] + 'X'
    print("Cipher Text:")
    while i < len(msg):
        loc = list()
        loc = location(msg[i])
        loc1 = list()
        loc1 = location(msg[i + 1])
        if loc[1] == loc1[1]:
            print("{}{}".format(matrix[(loc[0] + 1) % 5][loc[1]], matrix[(loc1[0] + 1) % 5][loc1[1]]), end=' ')
        elif loc[0] == loc1[0]:
            print("{}{}".format(matrix[loc[0]][(loc[1] + 1) % 5], matrix[loc1[0]][(loc1[1] + 1) % 5]), end=' ')
        else:
            print("{}{}".format(matrix[loc[0]][loc1[1]], matrix[loc1[0]][loc[1]]), end=' ')
        i = i + 2


def decrypt():  # decryption
    msg = str(input("ENTER CIPHER TEXT:"))
    msg = msg.upper()
    print("PLAIN TEXT:", end=' ')
    i = 0
    while i < len(msg):
        loc = list()
        loc = location(msg[i])
        loc1 = list()
        loc1 = location(msg[i + 1])
        if loc[1] == loc1[1]:
            print("{}{}".format(matrix[(loc[0] - 1) % 5][loc[1]], matrix[(loc1[0] - 1) % 5][loc1[1]]), end=' ')
        elif loc[0] == loc1[0]:
            print("{}{}".format(matrix[loc[0]][(loc[1] - 1) % 5], matrix[loc1[0]][(loc1[1] - 1) % 5]), end=' ')
        else:
            print("{}{}".format(matrix[loc[0]][loc1[1]], matrix[loc1[0]][loc[1]]), end=' ')
        i = i + 2


while 1:
    choice = int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT \n"))
    if choice == 1:
        encryption()
    elif choice == 2:
        decrypt()
    elif choice == 3:
        exit()
    else:
        print("Choose correct choice")
