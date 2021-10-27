# 프로그래머스 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576 
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i, j in zip(participant, completion):
        if i != j:
            return i
    return participant[-1]
