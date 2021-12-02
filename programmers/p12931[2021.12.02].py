# 프로그래머스 파이썬 자릿수 더하기
# https://programmers.co.kr/learn/courses/30/lessons/12931
def solution(n):
    answer = 0
    n = str(n)
    for i in n:
        answer += int(i)
    return answer
