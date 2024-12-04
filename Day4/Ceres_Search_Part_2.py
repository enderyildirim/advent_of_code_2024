from typing import List


def readInput(file: str) -> List[str]:
    rows = []
    with open(file, 'r') as file:
        for line in file:
            rows.append(line.strip())
    return rows

class Solution:
    def __init__(self):
        self.directionMat = [[ -1, -1 ], # ↖ Up-Left
                             [  0,  0 ], # Stay (no movement)
                             [  1,  1 ], # ↘ Down-Right
                             [  1, -1 ], # ↙ Down-Left
                             [  0,  0 ], # Stay (no movement)
                             [ -1,  1 ]] # ↗ Up-Right

    def isXmasShape(self, xmasMatrix: List[str], row: int, col: int) -> bool:
        def isXmas(chars: List[str]) -> bool:
            joined = "".join(chars)
            return joined == "MAS" or joined == "SAM"

        if 0 < row < (len(xmasMatrix) - 1) and 0 < col < (len(xmasMatrix[row]) - 1):
            charSequence1 = []
            for direction in self.directionMat[:3]:
                newRow, newCol = row + direction[0], col + direction[1]
                charSequence1.append(xmasMatrix[newRow][newCol])

            charSequence2 = []
            for direction in self.directionMat[3:]:
                newRow, newCol = row + direction[0], col + direction[1]
                charSequence2.append(xmasMatrix[newRow][newCol])

            return isXmas(charSequence1) and isXmas(charSequence2)

        return False

    def countXmas(self, xmasMatrix: List[str]) -> int:
        shapeCount = 0
        for row in range(len(xmasMatrix)):
            for col in range(len(xmasMatrix[0])):
                if self.isXmasShape(xmasMatrix, row, col):
                    shapeCount += 1
        return shapeCount

print(f"The answer is {Solution().countXmas(readInput('input.txt'))}")
