from typing import List

def readInput(file: str) -> List[List[int]]:
    allLevels = []
    with open(file, 'r') as file:
        for line in file:
            levels = [int(level) for level in line.strip().split(" ")]
            allLevels.append(levels)
    return allLevels

class Solution:
    def isIncreasingSafe(self, levels: List[int]) -> bool:
        stack = [levels[0]]
        index = 1
        while index < len(levels) and stack[-1] < levels[index]:
            diff = levels[index] - stack[-1]
            if diff < 1 or diff > 3:
                break
            stack.append(levels[index])
            index += 1
        return index == len(levels)

    def isDecreasingSafe(self, levels: List[int]) -> bool:
        stack = [levels[0]]
        index = 1
        while index < len(levels) and stack[-1] > levels[index]:
            diff = stack[-1] - levels[index]
            if diff < 1 or diff > 3:
                break
            stack.append(levels[index])
            index += 1
        return index == len(levels)

    def countSafeLevels(self, allLevels: List[List[int]]):
        safeLevelsCount = 0
        for levels in allLevels:
            if self.isIncreasingSafe(levels) or self.isDecreasingSafe(levels):
                safeLevelsCount += 1
        return safeLevelsCount

print(f"The answer is {Solution().countSafeLevels(readInput('input.txt'))}")

