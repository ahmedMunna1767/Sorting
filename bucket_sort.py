def getBucketNum(val, minVal, segmentVal):
    diff = (val - minVal) / segmentVal - int((val - minVal) / segmentVal)
    if(diff == 0 and val != minVal):
        return int((val - minVal) / segmentVal) - 1
    else:
        return int((val - minVal) / segmentVal)

def bucketSort(unSortedList, bucketNum):
    maxVal = max(unSortedList)
    minVal = min(unSortedList)
    segmentVal = (maxVal - minVal) / bucketNum

    tempBuckets = []
    for i in range(bucketNum):
        tempBuckets.append([])

    for val in unSortedList:
        index = getBucketNum(val= val, minVal= minVal, segmentVal= segmentVal)
        tempBuckets[index].append(val)

    for i in range(len(tempBuckets)):
        if len(tempBuckets[i]) != 0:
            tempBuckets[i].sort()

    sortedList = []
    for bucket in tempBuckets:
        for val in bucket:
            sortedList.append(val)
    return sortedList

if __name__ == '__main__':
    print("Bucket-Sort")

   # unSortedList = list(map(int, input().rstrip().split()))
    unSortedList = [9.8, 0.6, 10.1, 1.9, 3.07, 3.04, 5.0, 8.0, 4.8, 7.68]
    print("Unsorted:", unSortedList)
    sortedList = bucketSort(unSortedList= unSortedList, bucketNum = 5)
    print("Sorted:  ", sortedList)
