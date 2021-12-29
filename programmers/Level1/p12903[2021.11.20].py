# 프로그래머스 파이썬 가운데 글자 가져오기
# https://programmers.co.kr/learn/courses/30/lessons/12903
def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        n = int(len(s) / 2)
        answer = s[n-1] + s [n]
    else:
        n = int(len(s) / 2)
        answer = s[n]
    return answer
