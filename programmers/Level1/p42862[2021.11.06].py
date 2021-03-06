# 프로그래머스 파이썬 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862#
def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
            
    return n-len(set_lost)
