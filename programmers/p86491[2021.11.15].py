# 프로그래머스 파이썬 최소직사각형
# https://programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    sizes = [sorted(size, reverse=True) for size in sizes]

    widths = [size[0] for size in sizes]
    heights = [size[1] for size in sizes]
    
    widht = max(widths)
    height = max(heights)
    
    answer = widht * height
    
    return answer
