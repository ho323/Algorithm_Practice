# 프로그래머스 파이썬 나누어 떨어지는 숫자 배열
# https://programmers.co.kr/learn/courses/30/lessons/12910
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if not answer:
        answer.append(-1)
    return sorted(answer)
