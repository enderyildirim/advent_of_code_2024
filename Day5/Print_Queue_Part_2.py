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

    def findMiddleInIncorrectPrintQueue(self, orderingRules: Dict[int, Set[int]], printQueue: List[int]) -> int:
        def hasToBeBefore(page1: int, page2: int):
            return page2 in orderingRules[page1]

        for i, page in enumerate(printQueue):
            beforePageCount = 0
            for j, anotherPage in enumerate(printQueue):
                if i != j and hasToBeBefore(page, anotherPage):
                    beforePageCount += 1

            if beforePageCount == len(printQueue) // 2:
                return printQueue[i]

    def processCorrectPrintQueues(self, pageOrderingRules: List[Tuple[int, int]], printQueues: List[List[int]]) -> int:
        orderingRules = collections.defaultdict(set)
        for firstPage, latterPage in pageOrderingRules:
            orderingRules[firstPage].add(latterPage)

        incorrectPrintQueues = [printQueue for printQueue in printQueues if not self.isCorrectPrintQueue(orderingRules, printQueue)]
        middlesOfIncorrectPrintQueues = [self.findMiddleInIncorrectPrintQueue(orderingRules, printQueue) for printQueue in incorrectPrintQueues]
        return sum(middlesOfIncorrectPrintQueues)


print(f"The answer is {Solution().processCorrectPrintQueues(*readFile('input.txt'))}")