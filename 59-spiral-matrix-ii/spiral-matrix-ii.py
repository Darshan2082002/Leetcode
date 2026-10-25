class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        result = [[0] * n for _ in range(n)]
        row = col = 0
        direction = [0, 1, 0, -1, 0] 
        direction_index = 0
        
        for j in range(1, n * n + 1):
            result[row][col] = j 
            
            # Predict the next cell by adding current position to direction delta
            n_row = row + direction[direction_index]
            n_col = col + direction[direction_index + 1]

            # If out of bounds or already filled, turn 90 degrees right
            if (n_row < 0 or n_row >= n or 
                n_col < 0 or n_col >= n or 
                result[n_row][n_col] != 0):
                direction_index = (direction_index + 1) % 4

            # Step forward in the final chosen direction
            row += direction[direction_index]
            col += direction[direction_index + 1]
            
        return result