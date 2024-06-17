'''
2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 
두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT
입니다. 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요
'''

def solution(a, b):
    answer = ''
    month_days_arr = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0
    
    for i in range(a-1) :
        total_days += month_days_arr[i]
        
    total_days += b
    remain_day = total_days % 7
    
    if remain_day == 0:
        answer = 'THU'
    elif remain_day == 1:
        answer = 'FRI'
    elif remain_day == 2:
        answer = 'SAT'
    elif remain_day == 3:
        answer = 'SUN'
    elif remain_day == 4:
        answer = 'MON'  
    elif remain_day == 5:
        answer = 'TUE'
    else :
        answer = 'WED'
    print(answer)
    return answer

solution(6, 1)