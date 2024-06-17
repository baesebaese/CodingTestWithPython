'''
실패율을 구하는 코드를 완성하라.

실패율은 다음과 같이 정의한다.
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성
'''

def solution(N, stages):
    answer = []
    # 스테이지별 도전자 수
    challenger = [0] * (N + 2)
    
    for stage in stages:
        challenger[stage] += 1
    
    # 스테이지별 실패한 사용자 수 계산
    fails = {}
    total = len(stages)
    
    # 스테이지를 순회하며, 실패율 계산
    for i in range(1, N+1):
        if challenger[i] == 0:
            fails[i] = 0
        else :
            fails[i] = challenger[i]/total 
            total -= challenger[i]
            
    #정렬
    result = sorted(fails, key=lambda x: fails[x], reverse=True)

    return result 