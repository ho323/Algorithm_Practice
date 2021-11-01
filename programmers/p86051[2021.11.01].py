# 프로그래머스 파이썬 없는 숫자 더하기
# https://programmers.co.kr/learn/courses/30/lessons/86051
def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer
