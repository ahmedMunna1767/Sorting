def insertionSort(unSortedList):
    for i in range(1, len(unSortedList)):
        key = unSortedList[i]
        j = i-1
        while j >= 0 and key < unSortedList[j] :
            unSortedList[j + 1] = unSortedList[j]
            j = j - 1
        unSortedList[j + 1] = key

    return unSortedList

if __name__ == '__main__':
    print("Insertion Sort")
    unSortedList = [14, 21, 12, 11, 13, 5, 6, 7, 32]
    print("Unsorted:", unSortedList)
    sortedList = insertionSort(unSortedList)
    print("Sorted:  ", sortedList)
