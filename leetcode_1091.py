from typing import List
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        total_row = len(grid) - 1
        total_col = len(grid[0]) - 1
        direction = [(1,0,), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (-1,-1), (1,-1)]

        def next_node(curr_row, curr_col, que, dist):
            for r, c in direction:
                next_row = curr_row + r
                next_col = curr_col + c
                if 0 <= next_row <= total_row and 0 <= next_col <= total_col:
                    if grid[next_row][next_col] != 0:
                        continue
                    else:
                        grid[next_row][next_col] = dist
                        que.append((next_row, next_col))
        
        if grid[0][0] != 0 or grid[total_row][total_col] != 0:
            return -1

        que = deque()
        que.append((0,0))
        grid[0][0] = 1

        while que:
            curr_row, curr_col = que.popleft()
            dist = grid[curr_row][curr_col]
            if (curr_row, curr_col) == (total_row, total_col):
                return dist
            else:
                next_node(curr_row, curr_col, que, dist + 1)
        return -1
