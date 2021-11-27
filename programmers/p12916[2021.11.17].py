# 프로그래머스 파이썬 문자열 내 p와 y의 개수
# https://programmers.co.kr/learn/courses/30/lessons/12916
def solution(s):
    p = s.count('p') + s.count('P')
    y = s.count('y') + s.count('Y')
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print(p,y)
    if p == y:
        answer = True
    else:
        answer = False
    return answer
