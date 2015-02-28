import json
from status import *
from ability import *

class Entity(object):
    def __init__(self, name, health, mana, abilities):
        self.name = name
        self.health = health
        self.mana = mana
        self.abilities = abilities
        self.buffs = StatusList()
        self.debuffs = StatusList()

    def __str__(self):
        return "{0} {1} {2}".format(self.name, self.health, self.mana)

    def use_ability(self, enemy, ability):
        if ability.kind == AbilityKind.Attack:
            damage = min(enemy.health, ability.damage)
            enemy.health -= damage
            print("{0} has done {1} damage to {2}\n{2} has {3} health remaining".format(self.name, damage, enemy.name, enemy.health))
        elif ability.kind == AbilityKind.Stun:
            pass
        elif ability.kind == AbilityKind.Bleed:
            pass

def load(filename):
    data = None
    with open(filename) as f:
        data = json.load(f)

    loaded_entities = []
    for e in data:

        alist = None
        if 'abilities' in e:
          alist = AbilityList()
          for a in e['abilities']:
            alist.append(Ability(a['name'], AbilityKind[a['kind']], a['damage'], a['duration'], a['cooldown']))

        ent = Entity(e['name'], e['health'], e['mana'], alist)
        loaded_entities.append(ent)
    return loaded_entities