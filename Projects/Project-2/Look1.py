import os
import re
import argparse
from colorama import init,Fore, Back, Style
init(autoreset=True)
# to check the string in the file
# to check the string as well as the line number
def searchfile(str1,list_file, i):
    list1 = []
    for each_file in list_file:
        #print (each_file)
        fr = open(each_file,"r")
        if i:
            m = re.search(str1,fr.read(),re.I)
        else:
            m = re.search(str1,fr.read())
        if m:
            t1 = (m.group(), each_file)
            list1.append(t1)
    return list1

def SearchFileWithLine(str1,list_file, i):
    list1 = []
    for each_file in list_file:
        #print (each_file)
        fr = open(each_file,"r")
        list2 = []
        if i:
            line_number = 1
            for each_line in fr:
                m1 = re.findall(str1,each_line,re.I)
                line_number = line_number+1
                if m1:
                    #t1 = (m1, each_file,line_number)
                    t11 = [(each,each_file,line_number) for each in m1]
                    list2.extend(t11)

        else:
            line_number1 = 1
            for each_line in fr:
                m1 = re.findall(str1,each_line)
                line_number1 = line_number1+1
                if m1:
                    #t1 = (m.group(), each_file, line_number1)
                    t11 = [(each,each_file,line_number1) for each in m1]
                    list2.extend(t11)
        list1.extend(list2)
    return list1

def OnlyFile(str1, dir, R=False, I=False,L=False):
    if R:
        main_list = []
        resp=os.walk(dir)
        for root, dirs, files in resp:
            if files:
                list_files = []
                for file in files:
                    file_with_path = root+"\\"+file
                    list_files.append(file_with_path)
                if L:
                    list1 = SearchFileWithLine(str1,list_files,  i=I)
                    #print ("this ",list1)
                else:
                    list1 = searchfile(str1,list_files,  i=I)
                    #print ("this ",list1)
                main_list.extend(list1)
        printdata(main_list)

    else:
        list_file = os.listdir(dir)
        list_file=[dir+"\\"+each for each in list_file ]
        list_file = [each for each in list_file if os.path.isfile(each)]
        #list1 = searchfile(str1,list_file,  i=I)
        if L:
            list1 = SearchFileWithLine(str1,list_file,  i=I)
        else:
            list1 = searchfile(str1,list_file,  i=I)
        printdata(list1)

def printdata(list1):
    i = 1
    for each in list1:

        str1,file,*line = each
        if line:
            for num in line:
                print (i," ",Fore.RED+Style.BRIGHT+str1,"\t", Fore.CYAN+Style.BRIGHT+file,"\t",Fore.MAGENTA+Style.BRIGHT+str(num))
        else:
            print (i," ",Fore.RED+Style.BRIGHT+str1,"\t", Fore.CYAN+Style.BRIGHT+file)
        i= i+1
#OnlyFile("Logger.*", "G:\\.MYEXP\\Lets_Batch_4\\31March2022", r=True)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f",nargs=2, help="Search the file in given folder")
    parser.add_argument("-i", action="store_true", help= "Case-Insensitive")
    parser.add_argument("-r", action="store_true", help= "Case-Insensitive")
    parser.add_argument("-l", action="store_true", help= "Case-Insensitive")
    arg = parser.parse_args()

    if arg.f:
        #print (arg.f, arg.i)
        str1, dir = arg.f
        OnlyFile(str1, dir, I=arg.i,R=arg.r,L=arg.l)
main()