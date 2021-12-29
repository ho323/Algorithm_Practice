# 프로그래머스 파이썬 문자열 다루기 기본
# https://programmers.co.kr/learn/courses/30/lessons/12918
def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            return True
        else:
            return False
    else:
        return False