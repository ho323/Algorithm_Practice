# 프로그래머스 로또의 최고 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    answer = [6,6]
    
    cnt = 0
    cntz = lottos.count(0)
    
    for i in lottos:
        for j in win_nums:
            if i == j:
                cnt += 1
                
    x = cnt + cntz - 1
    y = cnt - 1

    if x >= 0:
        answer[0] -= x
    if y >= 0:
        answer[1] -= y
        
    return answer
