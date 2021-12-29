# 프로그래머스 파이썬 2016년
# https://programmers.co.kr/learn/courses/30/lessons/12901
def solution(a, b):
    answer = ''
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    weeks = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
    days = sum(month[:a-1]) + b - 1
    
    answer = weeks[days % 7]
    
    return answer
