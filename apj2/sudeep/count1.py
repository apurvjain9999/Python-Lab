
string = """ #include <stdio.h>
int main()
{
   // printf() displays the string inside quotation
   printf("Hello, World!");
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
        if i == j:
            count = count +1
    print(i,end=' ')
    print(count)
    


