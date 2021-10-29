# 프로그래머스 파이썬 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301?language=python3
def solution(s):
    numberList = enumerate([
        'zero','one','two','three','four','five','six','seven','eight','nine'])
    
    for num, word in numberList:
        s = s.replace(word, str(num))
        
    return int(s)
