def selectionSort(unSortedList: list[int]) -> list[int]:
    for i in range(len(unSortedList)):
        min  = unSortedList[i]
        minIndex = i
        for j in range(i + 1, len(unSortedList)):
            if min > unSortedList[j]:
                min = unSortedList[j]
                minIndex = j
        if minIndex != i:
            unSortedList[i], unSortedList[minIndex] = unSortedList[minIndex], unSortedList[i]

    return unSortedList


if __name__ == '__main__':
    print("Selection-Sort")

    unSortedList = list(map(int, input().rstrip().split()))
    print("Unsorted:", unSortedList)
    sortedList = selectionSort(unSortedList= unSortedList)
    print("Sorted:  ", sortedList)