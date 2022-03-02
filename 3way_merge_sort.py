def merge(leftArr, rightArr, midArr, outArr):
    leftCur = 0
    midCur = 0
    rightCur = 0
    outCur = 0
    
    
    while ((leftCur < len(leftArr)) and (midCur < len(midArr)) and (rightCur < len(rightArr))):
        if  (leftArr[leftCur] < midArr[midCur]):
            if(leftArr[leftCur] < rightArr[rightCur]):
                outArr[outCur] = leftArr[leftCur]
                leftCur = leftCur + 1
                outCur = outCur + 1
            else:
                outArr[outCur] = rightArr[rightCur]
                rightCur = rightCur + 1
                outCur = outCur + 1
        else:
            if(midArr[midCur] < rightArr[rightCur]):
                outArr[outCur] = midArr[midCur]
                midCur = midCur + 1
                outCur = outCur + 1
            else:
                outArr[outCur] = rightArr[rightCur]
                outCur = outCur + 1
                rightCur = rightCur + 1


    while ((leftCur < len(leftArr)) and (midCur < len(midArr))):
        if(leftArr[leftCur] < midArr[midCur]):
            outArr[outCur] = leftArr[leftCur]
            outCur = outCur + 1
            leftCur = leftCur + 1

        else:
            outArr[outCur] = midArr[midCur]
            outCur = outCur + 1
            midCur = midCur + 1

    while ((rightCur < len(rightArr)) and (midCur < len(midArr))):
        if(rightArr[rightCur] < midArr[midCur]):
            outArr[outCur] = rightArr[rightCur]
            outCur = outCur + 1
            rightCur = rightCur + 1
        else:
            outArr[outCur] = midArr[midCur]
            outCur = outCur + 1
            midCur = midCur + 1

    while ((rightCur < len(rightArr)) and (leftCur < len(leftArr))):
        if(rightArr[rightCur] < leftArr[leftCur]):
            outArr[outCur] = rightArr[rightCur]
            outCur = outCur + 1
            rightCur = rightCur + 1
        else:
            outArr[outCur] = leftArr[leftCur]
            outCur = outCur + 1
            leftCur = leftCur + 1

    while leftCur < len(leftArr) :
        outArr[outCur] = leftArr[leftCur]
        leftCur = leftCur + 1
        outCur = outCur + 1

    while rightCur < len(rightArr) :
        outArr[outCur] = rightArr[rightCur]
        rightCur = rightCur + 1
        outCur = outCur + 1

    while midCur < len(midArr) :
        outArr[outCur] = midArr[midCur]
        midCur = midCur + 1
        outCur = outCur + 1

def threeWayMergeSort(unSortedList):
    if len(unSortedList) > 1:
        
        midOne = int(len(unSortedList)/ 3)
        midTwo = 2 * midOne 

        leftArr = unSortedList[ : midOne]
        midArr = unSortedList[midOne : midTwo]
        rightArr = unSortedList[midTwo: ]

        
        threeWayMergeSort(leftArr)
        threeWayMergeSort(midArr)
        threeWayMergeSort(rightArr)
        
        merge(leftArr, midArr, rightArr, unSortedList)
    return unSortedList

if __name__ == '__main__':
    print("3-Way Merge-Sort")
   # unSortedList = list(map(int, input().rstrip().split()))
    unSortedList = [1, 2, 3, 12, 11, 13, 5, 6, 7]
    print("Unsorted:", unSortedList)
    sortedList = threeWayMergeSort(unSortedList= unSortedList)
    print("Sorted:  ", sortedList)