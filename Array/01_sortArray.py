''' 01 배열 정렬하기
정수 배열을 정렬해서 반환하는 solution() 함수를 완성하세요
'''

# 버블 정렬로 정렬하기
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


        
        
    