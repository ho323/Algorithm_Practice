# 프로그래머스 크레인 인형뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    answer = 0
    basket = [0]
    for i in moves:
        for j in board:
            if j[i-1] != False:
                if basket[-1] != j[i-1]:
                    basket.append(j[i-1])
                else:
                    basket.pop(-1)
                    answer+=2
                j[i-1] = 0
                break
                
    return answer
