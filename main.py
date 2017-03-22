from random import randint
import random
import heur
# show the game mechanics
print '''
======================================
How to play
======================================

Both players start with 20 HP and 3 MP.
Every turn, both players gain 1 MP and gain one random element.
Both players start with 3 random elements.
First player to reach 0 HP loses the game.

======================================
Weapons
======================================

Sword beats Wand
Wand beats Shield
Shield beats Sword
i.e. Sword > Wand > Shield > Sword

======================================
Elements
======================================

Fire (2 MP): Deal additional 2 damage.
Water (2 MP): Restores 3 HP.
Wind (3 MP): Deal 4 damage but gets reflected by Earth element.
Earth (3 MP): Negates weapon and elemental damage. Also reflects Wind element.

======================================
Controls
======================================

Player will be first prompted to choose a weapon:
Q: Sword
W: Wand
E: Shield

If the player has at least 2 MP, he will be able to use an element.
0: Pass
1: Fire
2: Water
3: Wind
4: Earth
'''
# choices
weapons = {"q":"Sword","w":"Wand","e":"Shield"}
elements = ["Pass", "Fire", "Water", "Wind", "Earth"]

# initializations
player_hp = 20
player_mp = 2
cpu_hp = 20
cpu_mp = 2
player_hand = []
cpu_hand = []
game = True

# print current status of player and cpu
def show_stats(player_hp, player_mp, cpu_hp, cpu_mp, player_hand, cpu_hand):
	print '''
-----------------------------------------------------------------------
 Current Stats
-----------------------------------------------------------------------
 Player HP: %s | Player MP: %s
-----------------------------------------------------------------------
 Current Hand: %s
-----------------------------------------------------------------------
 CPU HP: %s    | CPU MP: %s
-----------------------------------------------------------------------
 CPU Hand: %s elements
----------------------------------------------------------------------- 
	''' % (player_hp, player_mp, player_hand, cpu_hp, cpu_mp, cpu_hand)

# return weapon fight winner
def weapon_win(player, cpu):
	if player == cpu:
		return 0
	if player == "Sword":
		if cpu == "Wand":
			return 1
		elif cpu == "Shield":
			return -1
	if player == "Wand":
		if cpu == "Shield":
			return 1
		elif cpu == "Sword":
			return -1
	if player == "Shield":
		if cpu == "Sword":
			return 1
		elif cpu == "Wand":
			return -1

# print weapon/element fight result
def show_battle(player_weapon, player_set, cpu_weapon, cpu_set, result_weapon, result_element):
	print """
-----------------------------------------------------------------------
 Weapon Battle
-----------------------------------------------------------------------
 Player Weapon: %s | CPU Weapon: %s
-----------------------------------------------------------------------
 Result: %s
-----------------------------------------------------------------------
 Element Battle
-----------------------------------------------------------------------
 Player Element: %s | CPU Element: %s
-----------------------------------------------------------------------
 Result: 
 %s
-----------------------------------------------------------------------
	""" % (player_weapon, cpu_weapon, result_weapon, player_set, cpu_set, result_element)

# damage and mp computations for element-related things
def element_battle(player_set, cpu_set):
	global player_hp
	global cpu_hp
	global cpu_mp
	global cpu_hand
	result = ""
	player_total_damage = 0
	player_total_restore = 0
	cpu_total_damage = 0
	cpu_total_restore = 0
	cpu_earth = False
	for element in player_set:
		if element == "Fire":
			result += "Player dealt 2 fire damage. \n "
			player_total_damage += 2
		elif element == "Water":
			result += "Player gained 3 HP. \n "
			player_total_restore += 3		
		elif element == "Wind":
			result += "Player dealt 4 wind damage. \n "
			player_total_damage += 4

	for element in cpu_set:
		print cpu_mp
		if element == "Fire" and cpu_mp > 1:
			result += "CPU dealt 2 fire damage. \n "
			cpu_total_damage += 2
			cpu_mp -= 2
			cpu_hand.remove("Fire")
		elif element == "Water" and cpu_mp > 1:
			result += "CPU gained 3 HP. \n "
			cpu_total_restore += 3
			cpu_mp -= 2
			cpu_hand.remove("Water")
		elif element == "Wind" and cpu_mp > 2:
			result += "CPU dealt 4 wind damage. \n "
			cpu_total_damage += 4
			cpu_mp -= 3
			cpu_hand.remove("Wind")
		elif element == "Earth" and cpu_mp > 2:
			cpu_earth = True
			cpu_mp -= 3
			cpu_hand.remove("Earth")

	if cpu_earth:
		result += "CPU negated incoming damage. \n"
		player_total_damage = 0
		for i in range(player_set.count("Wind")):
			result += "CPU reflected 4 Wind damage. \n"
			player_hp -= 4

	if "Earth" in player_set:
		result += "Player negated incoming damage. \n"
		cpu_total_damage = 0
		for i in range(cpu_set.count("Wind")):
			result += "Player reflected 4 Wind damage. \n"
			cpu_hp -= 4
		
		

	player_hp -= cpu_total_damage
	player_hp += player_total_restore
	cpu_hp -= player_total_damage
	cpu_hp += cpu_total_restore


	return result


def determine_winner(player_hp, cpu_hp):
	if player_hp < 1 and cpu_hp < 1:
		return "DRAW"
	if player_hp < 1:
		return "CPU WINS!"
	if cpu_hp < 1:
		return "PLAYER WINS!"

for i in range(3):
	player_hand.append(elements[random.randint(1,4)])
	cpu_hand.append(elements[random.randint(1,4)])

while game:
	player_mp += 1
	cpu_mp += 1
	player_hand.append(elements[random.randint(1,4)])
	cpu_hand.append(elements[random.randint(1,4)])
	
	show_stats(player_hp, player_mp, cpu_hp, cpu_mp, player_hand, len(cpu_hand))

	flag = True
	while flag:
		player_weapon = raw_input("Choose your Weapon: ").lower()
		if player_weapon in "qwe":
			flag = False
			player_weapon = weapons[player_weapon]
		else:
			print "Please input Q, W, or E"
	
	flag = True
	first = True
	player_set = []
	cpu_set = []
	cost = 0
	while flag:
		if first:
			player_element = raw_input("Choose your Element: ")
		else:
			player_element = raw_input("Choose another Element: ")

		if player_element == "0":
			break

		if player_hand[int(player_element) - 1] == "Fire":
			player_element = "Fire"
			cost = 2
		elif player_hand[int(player_element) - 1] == "Water":
			player_element = "Water"
			cost = 2
		elif player_hand[int(player_element) - 1] == "Earth":
			player_element = "Earth"
			cost = 3
		elif player_hand[int(player_element) - 1] == "Wind":
			player_element = "Wind"
			cost = 3
		
		if player_mp >= cost:
			player_mp -= cost
			player_set.append(player_element)
			player_hand.remove(player_element)
		else:
			print "Not enough MP."

		if player_mp < 2:
			flag = False
		else:
			first = False


	# CPU decisions and actions
	cpu_weapon = weapons[random.choice('qwe')]
	cpu_set_choices = list(heur.setHand(player_hp, player_mp, cpu_hp, cpu_mp, cpu_hand))
	total_cost = 0
	for element in cpu_set_choices:
		if total_cost >= cpu_mp:
			break
		if element == "Fire":
			total_cost += 2
			cpu_set.append("Fire")
		elif element == "Water":
			total_cost += 2
			cpu_set.append("Water")
		elif element == "Wind":
			total_cost += 3
			cpu_set.append("Wind")
		elif element == "Earth":
			total_cost += 3
			cpu_set.append("Earth")




	if weapon_win(player_weapon, cpu_weapon) == 1:
		cpu_hp -= 2
		result_weapon = "Player dealt 2 damage to CPU."
	elif weapon_win(player_weapon, cpu_weapon) == -1:
		player_hp -= 2
		result_weapon = "CPU dealt 2 damage to Player."
	else:
		result_weapon = "Draw"

	show_battle(player_weapon, player_set, cpu_weapon, cpu_set, result_weapon, element_battle(player_set, cpu_set))
	
	if player_hp < 1 or cpu_hp < 1:
		game = False
		print determine_winner(player_hp, cpu_hp)
