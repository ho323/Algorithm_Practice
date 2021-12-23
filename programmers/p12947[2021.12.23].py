# 프로그래머스 파이썬 하샤드 수
# https://programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    answer = False
    h = 0
    for i in range(len(str(x))):
        h += int(str(x)[i])
    if x % h == 0:
        answer = True
    return answer
