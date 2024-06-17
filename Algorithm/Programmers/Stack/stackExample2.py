'''
 소괄호는 짝을 맞춘 열린괄호 '(' 와 닫힌 괄호 ')' 로 구성합니다. 문제에서는 열린괄호나 닫힌 괄호가 뒤섞인 문자열이 주어집니다.
 이때 소괄호가 정상으로 열고 닫혔는지 판별하는 solution() 함수를 구현하세요
'''

def solution(s)
    stack = []
    
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                return False
            else:
                stack.pop(c)
            
    if stack:
        return False
    else:
        return True
