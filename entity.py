import json
import status
from ability import *

class Entity(object):
  def __init__(self, name, health, mana, abilities):
    self.name = name
    self.health = health
    self.mana = mana
    self.abilities = abilities
    self.buffs = status.StatusList()
    self.debuffs = status.StatusList()

  def __str__(self):
    return "{0} {1} {2}".format(self.name, self.health, self.mana)

  def use_ability(self, enemy, ability):
    # 1. Switch on what kind the ability is
    # 2. Execute the ability
    #    2a. If it's damage, apply damage to enemy
    #    2b. If it's an effect, apply effect to enemy
    
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
            alist.append(Ability(a['name'], a['kind'], a['damage'], a['duration'], a['cooldown']))

        ent = Entity(e['name'], e['health'], e['mana'], alist)
        loaded_entities.append(ent)
    return loaded_entities