# 프로그래머스 파이썬 부족한 금액 계산하기
# https://programmers.co.kr/learn/courses/30/lessons/82612
def solution(price, money, count):
    answer = 0
    for i in range(1, count+1):
        answer += price * i
    if answer > money:
        answer -= money
    else:
        answer = 0
    return answer
