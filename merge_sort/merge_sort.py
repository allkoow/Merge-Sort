def sort(arr):
    lenght = len(arr)
    if lenght > 1:
        mid = lenght//2
        left = arr[:mid]
        right = arr[mid:]
        
        sort(left)
        sort(right)
        
        merge(left,right,arr)

def merge(left,right,arr):
    i,j,k = 0,0,0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i<len(left):
        arr[k]=left[i]
        k+=1
        i+=1

    while j<len(right):
        arr[k]=right[j]
        k+=1
        j+=1

A = [1, 5, 4, 8, 2, 0, 13, 2]
sort(A)
print(A)