def findMedian(arr):
    # Write your code here
    mid = len(arr) // 2
    n = len(arr)
    quickSort(arr, 0, n-1)
    print(arr)
    return arr[mid]

def quickSort(arr, low, high):
    if len(arr) == 1:
        mid = len(arr) // 2
        return arr[mid]
    if low < high:
        p = iterPart(arr, low, high)
        quickSort(arr, low, p-1)
        quickSort(arr, p + 1, high)

def iterPart(arr, low, high):
    lower_idx = low - 1
    pivot = arr[high]
    
    for i in range(low, high):
        if arr[i] <= pivot:
            lower_idx += 1
            arr[lower_idx], arr[i] = arr[i], arr[lower_idx]
    
    arr[lower_idx+1], arr[high] = arr[high], arr[lower_idx+1]
    
    return lower_idx + 1

if __name__ == "__main__":
    arr = [5, 3, 1, 2, 4]
    n = len(arr)
    result = findMedian(arr)
    print(result)