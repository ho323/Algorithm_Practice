# 프로그래머스 파이썬 약수의 합
# https://programmers.co.kr/learn/courses/30/lessons/12928
def solution(n):
    answer = 0
    arr = []
    for i in range(1, n+1):
        if n % i == 0:
            arr.append(i)
    answer = sum(arr)
    return answer
