import math
n = int(input())
for i in range(n):
  a,b = list(map(int, input().split()))
  d = b-a
  margin = int(math.ceil(math.sqrt(d)))
  if margin**2 - d < margin:
    print(margin*2-1)
  else:
    print(margin*2-2)