 
board = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    bucket = []

    for m in moves:
        for b in range(len(board)):
            if board[b][m-1]>0:
                bucket.append(board[b][m-1])
                board[b][m-1] = 0;
                if bucket[-1:] == bucket[-2:-1]:
                    bucket = bucket[:-2]
                    answer+=2 
                break;
    return answer

result = solution(board,moves)
print(result)
