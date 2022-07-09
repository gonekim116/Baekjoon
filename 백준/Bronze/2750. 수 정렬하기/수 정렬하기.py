n=int(input())
arr = []
for _ in range(n):
	arr.append(int(input()))
arr.sort()
print('\n'.join([str(i) for i in arr]))