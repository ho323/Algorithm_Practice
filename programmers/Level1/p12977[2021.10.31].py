# 프로그래머스 파이썬 소수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12977
from itertools import combinations

def primeNumber(num) :
    for i in range(2, num) :
        if num % i == 0 :
            return False
    return True


def solution(nums):
    case = []
    sum_case = []
    count = 0
    for i in list(combinations(nums,3)):
        case.append(sum(i))
    for i in case :
        if primeNumber(i) :
            count += 1
    return count
