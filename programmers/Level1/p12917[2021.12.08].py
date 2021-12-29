# 프로그래머스 파이썬 문자열 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12917
def solution(s):
    return (''.join(reversed(sorted(s))))
