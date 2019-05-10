string = """ #include <stdio.h>
int main()
{
   /* while break case char if */
   printf("Hello, World!");
   float r = 6.0;
   int d = 6;
   if (d == 6)
       d = 5;
   return 0;
}"""
list1 = ['auto','break','case','char','const','continue','default','do','double'
         ,'else','enum','extern','float','for','goto','if','int','long','register',
         'return','short','signed','sizeof','static','struct','switch','typedef',
         'union','void','while','unsigned','volatile']
list2 = string.split()



for i in list1:
    count = 0
    for j in list2:
        if j == '/*':
            f=1
        elif j=='*/':
            f=0
        elif i == j and f!=1:
            count = count +1
    print(i,end=' ')
    print(count)
    


