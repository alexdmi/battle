import hero
import enemy

def select_entity(prompt, entities):
	i = 1
	for h in entities:
		print("{0}. {1}".format(i, h.name))
		i += 1
	choice = int(input("Select your {0}: ".format(prompt)))
	return entities[choice-1]

def player_turn(player):
	while True:
		i = 1
		for a in player.abilities:
			print("{0}. {1}".format(i, a.name))
			i += 1
		choice = int(input("Select your ability: "))
		didWork = player.abilites.use(choice-1)

		# Affect the enemy
		ability.use_on(player, enemy)

		ability.use_on(enemy, player)

		if didWork:
			break

def enemy_turn(enemy):
	pass

player = select_entity("hero", hero.heroes)
enemy = select_entity("opponent", enemy.enemies)
print("{0} vs {1}".format(player.name, enemy.name))

isPlayerTurn = True
while True:
	if isPlayerTurn:
		player_turn(player)
		isPlayerTurn = False
	else:
		enemy_turn(enemy)
		isPlayerTurn = True

	break

	if player.health == 0 or enemy.health == 0:
		break