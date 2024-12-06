import collections
from typing import List, Dict, Tuple, Set

def readFile(file: str) -> Tuple[List[Tuple[int, int]], List[List[int]]]:
    # Initialize structures for the two sections
    pageOrderingRules = []
    printQueues = []

    with open(file, 'r') as file:
        lines = file.readlines()

    # Split sections using the empty line as a separator
    sections = ''.join(lines).split("\n\n")

    if len(sections) >= 2:
        # Parse the first section: key-value pairs
        for line in sections[0].strip().split('\n'):
            key, value = map(int, line.split('|'))
            pageOrderingRules.append((key, value))

        # Parse the second section: list of lists of integers
        for line in sections[1].strip().split('\n'):
            numbers = list(map(int, line.split(',')))
            printQueues.append(numbers)

    return pageOrderingRules, printQueues

class Solution:
    def isCorrectPrintQueue(self, orderingRules: Dict[int, Set[int]], printQueue: List[int]) -> bool:
        previousPages = set()
        for page in printQueue:
            for prevPage in previousPages:
                if prevPage in orderingRules[page]:
                    return False
            previousPages.add(page)
        return True

    def processCorrectPrintQueues(self, pageOrderingRules: List[Tuple[int, int]], printQueues: List[List[int]]) -> int:
        orderingRules = collections.defaultdict(set)
        for firstPage, latterPage in pageOrderingRules:
            orderingRules[firstPage].add(latterPage)

        correctPrintQueues = [printQueue for printQueue in printQueues if self.isCorrectPrintQueue(orderingRules, printQueue)]

        middleValuesOfCorrectPrintQueues = []
        for printQueue in correctPrintQueues:
            middleValuesOfCorrectPrintQueues.append(printQueue[len(printQueue) // 2])

        return sum(middleValuesOfCorrectPrintQueues)


print(f"The answer is {Solution().processCorrectPrintQueues(*readFile('input.txt'))}")