def insertionSort(arr):
    for i in range(0,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr





arr=[5,2,4,6,1,3]
print("Unsorted Array \n",arr)
arr=insertionSort(arr)
print("Sorted Array:\n ",arr)
