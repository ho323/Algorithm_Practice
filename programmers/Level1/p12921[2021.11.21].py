# 프로그래머스 파이썬 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921
def solution(n):
    m=set(range(2,n+1))

    for i in range(2,n+1):
        if i in m:
            m-=set(range(2*i,n+1,i))
    answer=len(m)
    return answer
