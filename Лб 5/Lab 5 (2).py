import csv
import sys

zag=0
pr=0
my_list2=[]
my_list1=[]
filename = "Vedmak.txt"
ryadky=[]
fd = open(filename, "r")
ryadky=fd.readlines()
fd.close()


for elem in ryadky:
    zag=zag+len(elem)
    pr=pr+elem.count(' ')
    slova=elem.split(' ')
    my_list1.append(slova)
print(my_list1[3])
print('pr=',pr) 
print('sym=', zag)
L1=len(my_list1)
L2=0
words_all=0
words_unig=0


for i in range(L1):
    L2=len(my_list1[i])
    for j in range (L2):
        elem=my_list2[i][j]
        words_all=words_all+1
        if elem in my_list2:
            continue
        else:
            my_list2.append(elem)


L1=len(my_list2)
for i in range(L1):
    elem=my_list2[i]
    zriz=elem[-2:]
    if zriz=="\n":
        my_list2[i]=elem[0:-2]
    
words_uniq=len(my_list2)
print(my_list2)
print("all_words=",words_all)
print("unique words=",words_uniq)