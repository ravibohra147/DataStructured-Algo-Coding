import sys
def mergeSort(arr,p,r):
    if p<r:
        q=(p+r)//2
        mergeSort(arr,p,q)
        mergeSort(arr,q+1,r)
        merge(arr,p,q,r)
    return arr
def merge(arr,p,q,r):
    left=arr[p:q+1]
    right=arr[q+1:r+1]
    i=0
    j=0
    left.append(sys.maxsize)
    right.append(sys.maxsize)
    for k in range(p,r+1):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i=i+1
        else:
            arr[k]=right[j]
            j=j+1
        k=k+1
    return arr

arr=[5,2,4,6,1,3]
print("Unsorted Array \n",arr)
arr=mergeSort(arr,0,len(arr)-1)
print("Sorted Array:\n ",arr)