def MergeSort(Array) :
    if len(Array) > 1 :
        n=len(Array)//2
        LeftArray=[Array[k] for k in range (0,n)]
        RightArray=[Array[k] for k in range (n,len(Array))] ,     