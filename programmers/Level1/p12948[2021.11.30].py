# 프로그래머스 파이썬 핸드폰 번호 가리기
# https://programmers.co.kr/learn/courses/30/lessons/12948
def solution(phone_number):
    answer = ''
    for i in range(len(phone_number) - 4):
        answer += '*'
    for i in range(len(phone_number) - 4, len(phone_number)):
        answer += phone_number[i]
    return answer
