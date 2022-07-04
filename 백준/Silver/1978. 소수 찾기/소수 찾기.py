n = int(input())
import math
count = 0
for i in list(map(int, input().split())):
  if i == 1: count += 1; continue
  if i == 2: continue
  for j in range(2, int(math.sqrt(i))+1):
    if i % j == 0:
      count += 1
      break
print(n-count)