# 프로그래머스 파이썬 같은 숫자는 싫어
# https://programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = []
    b = arr[0]
    answer.append(b)
    
    for i in range(1, len(arr)):
        if b != arr[i]:
            answer.append(arr[i])
            b = arr[i]
    return answer
