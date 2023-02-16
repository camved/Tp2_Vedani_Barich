
import ArrayFunc 


def getMin(Array:list,firstIndex):
    min=firstIndex
    for i in range(firstIndex+1,len(Array)):
        
        if Array[min] < Array[i]:
            min=i
    return min


def main(Array:list):
    print(Array)
    lenght = len(Array)
    for i in range(lenght):
        min = getMin(Array,i)
        if (Array[i]<Array[min]):
            Array = ArrayFunc.iterate(Array,min,i)
    return Array



print(main(ArrayFunc.GenerateRandomArray(5,-10,10)))
        


    
    