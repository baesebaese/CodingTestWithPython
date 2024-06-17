# 선택 정렬

def selection_sort(arr):
    n = len(arr)
    min_num = 0
    for i in range(n):
        min_num = i
        for j in range(i + 1, n):
            if(j < min_num):
                arr[i] = arr[j]
                min_num = j
                
        swap(arr, min_num, i)
    return arr        
                
def swap(arr, i, j):
    tmp = arr
    arr[i] = arr[j]
    arr[j] = tmp
    
arr1 = [1, 2, 3, 4, 5]    
print(selection_sort(arr1))

    
