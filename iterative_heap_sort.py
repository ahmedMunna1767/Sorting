import getpass


def getParent(n): 
    return int((n-1) / 2)

def buildMaxHeap(unSortedList):
    for i in range(len(unSortedList)):
        if(getParent(i) < 0):
            continue
        if unSortedList[i] > unSortedList[getParent(i)]:
            j = i 
            while unSortedList[j] > unSortedList[getParent(j)]:
                unSortedList[j], unSortedList[getParent(j)] = unSortedList[getParent(j)], unSortedList[j]
                j = getParent(j)    
    return unSortedList

def heapSort(unSortedList):
    buildMaxHeap(unSortedList)

    for i in range(len(unSortedList) - 1, 0, -1):
        unSortedList[0], unSortedList[i] = unSortedList[i], unSortedList[0]

        parent, child = 0, 0
        while True:
            child = 2 * parent + 1

            # Point to the bigger Child
            if(child < (i - 1)) and (unSortedList[child] < unSortedList[child + 1]):
                child = child + 1
            
            if child < i and (unSortedList[parent] < unSortedList [child]):
                unSortedList[parent], unSortedList[child] = unSortedList[child], unSortedList[parent]

            parent  = child
            if child >= i:
                break
    
    return unSortedList

if __name__ == '__main__':
    print("Iterative Heap Sort")
    unSortedList = [14, 21, 12, 11, 13, 5, 6, 7, 32]
    print("Unsorted:", unSortedList)
    sortedList = heapSort(unSortedList)
    print("Sorted:  ", sortedList)

