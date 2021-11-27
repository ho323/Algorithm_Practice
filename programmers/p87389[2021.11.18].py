# 프로그래머스 파이썬 나머지가 1이 되는 수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/87389
def solution(n):
    cnt = 1
    while True:
        if n % cnt == 1:
            answer = cnt
            break
        cnt += 1
    return answer
