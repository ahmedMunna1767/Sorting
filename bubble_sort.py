def bubbleSort(unSortedList: list[int]) -> list[int]:
    swapHappened = False
    while True:
        for i in range(len(unSortedList) - 1):
            if unSortedList[i] > unSortedList[i + 1]:
                unSortedList[i], unSortedList[i + 1] = unSortedList[i + 1], unSortedList[i]
                swapHappened = True
        if swapHappened:
            swapHappened = False
        else:
            break

    return unSortedList

if __name__ == '__main__':
    unSortedList = list(map(int, input().rstrip().split()))
    print("Unsorted:", unSortedList)
    sortedList = bubbleSort(unSortedList= unSortedList)
    print("Sorted:  ", sortedList)