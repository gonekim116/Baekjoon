def hanoi(n,start,end):
	if n==1:
		return [(start,end)]

	moves = []
	pillar = [1,2,3]
	pillar.remove(start)
	pillar.remove(end)
	
	pre_start, pre_end = start, pillar[0]
	post_start, post_end = pre_end, end
		
	premoves = hanoi(n-1,pre_start,pre_end)
	postmoves = hanoi(n-1,post_start,post_end)
	for m in premoves:
		moves.append(m)
	moves.append((start,end))
	for m in postmoves:
		moves.append(m)
	return moves

l = []
for pair in hanoi(int(input()),1,3):
	l.append(' '.join(list(map(str,pair))))
print(len(l),'\n'.join(l),sep='\n')