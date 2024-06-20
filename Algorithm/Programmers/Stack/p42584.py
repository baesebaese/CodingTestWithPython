'''
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

'''
def solution(prices):
    n = len(prices)
    answer = [0] * n

    # 스택을 사용해 이전 가격과 현재 가격 비교
    stack = [0]
    for i in range(1, n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i-j
        stack.append(i)
        
    # 스택에 남아 있는 가격들은 가격이 떨어지지 않은 경우
    while stack:
        j = stack.pop()
        answer[j] = n-1-j
    
    
    return answer    

solution([1, 6, 9, 5])