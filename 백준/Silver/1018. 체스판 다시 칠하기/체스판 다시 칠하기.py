n,m=map(int,input().split())
board = []
for _ in range(n):
	board.append(input())

n_range = range(n-7)
m_range = range(m-7)

min_total = 64
for a in n_range:
	for b in m_range:
		count, reverse_count = 0, 0
		for i in range(a,a+8):
			for j in range(b,b+8):
				if (i+j) % 2 == 0:
					if board[i][j] == 'W':
						count += 1
					else:
						reverse_count += 1
				if (i+j) % 2 == 1:
					if board[i][j] == 'B':
						count += 1
					else:
						reverse_count += 1
		min_fix = min(count, reverse_count)
		if min_fix < min_total:
			min_total = min_fix
print(min_total)