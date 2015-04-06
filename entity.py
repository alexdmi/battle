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
            self.damage_ability(enemy, ability)

        elif ability.kind == AbilityKind.Stun:
            if ability.damage > 0:
                self.damage_ability(enemy, ability)
            enemy.debuffs.append(Status(ability.name, ability.kind, ability.damage, ability.duration))
            print("{0} is now stunned!".format(enemy.name))

        elif ability.kind == AbilityKind.Bleed:
            enemy.debuffs.append(Status(ability.name, ability.kind, ability.damage, ability.duration))
            print("{0} has started to bleed".format(enemy.name))

        elif ability.kind == AbilityKind.Burn:
            enemy.debuffs.append(Status(ability.name, ability.kind, ability.damage, ability.duration))
            print("{0} has got a nasty burn...".format(enemy.name))

        elif ability.kind == AbilityKind.Lifelink:
            self.buffs.append(Status(ability.name, ability.kind, ability.damage, ability.duration))
            print("{0} has started to drain life from {1}".format(self.name, enemy.name))

        elif ability.kind == AbilityKind.Heal:
            self.buffs.append(Status(ability.name, ability.kind, ability.damage, ability.duration))
            print("{0} has begun to heal themselves!".format(self.name))

    def damage_ability(self, enemy, ability):
        damage = min(enemy.health, ability.damage)
        enemy.health -= damage
        print("{0} has done {1} damage to {2}".format(self.name, damage, enemy.name))

    def apply_buffs(self, enemy):
        for buff in self.buffs:
            if buff.kind == AbilityKind.Heal:
                self.health += buff.damage
                print("{0} has healed for {1}".format(self.name, buff.damage))
            elif buff.kind == AbilityKind.Lifelink:
                enemy.health -= buff.damage
                self.health += buff.damage
                print("{0} has stolen {1} life from {2}".format(self.name, buff.damage, enemy.name))
    
    def apply_debuffs(self, enemy):
        incapacitated = False
        for debuff in self.debuffs:
            if debuff.kind == AbilityKind.Stun:
                print("{0} is still stunned".format(self.name))
                incapacitated = True
            elif debuff.kind == AbilityKind.Bleed:
                self.health -= debuff.damage
                print("{0} bleeds for {1}".format(self.name, debuff.damage))
            elif debuff.kind == AbilityKind.Burn:
                self.health -= debuff.damage
                print("{0} has started to take damage form they're burn! They take {1} damage.".format(self.name, debuff.damage))


        return incapacitated

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