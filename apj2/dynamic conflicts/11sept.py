#in file 'transaction.txt' data should be wriiten like below given example:
#eg T1<space>:<space>read<space>A

filename="transactions.txt"
f=open(filename)
lines=list(f)
values={"T1":{"T2":0,"T3":0},
   "T2":{"T1":0,"T3":0},
   "T3":{"T1":0,"T2":0}
    }
f1 = open("transactions taking place.txt","w+")
a=len(lines)
h=a
t=0
conflict=0
while a-1!=0:
    b=lines[t]
    if b.find("T1")!=-1:
            c="T1"
    if b.find("T2")!=-1:
            c="T2"
    if b.find("T3")!=-1:
            c="T3"
    if b.find("read")!=-1:
            d="read"
    if b.find("write")!=-1:
            d="write"
    if b.find("A")!=-1:
        g="A"
    if b.find("B")!=-1:
        g="B"
    t=t+1
    for j in range(t,h):
        e=lines[j]
        if e.find("T1")!=-1:
            x="T1"
        if e.find("T2")!=-1:
            x="T2"
        if e.find("T3")!=-1:
            x="T3"
        if e.find("read")!=-1:
            y="read"
        if e.find("write")!=-1:
            y="write"
        if e.find("A")!=-1:
            z="A"
        if e.find("B")!=-1:
            z="B"
        if c!=x and g==z and not(d=="read" and y=="read"):
            #print("{0} ---> {1}".format(c,x))
            values[c][x]=values[c][x]+1
            if values[x][c]!=0:
                conflict=1
                break
            f1.write("\n{0} ---> {1}".format(c,x))
    if conflict==1:
        break;
    a=a-1
if conflict==1:
    f1.truncate(0)
    f1.write("\nconflict")
f.close()
f1.close()
