from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        DIRECTIONS = [(0,1), (0,-1),(1,0), (-1,0)]
        row = len(maze)
        col = len(maze[0])
        visited = [[False for _ in range(col)] for _ in range(row)]

        def dfs(maze, r, c):
            if [r, c] == destination:
                return True
            for dr, dc in DIRECTIONS:
                nr = r + dr
                nc = c + dc
                # print(dr, dc, [nr,nc])
                while 0 <= nr < row and 0 <= nc < col and maze[nr][nc] == 0:
                    nr += dr
                    nc += dc
                nr -= dr
                nc -= dc
                
                if visited[nr][nc] == False:
                    visited[nr][nc] = True
                    # print(nr,nc)
                    if dfs(maze, nr, nc) == True:
                        return True
            return False
        return dfs(maze, start[0], start[1])

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
    


