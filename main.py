import hero
import enemy
from entity import *
def select_entity(prompt, entities):
	i = 1
	for h in entities:
		print("{0}. {1}".format(i, h.name))
		i += 1
	choice = int(input("Select your {0}: ".format(prompt)))
	return entities[choice-1]

def player_turn(player, enemy):
	while True:
		i = 1
		for a in player.abilities:
			isCooldown = player.abilities.on_cooldown(i-1)
			if isCooldown > 0:
				print("{0}. {1} ({2} cooldown remaining)".format(i, a.name, isCooldown))
			else:
				print("{0}. {1}".format(i, a.name))
			i += 1
		choice = int(input("Select your ability: "))
		notcooldown = player.abilities.use(choice-1)

		if not notcooldown:
			print("That ability is on cooldown.")
			continue

		player.use_ability(enemy, player.abilities[choice-1])
		break

def enemy_turn(enemy):
	index = 0
	for i in reversed(range(len(enemy.abilities))):
		if enemy.abilities.use(i):
			index = i
			break
	enemy.use_ability(player, enemy.abilities[index])

player = select_entity("hero", hero.heroes)
enemy = select_entity("opponent", enemy.enemies)
print("{0} vs {1}".format(player.name, enemy.name))


def print_health(player, enemy):
	max_characters = max(len(player.name), len(enemy.name))
	print("-"*(10 + max_characters))
	print("| {0:<{width}} | {1:>3} |".format(player.name, player.health, width=max_characters))
	print("| {0:<{width}} | {1:>3} |".format(enemy.name, enemy.health, width=max_characters))
	print("-"*(10 + max_characters))

isPlayerTurn = True
while True:
	print_health(player, enemy)
	if isPlayerTurn:
		player.abilities.tick()
		player.buffs.tick()
		player.debuffs.tick()

		player.apply_buffs(enemy)
		incapacitated = player.apply_debuffs(enemy)

		if not incapacitated:
			player_turn(player, enemy)
		isPlayerTurn = False
	else:
		enemy.abilities.tick()
		enemy.buffs.tick()
		enemy.debuffs.tick()

		enemy.apply_buffs(player)
		incapacitated = enemy.apply_debuffs(player)

		if not incapacitated:
			enemy_turn(enemy)
		isPlayerTurn = True

	if player.health == 0 or enemy.health == 0:
		if player.health == 0:
			print("You lost ):")
		if enemy.health == 0:
			print("You won!")
		break