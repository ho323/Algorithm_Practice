# 프로그래머스 음양 더하기
# https://programmers.co.kr/learn/courses/30/lessons/76501?language=python3
def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i] == False:
            absolutes[i] *= -1
        answer += absolutes[i]
            
    return answer
