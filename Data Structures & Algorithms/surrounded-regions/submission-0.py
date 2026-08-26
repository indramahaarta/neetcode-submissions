from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:

        def bfs(row, col):
            print("bfs ", row, col)
            q = deque([(row, col)])
            visited = set()

            has_edge = False
            while q:
                N = len(q)
                for _ in range(N):
                    row, col = q.popleft()
                    
                    if (row, col) in visited:
                        continue
                    
                    if row == 0 or row == len(board) - 1 or col == 0 or col == len(board[row]) - 1:
                        has_edge = True
                    
                    visited.add((row, col))

                    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    for r, c in directions:
                        r, c = r + row, c + col

                        if r < 0 or c < 0 or r >= len(board) or c >= len(board[r]) or board[r][c] != 'O':
                            continue
                        
                        q.append((r, c))
                            

            for row, col in visited:
                if has_edge:
                    board[row][col] = 'T'
                else:
                    board[row][col] = 'F'
            

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 'O':
                    bfs(row, col)
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 'T':
                    board[row][col] = 'O'
                elif board[row][col] == 'F':
                    board[row][col] = 'X'


        