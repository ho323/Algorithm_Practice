# 프로그래머스 파이썬 3진법 뒤집기
# https://programmers.co.kr/learn/courses/30/lessons/68935
def solution(n):
    ba = ''
    while n > 0:
        n, mod = divmod(n, 3)
        ba += str(mod)
    
    return int(ba,3)
