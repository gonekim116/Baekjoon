import sys
from collections import Counter
n=int(input())
arr = []
for _ in range(n):
	arr.append(int(sys.stdin.readline()))
avg = round(sum(arr)/n)
print(avg)
arr.sort()
print(arr[int((n-1)/2)])
counted = Counter(arr).most_common()
if len(counted) > 1:
    if counted[0][1] == counted[1][1]:
        print(counted[1][0])
    else:
        print(counted[0][0])
else:
    print(counted[0][0])
print(max(arr)-min(arr))