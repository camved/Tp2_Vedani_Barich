import ArrayFunc

def InsertionSort(Array) :
    print(Array)
    for k in range (1,len(Array)):
        key = Array[k]
        i = k-1
        while i>=0 and Array[i]>key :
            Array[i+1] = Array[i]
            i = i-1
            Array[i+1] = key
    return(Array)
    

print(InsertionSort(ArrayFunc.GenerateRandomArray(6,-15,15)))
