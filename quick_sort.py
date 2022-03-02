def quickSort(unSortedList: list, start: int, end: int):
    if (start < end):
        p = partition(start, end, unSortedList)
        quickSort(unSortedList, start, p - 1)
        quickSort(unSortedList, p + 1, end)

    return unSortedList

def partition(start: int, end: int, array: list):
	pivotIndex = start
	pivotVal = array[pivotIndex]

	while start < end:
		while start < len(array) and array[start] <= pivotVal:
			start += 1

		while array[end] > pivotVal:
			end -= 1

		if(start < end):
			array[start], array[end] = array[end], array[start]
	
	array[end], array[pivotIndex] = array[pivotIndex], array[end]
	return end
	
    
if __name__ == '__main__':
    print("Quick-Sort")

   # unSortedList = list(map(int, input().rstrip().split()))
    unSortedList = [14, 21, 32, 12, 11, 13, 5, 6, 7]
    print("Unsorted:", unSortedList)
    sortedList = quickSort(unSortedList, 0, len(unSortedList)-1)
    print("Sorted:  ", sortedList)