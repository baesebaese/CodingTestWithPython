'''
정수 배열 numbers가 주어집니다. 
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 
모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
'''

def solution(numbers):
    ret = [] # 빈 배열 생성
    
    # 두 수를 선택하는 모든 경우의 수 반복문으로 구하기
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            #두 수를 더한 결과를 새로운 배열에 추가
            ret.append(numbers[i] + numbers[j])
            
    #중복된 값 제거, 오름차순 정렬
    ret = sorted(set(ret))
    print(ret)
    return ret
    
def main():
    arr = list(map(int, input().split()))
    solution(arr)
    
main()