file = open("apurv.c",'r')
list1 = ['auto','break','case','char','const','continue','default','do','double'
         ,'else','enum','extern','float','for','goto','if','int','long','register',
         'return','short','signed','sizeof','static','struct','switch','typedef',
         'union','void','while','unsigned','volatile','asm','dynamic_cast',
         'namespace','reinterpret_cast','bool','explicit','new','static_cast',
         'catch','false','operator','template','class','friend','private','this',
         'const_cast','inline','public','throw','delete','mutable','protected',
         'true','try','typeid','typename','using','virtual','wchar_t','cout','cin','printf','scanf','stdio.h']


count = [0 for x in list1]
print(count)

while str:
    str = file.readline()
    print(str)
    if str.startswith('//') or str.startswith('#'):
        continue
    else:
        list3 = str.split()
        for k in range(0,len(list1)):
            flag = 0

            for j in list3:
                if j == '/*':
                    flag =1
                if j == '("':
                    flag =1
                if j == '")':
                    flag = 0
                if j == '*/':
                    flag = 0
                if flag == 0 and j == list1[k]:
                    count[k]= count[k] + 1

for k in range(0,len(list1)):
    print(list1[k]," = " ,count[k])
            
