import entity

enemies = entity.load('enemies.dat')
print("Loaded {0} enemies.".format(len(enemies)))
for enemy in enemies:
    print(enemy)
