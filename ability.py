from enum import Enum

class AbilityList(object):
  """
  A list of abilities for an entity.
  """
  def __init__(self):
    self.abilities = []
    self.cooldowns = []
  
  def append(self, ability):
    self.abilities.append(ability)
    self.cooldowns.append(0)

  def on_cooldown(self, index):
    if index >= len(self.abilities):
      raise Exception('No ability at index: {0}'.format(index))

    return self.cooldowns[index]

  def use(self, index):
    """
    Returns False if the ability could not be used, otherwise
    sets the cooldown and returns True.

    Throws an exception if the ability @ index is not available.
    """
    if index >= len(self.abilities):
      raise Exception('No ability at index: {0}'.format(index))

    if self.cooldowns[index] != 0:
      return False

    a = self.abilities[index]
    self.cooldowns[index] = a.cooldown + 1
    return True

  def tick(self):
    for i in range(len(self.cooldowns)):
      if self.cooldowns[i] > 0:
        self.cooldowns[i] -= 1

  def __iter__(self):
    for i in self.abilities:
      yield i

  def __len__(self):
    return len(self.abilities)

  def __getitem__(self, key):
    return self.abilities[key]

class Ability(object):
  def __init__(self, name, kind, damage, duration, cooldown):
    self.name = name
    self.kind = kind
    self.damage = damage
    self.duration = duration
    self.cooldown = cooldown

class AbilityKind(Enum):
  Attack = 1
  Stun = 2
  Bleed = 3
  Heal = 4
  Burn = 5
  Lifelink = 6