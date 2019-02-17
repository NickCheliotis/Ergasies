def maxSequence (ListWithNumbers):

    ListLen=len(ListWithNumbers)
    ListOfLists=[]

    p=0
    Monoi=[]
    Sums=[]


    for i in range (0,ListLen):
        p=p+1
        for j in range(p, ListLen+1):
         List=[]
         for t in range (i,j):
             List.append(ListWithNumbers[t])
         ListOfLists.append(List)

    ListLen2=len(ListOfLists)
    for i in range(0,ListLen2):
        if(len(ListOfLists[i])==1):
            Monoi.append(ListOfLists[i])
    for i in range (0,len(Monoi)):
        ListOfLists.remove(Monoi[i])

    for i in range (0,len(ListOfLists)):
        for j in range (0,len(ListOfLists[i])):
            ListOfLists[i][j]=int(ListOfLists[i][j])
    for i in range (0,len(ListOfLists)):
        Sums.append(sum(ListOfLists[i]))
    MaxSum=max(Sums)
    for i in range (0,len(ListOfLists)):
        if (sum(ListOfLists[i])==MaxSum):
            MaxSumIndex=i
    return ListOfLists[MaxSumIndex],MaxSum


















































