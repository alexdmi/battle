import entity

heroes = entity.load('heroes.dat')
print("Loaded {0} heroes.".format(len(heroes)))
for hero in heroes:
    print(hero)
    if hero.abilities != None:
        for ability in hero.abilities:
            print(ability.name)
