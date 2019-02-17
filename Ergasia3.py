import os
FileLines=[]

x=input("Hey,please give me your Python file:")
infile=open(x,'r')
for line in infile:
   FileLines.append(line)
infile.close()




start=0
extra=0
Checker="False"

for i in range(0,len(FileLines)):
    extra=0
    CommentCounter=FileLines[i].count("#")
    for j in range (0,CommentCounter):
        StrCounter=FileLines[i].count('"',start,FileLines[i].find("#",start))
        print (StrCounter)


        if ((StrCounter+extra)%2==0):

            FileLines[i]=FileLines[i][0:FileLines[i].find("#",start)]+"\n"
            if (FileLines[i][0]=="#"):
                FileLines[i]=""
            break
        else:
            extra=FileLines[i].count('"',start,FileLines[i].find("#",start))
            start2=start
            start=FileLines[i].find("#",start2)+1

infile2=open('NewFile.py',"w")
infile2.writelines(FileLines)
infile2.close()
os.remove(x)
os.rename('NewFile.py',x)




