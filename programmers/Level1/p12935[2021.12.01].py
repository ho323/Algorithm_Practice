# 프로그래머스 파이썬 제일 작은 수 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12935
def solution(arr):
    m = min(arr)
    arr.remove(m)
    if not arr:
        arr.append(-1)
    return arr
