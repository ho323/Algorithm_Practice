# 프로그래머스 파이썬 서울에서 김서방 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12919
def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            answer = '김서방은 %d에 있다' %(i)
            break
    return answer
