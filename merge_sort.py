def merge(leftArr, rightArr, outArr):
    leftCur = 0
    rightCur = 0
    outCur = 0

    while (leftCur < len(leftArr)) and (rightCur < len(rightArr)) :
        if leftArr[leftCur] < rightArr[rightCur]: 
            outArr[outCur] = leftArr[leftCur]
            leftCur = leftCur + 1
        else: 
            outArr[outCur] = rightArr[rightCur]
            rightCur = rightCur + 1
        
        outCur = outCur + 1

    while leftCur < len(leftArr) :
        outArr[outCur] = leftArr[leftCur]
        leftCur = leftCur + 1
        outCur = outCur + 1

    while rightCur < len(rightArr) :
        outArr[outCur] = rightArr[rightCur]
        rightCur = rightCur + 1
        outCur = outCur + 1

def mergeSort(unSortedList) -> list:
    if len(unSortedList) > 1:
        
        midInd = len(unSortedList)//2

        leftArr = unSortedList[ : midInd]
        rightArr = unSortedList[midInd : ]
        
        mergeSort(rightArr)
        mergeSort(leftArr)

        
        merge(leftArr, rightArr, unSortedList)
    return unSortedList

if __name__ == '__main__':
    print("Merge-Sort")

   # unSortedList = list(map(int, input().rstrip().split()))
    unSortedList = [1, 2, 3, 12, 11, 13, 5, 6, 7]
    print("Unsorted:", unSortedList)
    sortedList = mergeSort(unSortedList= unSortedList)
    print("Sorted:  ", sortedList)
