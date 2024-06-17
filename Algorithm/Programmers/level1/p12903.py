'''
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요.
단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
'''
import math

def solution(s):
    # 1. 문자열의 길이 구하기
    strLen = len(str(s))
    halfLen = math.floor(strLen/2)
    print(halfLen)

    # 2. 문자열이 짝수라면 가운데 두자리, 홀수라면 가운데 한자리를 변수에 할당
    if strLen%2==0:
        return s[halfLen-1:halfLen+1]
    else :
        return s[halfLen:halfLen+1]

    
def main():
    inputStr = input()
    solution(inputStr)
    
main()