import random


def existsPair(first6):
	for i in first6:
		if first6.count(i) > 1:
			return True
	return False

deck = range(13)*4

count = 0
for i in range(100):
	random.shuffle(deck)
	if existsPair(deck[:7]):
		print deck[:7] 
		count+=1

print count


