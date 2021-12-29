# 프로그래머스 파이썬 이상한 문자 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12930
def solution(s):
    lst = s.split(' ')
    a = []
    for i in lst:
        s = ''
        for j in range(len(i)):
            s += i[j].upper() if j%2==0 else i[j].lower()
        a.append(s)
    answer = ' '.join(a)
    return answer
