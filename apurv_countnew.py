file = open ("apurv.c",'r')
list1 = ['auto','break','case','char','const','continue','default','do','double'
         ,'else','enum','extern','float','for','goto','if','int','long','register',
         'return','short','signed','sizeof','static','struct','switch','typedef',
         'union','void','while','unsigned','volatile']
		 
count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while str!="":
	str=file.readline()
	if not str.startswith('#') or str.startswith('//') or str.startswith('/*'):
		continue
	
	else :
		list=str.split()
		for i in list:
			for k in range(32):
				if i==list1[k]:
					count[k]=count[k]+1
					
		
for k in range(32):
	print(list1[k]," = " ,count[k])
