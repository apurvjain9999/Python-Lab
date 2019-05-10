#in file 'transaction.txt' data should be wriiten like below given example:
#eg T1<space>:<space>read<space>A
filename="transactions.txt"
f=open(filename)
lines=list(f)
aa=int(input("enter number of transactions you want to have :\n"))
values={}
for ii in range(aa):
    bb='T'+str(ii+1)
    dd={}
    for jj in range(aa):
        if ii!=jj:
            cc='T'+str(jj+1)
            dd[cc]=0
    values[bb]=dd
print(values)
f1 = open("transactions taking place.txt","w+")
a=len(lines)
print("number of lines = ",a)
h=a
t=0
conflict=0
while a-1!=0:
    b=lines[t]
    print(b)
    #if b.find("T1")!=-1:
    #       c="T1"
    #if b.find("T2")!=-1:
    #       c="T2"
    #if b.find("T3")!=-1:
    #       c="T3"
    first_character=b.split(" ");
    c=first_character[0]
    #if b.find("read")!=-1:
    #       d="read"
    #if b.find("write")!=-1:
    #      d="write"
    d=first_character[1]
    #if b.find("A")!=-1:
    #    g="A"
    #if b.find("B")!=-1:
    #   g="B"
    g=first_character[2]
    t=t+1
    for j in range(t,h):
        e=lines[j]
        first_character=e.split(" ");
        x=first_character[0]
        y=first_character[1]
        z=first_character[2]
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
