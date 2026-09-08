class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        cc = image[sr][sc]
        if cc == color:
            return image
        rows, cols = len(image), len(image[0])

        def fill(r, c):
            # 왜 이걸 생각을 못했을까...
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != cc:
                return
            image[r][c] = color
            fill(r+1, c)
            fill(r-1, c)
            fill(r, c+1)
            fill(r, c-1)

        fill(sr, sc)
        return image