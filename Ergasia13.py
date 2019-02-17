from itertools import combinations


def maxDistance (List,MaxNumber):
    MaxSum=0
    ListWithCombinations=[]
    ListWithSums=[]
    List2=[]
    ListLen=len(List)
    for i in range (2,ListLen+1):
        List2=list(combinations(List,i))
        for j in range (0,len(List2)):
            ListWithCombinations.append(List2[j])
        List2.clear()
    for i in range (0,len(ListWithCombinations)):
        ListWithSums.append(sum(ListWithCombinations[i]))
    print (ListWithSums)

    for i in range (0,len(ListWithSums)):
        if (ListWithSums[i]>MaxSum) & (ListWithSums[i]<MaxNumber):
            MaxSum=ListWithSums[i]
    return MaxSum





















