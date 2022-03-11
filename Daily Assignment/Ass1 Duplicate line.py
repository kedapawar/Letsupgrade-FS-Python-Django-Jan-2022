i=0
sample_list=[]
a_file=open("file.txt","r") #file change....
for each in a_file:
    if each in sample_list:
        print("Duplicate line is:",each)
        print(i)
    sample_list.append(each)
    i=i+1