n = int(input())
m = int(input())
if n>m: print(-1)
import math
li = list(range(n,m+1))
for i in range(n,m+1):
  if i==1: li.remove(i)
  if i==2: continue
  for j in range(2, int(math.sqrt(i))+1):
    if i % j == 0:
      li.remove(i)
      break
if len(li) == 0: print(-1)
else:
  print(sum(li), min(li), sep='\n')