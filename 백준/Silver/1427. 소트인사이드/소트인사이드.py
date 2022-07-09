unsorted = input()
arr = []
for _ in range(len(unsorted)):
	arr.append(unsorted[_])
arr = list(map(int,arr))
arr.sort(reverse=True)
print(''.join(list(map(str,arr))))