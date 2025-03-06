sentence=input()
s=sentence.split()
p=""
l=[]
for i in s:
    p=""
    for j in range(len(i)-1,-1,-1):
        p=p+i[j]
    l.append(p)
p=""
for i in l:
    p=p+i
    p=p+" "
print(p)

    


