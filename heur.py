def arrangePriorities(p1_hp,p1_mp,ai_hp,ai_mp,ai_hand):
	# set the priorities of the elements
	# 1 = Fire(2); 2 = Water(2); 3 = Wind(3); 4 = Earth(3); 5 = Pass
	priorities = {}
	# set len of priorities according to number of cards in hand
	for num in xrange(1,len(ai_hand)+1):
		priorities[num] = None

	# lethal is the highest prio
	if p1_hp == 4 and p1_mp < 3 and "3" in ai_hand:
		priorities = assignPrio(priorities,"3")
		# set the estimated  mp
		ai_mp -=3

	# self preservation second prio
	if ai_hp <= 4 and ai_mp >= 2 and "2" in ai_hand:
		priorities = assignPrio(priorities,"2")
		# set the estimated hp and mp
		ai_hp += 3
		ai_mp -=2
	# in case water is not in hand use earth or p1 can use wind
	if (ai_hp <= 4 and ai_mp >= 2 and "4" in ai_hand) or (ai_mp >=3 and "4" in ai_hand and p1_mp >=3):
		priorities = assignPrio(priorities,"4")
		ai_mp -=3
	# default fire if available and has mp
	if ai_mp >= 2 and "1" in ai_hand:
		priorities = assignPrio(priorities,"1")
		ai_mp-=2

	
	return priorities


# dynamic assigning of priorities
def assignPrio(priorities, value):
	for key in priorities:
		if priorities[key] is None:
			priorities[key] = value
			break
	return priorities

p1_hp = 20
p1_mp = 20
ai_hp = 20
ai_mp = 10
ai_hand = ["1","2","3","4"]

print arrangePriorities(p1_hp,p1_mp,ai_hp,ai_mp,ai_hand)