# 프로래머스 파이썬 두 개 뽑아서 더하기
# https://programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer=[]
    for i, n in enumerate(numbers):
        num_list = numbers[i+1:]
        for s in num_list:
            answer.append(s+numbers[i])
        
    answer = sorted(list(set(answer)))
    return answer