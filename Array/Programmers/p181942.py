'''
길이가 같은 두 문자열 str1과 str2가 주어집니다.
두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열 return
'''
def solution(str1, str2):
    answer = ''
    
    if len(str1) == len(str2):
       num=0
       for i in str1:
           answer += str1[num]
           answer += str2[num]
           num+=1
   
    print(answer)
    return answer

def main():
    solution('aaaaa', 'bbbbb')

main()