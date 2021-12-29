# 프로그래머스 파이썬 정수 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12933
def solution(n):
    s = str(n)
    l = []
    for i in s:
        l.append(i)
    l.sort(reverse=True)
    s = ''
    for i in l:
        s += i
    return int(s)
