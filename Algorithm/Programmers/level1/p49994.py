'''
게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.
U: 위쪽으로 한 칸 가기
D: 아래쪽으로 한 칸 가기
R: 오른쪽으로 한 칸 가기
L: 왼쪽으로 한 칸 가기
캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다.
좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.
명령어가 매개변수 dirs로 주어질 때, 게임 캐릭터가 처음 걸어본 길의 길이를 구하여 return 하는 solution 함수를 완성해 주세요.
'''


# 좌표평면을 벗어나는지 체크하는 함수
def is_valid_move(nx, ny):
    return 0 <= nx < 11 and 0 <= ny < 11 

# 명령어를 통해 다음 좌표 결정
def update_location(x, y, dir):
    if dir == 'U':
        nx, ny = x, y+1
    elif dir == 'D':
        nx, ny = x, y-1
    elif dir == 'L':
        nx, ny = x-1, y
    elif dir == 'R':
        nx, ny = x+1, y
    return nx, ny


def solution(dirs):
    x, y = 5, 5
    ans = set() # 겹치는 좌표는 1개로 처리
    for dir in dirs : 
        nx, ny = update_location(x, y, dir)
        if not is_valid_move(nx, ny) : # 유효성 체크
            continue
        ans.add((x, y, nx, ny))
        ans.add((nx, ny, x, y))
        x, y = nx, ny
    return len(ans)/2

solution('ULURRDLLU')