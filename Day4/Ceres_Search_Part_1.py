from typing import List, Set


def readInput(file: str) -> List[str]:
    rows = []
    with open(file, 'r') as file:
        for line in file:
            rows.append(line.strip())
    return rows

class Solution:
    def __init__(self):
        self.searchWord = "XMAS"
        self.wordCount = 0
        self.xmasMatrix = None
        self.directionMat = [[  1,  1 ], # ↘ Down-Right
                             [  1, -1 ], # ↙ Down-Left
                             [ -1, -1 ], # ↖ Up-Left
                             [ -1,  1 ], # ↗ Up-Right
                             [  1,  0 ], # ↓ Down
                             [  0,  1 ], # → Right
                             [ -1,  0 ], # ↑ Up
                             [  0, -1 ]] # ← Left

    def countXmasRecursively(self, xmasMatrix: List[str], row: int, col: int, searchIndex: int, direction: List[int]) -> None:
        if row < 0 or row >= len(xmasMatrix) or col < 0 or col >= len(xmasMatrix[0]):
            return

        if xmasMatrix[row][col] != self.searchWord[searchIndex]:
            return

        if searchIndex == len(self.searchWord) - 1:
            self.wordCount += 1
            return

        nextRow, nextCol = row + direction[0], col + direction[1]
        self.countXmasRecursively(xmasMatrix, nextRow, nextCol, searchIndex + 1, direction)

    def countXmas(self, xmasMatrix: List[str]) -> int:
        for row in range(len(xmasMatrix)):
            for col in range(len(xmasMatrix[0])):
                for direction in self.directionMat:
                    self.countXmasRecursively(xmasMatrix, row, col, 0, direction)
        return self.wordCount

print(f"The answer is {Solution().countXmas(readInput('input.txt'))}")
