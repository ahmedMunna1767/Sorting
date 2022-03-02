def heapSort(unSortedList: list) -> list:
    arrLen = len(unSortedList)

    for i in range(arrLen//2 - 1, -1, -1):
        heapify(unSortedList, arrLen, i)
        

    for i in range(arrLen-1, 0, -1):
        unSortedList[i], unSortedList[0] = unSortedList[0], unSortedList[i]
        heapify(unSortedList, i, 0)

    return unSortedList

def heapify(arr, arrLen, i):
    largest = i 
    l = 2 * i + 1	 
    r = 2 * i + 2	 

    if l < arrLen and arr[largest] < arr[l]:
        largest = l

    if r < arrLen and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] 
        heapify(arr, arrLen, largest)


if __name__ == '__main__':
    print("Heap-Sort")

   # unSortedList = list(map(int, input().rstrip().split()))
    unSortedList = [1, 2, 3, 12, 11, 13, 5, 6, 7]
    print("Unsorted:", unSortedList)
    sortedList = heapSort(unSortedList= unSortedList)
    print("Sorted:  ", sortedList)