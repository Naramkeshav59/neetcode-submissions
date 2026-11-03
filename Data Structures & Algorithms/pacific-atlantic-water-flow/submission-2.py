class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        def dfs(r, c, vis, prev):
            if(r < 0 or c < 0 or 
            r > len(heights) - 1 or c > len(heights[0]) - 1 or
            heights[r][c] < prev or (r,c) in vis):
                return

            vis.add((r,c))

            dfs(r + 1, c, vis, heights[r][c])
            dfs(r - 1, c, vis, heights[r][c])
            dfs(r, c + 1, vis, heights[r][c])
            dfs(r, c - 1, vis, heights[r][c])
        for r in range(len(heights)):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, len(heights[0]) - 1, atl, heights[r][len(heights[0]) - 1])
        for c in range(len(heights[0])):
            dfs(0, c, pac, heights[0][c])
            dfs(len(heights) - 1, c, atl, heights[len(heights) - 1][c])
        
        return [list(i) for i in atl.intersection(pac)]

