'''
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
'''

def solution(a, b):
    answer = 0
    diff = abs(b-a)
    min_numb = a if a < b else b   
    
    for i in range(diff+1):
        answer += min_numb
        min_numb += 1

    return answer

solution(1, 10)