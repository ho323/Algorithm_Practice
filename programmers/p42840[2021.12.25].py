# 프로그래머스 파이썬 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    answer = []
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    s = [0,0,0]
    
    for idx, a in enumerate(answers):
        if a == p1[idx%len(p1)]:
            s[0] += 1
        if a == p2[idx%len(p2)]:
            s[1] += 1
        if a == p3[idx%len(p3)]:
            s[2] += 1
    
    for idx, d in enumerate(s):
        if d == max(s):
            answer.append(idx+1)
    
    return answer
