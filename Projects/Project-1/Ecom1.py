import os
import time
t1 = time.time()
fr=open("Category.txt")
dict1={}
for line in fr:
    k,v =line.split(":")
    dict1[k.strip()]=v.strip()
remain=[]
main_dict1={}
fr=open("data1.txt","r")
for line in fr:
        for word,cat in dict1.items():
            if word in line:
                main_dict1.setdefault(cat,[]).append(line)
                break
            else:
                remain.append(line)
os.chdir("all_files")
for k,v in main_dict1.items():
        new_name=k+".txt"
        fr=open(new_name,"w")
        fr.writelines(v)
        fr.close()

fr=open("remain.txt","w")
fr.writelines(remain)
fr.close()
t2=time.time()
print("timetaken",t2-t1)    