
left = []
right = []
with open('input.txt', 'r') as file:
    for line in file:
        fields = line.strip().split("   ")
        left.append(int(fields[0]))
        right.append(int(fields[1]))

left.sort()
right.sort()
index = 0
ans = 0
while index < len(left):
    ans += abs(left[index] - right[index])
    index += 1

print(f"The answer is {ans}")
