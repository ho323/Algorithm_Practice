# 프로그래머스 파이썬 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889
from collections import Counter

def solution(N, stages):
    fail = {}
    players = len(stages)
    stages.sort()
    counter = Counter(stages)
    for stage in counter:
        if stage in range(1, N+1):
            fail[stage] = counter[stage] / players
            players -= counter[stage]
    for i in range(1, N+1):
        if i not in fail:
            fail[i] = 0
    fail = dict(sorted(fail.items(), key=lambda item: (-item[1], item[0])))
    answer = list(fail.keys())
    return answer
