file1 = open("Transaction.txt","r")
text = file1.read()
list = ['T1','T2','T3','read(A)','write(A)','read(B)','write(B)']
count = 0
lines  = text.split('\n')
words = []
for line in lines:
    word = line.split()
    words.append(word)
storage1 = []
storage2 = []
for i in words:
    count = 0
    for j in i:
        if count != 0:
            continue
        count = count + 1
        if j == list[0] or j == list[1] or j == list[2]:
            storage1.append(i[2])
            storage2.append(j)

file1 = open("Output.txt","w+")

count = [ 0 for x in range(6)]
index1 = 0

length = len(storage1)
for i in range(length):
    
    if storage1[i] == list[3]:
        
        for j in range(i+1,length):
            
            if storage1[j] == list[4] and storage2[i] != storage2[j]:
                file1.write(storage2[i]+"->")
                file1.write(storage2[j]+", ")
                if storage2[i] == 'T1' and storage2[j] == 'T2':
                    count[0] = count[0] + 1
                elif storage2[i] == 'T2' and storage2[j] == 'T1':
                    count[1] = count[1] + 1
                elif storage2[i] == 'T2' and storage2[j] == 'T3':
                    count[2] = count[2] + 1
                elif storage2[i] == 'T3' and storage2[j] == 'T2':
                    count[3] = count[3] + 1
                elif storage2[i] == 'T1' and storage2[j] == 'T3':
                    count[4] = count[4] + 1
                elif storage2[i] == 'T3' and storage2[j] == 'T1':
                    count[5] = count[5] + 1
                    
                              
                break
    
            
    if storage1[i] == list[4]:
        
        for j in range(i+1,length):
            
            if storage1[j] == list[3] and storage2[i] != storage2[j]:
                file1.write(storage2[i]+"->")
                file1.write(storage2[j]+", ")
                if storage2[i] == 'T1' and storage2[j] == 'T2':
                    count[0] = count[0] + 1
                elif storage2[i] == 'T2' and storage2[j] == 'T1':
                    count[1] = count[1] + 1
                elif storage2[i] == 'T2' and storage2[j] == 'T3':
                    count[2] = count[2] + 1
                elif storage2[i] == 'T3' and storage2[j] == 'T2':
                    count[3] = count[3] + 1
                elif storage2[i] == 'T1' and storage2[j] == 'T3':
                    count[4] = count[4] + 1
                elif storage2[i] == 'T3' and storage2[j] == 'T1':
                    count[5] = count[5] + 1
                
                
                break
            if storage1[j] == list[4] and storage2[i] != storage2[j]:
                file1.write(storage2[i]+"->")
                file1.write(storage2[j]+", ")
                if storage2[i] == 'T1' and storage2[j] == 'T2':
                    count[0] = count[0] + 1
                elif storage2[i] == 'T2' and storage2[j] == 'T1':
                    count[1] = count[1] + 1
                elif storage2[i] == 'T2' and storage2[j] == 'T3':
                    count[2] = count[2] + 1
                elif storage2[i] == 'T3' and storage2[j] == 'T2':
                    count[3] = count[3] + 1
                elif storage2[i] == 'T1' and storage2[j] == 'T3':
                    count[4] = count[4] + 1
                elif storage2[i] == 'T3' and storage2[j] == 'T1':
                    count[5] = count[5] + 1
                
                break
            
    if storage1[i] == list[5]:
        
        for j in range(i+1,length):
            if storage1[j] == list[6] and storage2[i] != storage2[j]:
                file1.write(storage2[i]+"->")
                file1.write(storage2[j]+", ")
                if storage2[i] == 'T1' and storage2[j] == 'T2':
                    count[0] = count[0] + 1
                elif storage2[i] == 'T2' and storage2[j] == 'T1':
                    count[1] = count[1] + 1
                elif storage2[i] == 'T2' and storage2[j] == 'T3':
                    count[2] = count[2] + 1
                elif storage2[i] == 'T3' and storage2[j] == 'T2':
                    count[3] = count[3] + 1
                elif storage2[i] == 'T1' and storage2[j] == 'T3':
                    count[4] = count[4] + 1
                elif storage2[i] == 'T3' and storage2[j] == 'T1':
                    count[5] = count[5] + 1
                
                break
            

    if storage1[i] == list[6]:
        
        for storage1[j] in range(i+1,length):
            if storage1[j] == list[5] and storage2[i] != storage2[j]:
                file1.write(storage2[i]+"->")
                file1.write(storage2[j]+", ")
                if storage2[i] == 'T1' and storage2[j] == 'T2':
                    count[0] = count[0] + 1
                elif storage2[i] == 'T2' and storage2[j] == 'T1':
                    count[1] = count[1] + 1
                elif storage2[i] == 'T2' and storage2[j] == 'T3':
                    count[2] = count[2] + 1
                elif storage2[i] == 'T3' and storage2[j] == 'T2':
                    count[3] = count[3] + 1
                elif storage2[i] == 'T1' and storage2[j] == 'T3':
                    count[4] = count[4] + 1
                elif storage2[i] == 'T3' and storage2[j] == 'T1':
                    count[5] = count[5] + 1
                
                break

            elif storage1[j] == list[6] and storage2[i] != storage2[j]:
                file1.write(storage2[i]+"->")
                file1.write(storage2[j]+", ")
                if storage2[i] == 'T1' and storage2[j] == 'T2':
                    count[0] = count[0] + 1
                elif storage2[i] == 'T2' and storage2[j] == 'T1':
                    count[1] = count[1] + 1
                elif storage2[i] == 'T2' and storage2[j] == 'T3':
                    count[2] = count[2] + 1
                elif storage2[i] == 'T3' and storage2[j] == 'T2':
                    count[3] = count[3] + 1
                elif storage2[i] == 'T1' and storage2[j] == 'T3':
                    count[4] = count[4] + 1
                elif storage2[i] == 'T3' and storage2[j] == 'T1':
                    count[5] = count[5] + 1
                
                break

if count[0]>=1 and count[1] >=1:
    file1.truncate(0)
    file1.write("\nCONFLICTS")
elif count[2]>=1 and count[3]>=1:
    file1.truncate(0)
    file1.write("\nCONFLICTS")
elif count[4]>=1 and count[5]>=1:
    file1.truncate(0)
    file1.write("\nCONFLICTS")
else:
    file1.write("\nNO CONFLICTS")
file1.close()
            
    
   
            
        
      
        


