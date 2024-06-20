'''
정수 리스트 num_list가 주어질 때, 마지막 원소가 그전 원소보다 크면 
마지막 원소에서 그전 원소를 뺀 값을 마지막 원소가 그전 원소보다 크지 않다면 
마지막 원소를 두 배한 값을 추가하여 return하도록 solution 함수를 완성해주세요.

'''

def solution(num_list):
    answer = []

    if num_list[-1]>num_list[-2]:
        num_list.append(num_list[-1] - num_list[-2])
    else:
        num_list.append(num_list[-1]*2)

    return answer

'''
두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다.
첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때,
이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return 하는 solution 함수를 작성해 주세요.

'''

def solution2(a, d, included):
    answer = 0
    for i in included:

        if i:
           answer += a
        a+=d
            
    print(answer)


solution2(3, 4, [true, false, false, true, true])