import re

class Solution:
    def parseMultiplication(self, mul: str) -> (int, int):
        pattern = r"mul\((\d+),(\d+)\)"
        match = re.search(pattern, mul)
        return int(match[1]), int(match[2])

    def scanCorruptedMemory(self, corruptedMemory: str) -> int:
        pattern = r"mul\(\d+,\d+\)"
        matches = re.findall(pattern, corruptedMemory)

        multiplies = 0
        for match in matches:
            numbers = self.parseMultiplication(match)
            multiplies += numbers[0] * numbers[1]


        return multiplies

print(f"The answer is {Solution().scanCorruptedMemory(open('input.txt').read())}")