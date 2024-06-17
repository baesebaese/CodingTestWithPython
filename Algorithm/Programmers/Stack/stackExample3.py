'''
 10 진수를 입력받아 2진수로 변환하는 solution 함수를 구현
'''

def solution(decimal):
    stack = []
    while decimal > 0:
        remainder = decimal % 2
        stack.append(str(remainder))
        decimal //= 2
    binary = ""
    
    while stack:
        binary += stack.pop
        
    return binary
    