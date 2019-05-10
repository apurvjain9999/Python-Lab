import apurv_count_module

p=apurv_count_module.func()
list=p.split(" ")
print(list)
j={u:list.count(u) for u in list}
print(j)
for u in list:
	if(u=='#include' or u=='<stdio.h>' or u=='void' or u=='main()' or u=='int')
		continue;
	