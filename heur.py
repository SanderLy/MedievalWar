import itertools

def arrangePriorities(p1_hp,p1_mp,ai_hp,ai_mp,ai_hand):
	# set the priorities of the elements
	# 1 = Fire(2); 2 = Water(2); 3 = Wind(3); 4 = Earth(3); 5 = Pass
	priorities = list(ai_hand)



	# lethal is the highest prio (wind)
	if p1_hp == 4 and p1_mp < 3 and "3" in ai_hand and ai_mp >= 3:
		index = priorities.index("3")
		priorities[index] = priorities[0]
		priorities[0] = "3"

		# set the estimated  mp
		ai_mp -=3
		p1_hp -= 4
		hueristic = 999
		return [hueristic , priorities]
	# lethal is the highest prio (fire)
	elif p1_hp == 2 and "1" in ai_hand and ai_mp >= 2:
		index = priorities.index("1")
		priorities[index] = priorities[0]
		priorities[0] = "1"
		# set the estimated  mp
		ai_mp -=2
		p1_hp -= 2
		hueristic = 999
		return [hueristic , priorities]
	# self preservation second prio
	elif ai_hp <= 4 and ai_mp >= 2 and "2" in ai_hand:
		index = priorities.index("2")
		priorities[index] = priorities[0]
		priorities[0] = "2"
		# set the estimated hp and mp
		ai_hp += 3
		ai_mp -=2
		hueristic = 999
		return [hueristic , priorities]
	# in case water is not in hand use earth or p1 can use wind
	elif (ai_hp <= 4 and ai_mp >= 2 and "4" in ai_hand) or (ai_mp >=3 and "4" in ai_hand and p1_mp >=3):
		index = priorities.index("4")
		priorities[index] = priorities[0]
		priorities[0] = "4"
		ai_mp -=3
		hueristic = 999
		return [hueristic , priorities]
	else:
		for card in ai_hand:
			if card == "1":
				ai_mp-=2
				p1_hp-=2
			if card == "2":
				ai_mp-=2
				ai_hp+=3
			if card == "3":
				ai_mp -= 3
				p1_hp -= 4
			if card == "4":
				ai_mp -= 3
		hueristic = (ai_hp*.7+ai_mp*.3)-(p1_hp*.7+p1_mp*.3)
		return [hueristic , ai_hand]
	return [hueristic , ai_hand]

# main function 
def setHand(p1_hp,p1_mp,ai_hp,ai_mp,ai_hand):
	# get all hueristics for the hand
	heur = {}
	for num in xrange(1,len(ai_hand)+1):
		perm = list(itertools.permutations(ai_hand,num))
		for item in perm:
			temp = arrangePriorities(p1_hp,p1_mp,ai_hp,ai_mp,item)
			heur[temp[0]] = temp[1]
	x1 = max(heur.keys(), key=int) #index of the greatest hueristic value
	return heur[x1]

# sample values
p1_hp = 2
p1_mp = 0
ai_hp = 20
ai_mp = 10

ai_hand = ["2","3","1"]

# print setHand(p1_hp,p1_mp,ai_hp,ai_mp,ai_hand)