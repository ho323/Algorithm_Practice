# 프로그래머스 파이썬 문자열을 정수로 바꾸기
# https://programmers.co.kr/learn/courses/30/lessons/12925
def solution(s):
    answer = 0
    if s[0] == '-':
        answer = -int(s[1:])
    else:
        if s[0] == '+':
            answer = int(s[1:])
        else:
            answer = int(s)
    return answer
