from collections import deque
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        def bfs(maze, start,destination):
            DIRECTIONS = [(0,1), (0,-1),(1,0), (-1,0)]
            row = len(maze)
            col = len(maze[0])
            visited = [[False for _ in range(col)] for _ in range(row)]

            queue =[ (start[0], start[1])]
            visited[start[0]][start[1]]
            while queue:
                r, c = queue.pop(0)
                if [r, c] == destination:
                    return True
                for dr, dc in DIRECTIONS:
                    nr = r + dr
                    nc = c + dc
                    while 0 <= nr < row and 0 <= nc < col and maze[nr][nc] == 0:
                        nr += dr
                        nc += dc
                    nr -= dr
                    nc -= dc
                    if visited[nr][nc] == False:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
            return False
        return bfs(maze, start,destination)

if __name__ == "__main__":
    solution = Solution()
    # test 1
    res = solution.hasPath([[0,0,1,0,0],
                            [0,0,0,0,0],
                            [0,0,0,1,0],
                            [1,1,0,1,1],
                            [0,0,0,0,0]],
                           [0,4],[4,4])
    print(res)
    # test 2
    res = solution.hasPath([[0,0,1,0,0],
                            [0,0,0,0,0],
                            [0,0,0,1,0],
                            [1,1,0,1,1],
                            [0,0,0,0,0]]
                            ,[0,4],[3,2])
    print(res)
    # test 3
    res = solution.hasPath([[0,0,0,0,0],
                            [1,1,0,0,1],
                            [0,0,0,0,0],
                            [0,1,0,0,1],
                            [0,1,0,0,0]]
                            ,[4,3], [0,1])
    print(res)
    


