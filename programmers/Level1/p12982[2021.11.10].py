# 프로그래머스 파이썬 예산
# https://programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if budget - i > -1:
            budget-=i
            answer+=1
    return answer
