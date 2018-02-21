#!/usr/bin/python
#-*- coding : utf-8-*-

import sys
import time

ref_file=sys.argv[1]
check_file=sys.argv[2]

ref_data=open(ref_file,'r')
main_data=open(check_file,'r')
main_phrases=[]
ref_phrases=[]
pruned_phrases=[]
f=open('pruned_data.txt','w')
count=open('count.txt','w')
for line in ref_data:
    ref_phrases.append(line.strip().decode('UTF-8'))
count_lines=0
for line in main_data:
    line=line.strip().decode('UTF-8')
    count_lines+=1
    count.write(str(count_lines)+'\n')
    if line in ref_phrases:
        f.write(line.encode('UTF-8')+'\n')

ref_data.close()
main_data.close()
f.close()
count.close()
"""        

print 'main phrases listed'
print time.time()
for i in main_phrases:
    if i not in ref_phrases:
        main_phrases.remove(i)
    else:
        f.write(i.encode('UTF-8')+'\n')

#for i in main_phrases:
""" 
