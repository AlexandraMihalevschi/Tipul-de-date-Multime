nume = list(input("Dati un nume: "))
m = 0
n = 0
if ord(nume[0])>=65 and ord(nume[0])<=90:
    m+=1
for i in range(1, len(nume)):
        if ord(nume[i])>=97 and ord(nume[i])<=122:
            n+=1
if m==1 and n==len(nume)-1:
    print("CORECT")
else: print("INCORECT")