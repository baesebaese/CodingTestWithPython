'''

수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성
'''

def solution(answers):
    # 수포자들의 패턴
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    # 수포자들의 점수 리스트
    scores = [0] * 3
    
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                scores[j] += 1
                
    # 가장 높은 점수 저장
    max_score = max(scores)
    
    #가장 높은 점수를 가진 수포자들의 번호를 찾아서 리스트에 저장
    highest_scores = []

    for i, score in enumerate(scores):
        if score == max_score:
            highest_scores.append(i + 1)
            
    return highest_scores
    
            
solution([1, 2, 3, 4, 5]);