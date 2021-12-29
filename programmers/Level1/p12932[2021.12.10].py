# 프로그래머스 파이썬 자연수 뒤집어 배열로 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12932
def solution(n):
    answer = []
    n = str(n)
    for i in reversed(range(len(n))):
        answer.append(int(n[i]))
    return answer
