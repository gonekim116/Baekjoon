n=int(input())
data = []
for _ in range(n):
	data.append(tuple(map(int,input().split())))

ranking = []
for i in range(n):
	smaller_than = 0
	for j in range(n):
		if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
			smaller_than += 1
	ranking.append(smaller_than+1)
print(' '.join([str(r) for r in ranking]))