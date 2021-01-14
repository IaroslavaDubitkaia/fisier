with open('input.txt', 'r') as f:
    a=f.readline()
for i in a:
    if (ord(i)>=65) and (ord(i)<=90):
        with open("literaA.txt","a") as f:
            f.write(str(i))
    elif (ord(i)>=48) and (ord(i)<=57):
        with open("cifre.txt","a") as f:
            f.write(str(i))
    elif (ord(i)>=97) and (ord(i)<=123):
        with open("literaB.txt","a") as f:
            f.write(str(i))
    else:
        with open("operatori.txt","a") as f:
            f.write(str(i))