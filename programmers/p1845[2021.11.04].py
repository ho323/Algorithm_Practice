# 프로그래머스 파이썬 폰켓몬
# https://programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    N = len(nums) / 2
    T = len(set(nums))
    if N > T:
        answer = T
    else:
        answer = N
    return answer
