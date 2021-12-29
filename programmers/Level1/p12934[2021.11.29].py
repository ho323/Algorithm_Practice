# 프로그래머스 파이썬 정수 제곱근 판별
# https://programmers.co.kr/learn/courses/30/lessons/12934
def solution(n):
    answer = 0
    r = int(n ** (1/2))
    answer = (r+1) ** 2
    if not r ** 2 == n:
        answer = -1
    return answer
