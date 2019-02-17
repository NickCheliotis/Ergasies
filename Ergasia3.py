import os
FileLines=[]
x=input ("Hey,Please give me your Python file:")
FileName=str(x)
DotLocation=x.find(".")
if (x[DotLocation+1:]!="py"):
    print ("This file isn't a python file, please try again")
else:
   infile=open(x,'r')
   for line in infile:
       FileLines.append(line)
   infile.close()
   for i in range(len(FileLines)):
       CommentLocation=FileLines[i].find("#")
       if (CommentLocation!=""):
           FileLines[i]= FileLines[i][0:CommentLocation]+"\n"
   infile2=open('NewFile.py',"w")
   infile2.writelines(FileLines)
   infile2.close()
   os.remove(x)
   os.rename('NewFile.py',FileName)







