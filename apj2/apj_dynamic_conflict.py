# Please enter transaction like "T1 read A" 
file1 = open("apj_input.txt","r")
users = int(input("Enter no. of Users "))
strg = file1.read()
ls = strg.split("\n")

dict1 = {}
for i in range(users):
    a1 = 'T' + str(i+1)
    dict2 = {}
    for j in range(users):
        if i != j:
            a2 = "T" + str(j+1)
            dict2[a2] = 0
    dict1[a1] = dict2
file1.close()

file2 = open("apj_output.txt","w")

len_ls = len(ls)
l_num = 0
check = 0

for l in ls:
    each = l.split()
    user = each[0]
    action = each[1]
    ac = each[2]

    l_num = l_num + 1

    for j in range(l_num,len_ls):
        lt = ls[j].split()
        user1 = lt[0]
        action1 = lt[1]
        ac1 = lt[2]

        if user != user1 and ac == ac1 and (action != "read" or action1 != "read"):
            dict1[user][user1] = dict1[user][user1] + 1
            if dict1[user1][user] != 0:
                check = 1
                break
            else:
                file2.write(user+"->"+user1+"\t")
                break
    if check == 1:
        break;
if check == 1:
    file2.truncate(0)
    file2.write("There is a Conflict!")   
file2.close()
                

    

