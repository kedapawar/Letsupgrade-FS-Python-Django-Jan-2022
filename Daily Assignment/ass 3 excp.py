import traceback
list1=[6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]
d1=36
r=[]
try:
    for each in list1:
        if(each==0):
           r.append("Zero dived by Exception")
        elif(36%each):
           r.append("Error")
        elif(36%each==0):
           r.append(0)
    print(r)
        #c=d1/each
        #print("Answer is",c)
except Exception as e:
        print(e)