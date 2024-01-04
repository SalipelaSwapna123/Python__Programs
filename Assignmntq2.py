string=input("enter string:")
string=string.lower()
l=[]
for i in string:
    if i not in l:
        l.append(i)
for i in l:
    if i != l[-1]:
        print(i,end=",")
    else:
        print(i)
