# 프로그래머스 파이썬 최대공약수와 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12940
def solution(n, m):
    answer = []
    mi = 1
    mx = 1
    for i in range(1, m+1):
        if n % i == 0 and m % i == 0:
            mi = i
    for i in range(m, n*m +1):
        if i % n == 0 and i % m == 0:
            mx = i
            break
    answer.append(mi)
    answer.append(mx)
    return answer
