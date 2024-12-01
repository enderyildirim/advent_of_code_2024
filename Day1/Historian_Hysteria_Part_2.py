import collections

left = []
right = []
with open('input.txt', 'r') as file:
    for line in file:
        fields = line.strip().split("   ")  # Split using the custom delimiter
        left.append(int(fields[0]))
        right.append(int(fields[1]))


countMap = collections.defaultdict(int)
for num in right:
    countMap[num] += 1

ans = 0
for num in left:
    ans += num * (countMap[num] if num in countMap else 0)

print(f"The answer is {ans}")
