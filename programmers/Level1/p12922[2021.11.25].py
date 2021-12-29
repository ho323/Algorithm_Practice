# 프로그래머스 파이썬 수박수박수박수박수박수?
# https://programmers.co.kr/learn/courses/30/lessons/1292
def solution(n):
    answer = ''
    tn = ['수', '박']
    i = 0
    for o in range(n):
        i+=1
        if i % 2 == 1:
            answer += (tn[0])
        elif i % 2 == 0:
            answer += (tn[1])
        elif i == 0:
            break
    return answer
