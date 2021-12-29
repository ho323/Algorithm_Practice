# 프로그래머스 파이썬 내적
# https://programmers.co.kr/learn/courses/30/lessons/70128
def solution(a, b):
    answer = 0
    product=[]
    for i in range(len(a)):
        product.append(a[i] * b[i])
    for i in range(len(product)):
        answer += product[i]
    return answer