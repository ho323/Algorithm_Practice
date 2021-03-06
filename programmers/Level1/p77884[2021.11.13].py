# 프로그래머스 파이썬 약수의 개수와 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/77884
import math
def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        count = 0
        for j in range(1, int(math.sqrt(i))+1):
            if i % j == 0:
                if i // j == j:
                    count += 1
                else:
                    count += 2
        if count % 2 == 0:
            answer += i
        else:
            answer -= i 

    return answer
