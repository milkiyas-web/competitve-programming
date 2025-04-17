# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dirr = [(0,1), (1,0), (-1, 0), (0, -1)]
        de = deque([(sr,sc)])
        n = len(image)
        m = len(image[0])
        original_color = image[sr][sc]

        if original_color == color:
            return image
        while de:
            r,c = de.popleft()
            if image[r][c] == original_color:
                image[r][c] = color
            for a, b in dirr:
                nr = r+a
                nc = c+b
                if 0<=nr<n and 0<=nc<m and image[nr][nc] == original_color:
                    de.append((nr, nc))

        return image





