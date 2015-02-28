from enum import Enum

class AbilityList(object):
  """
  A list of abilities for an entity.
  """

  def __init__(self):
    self.abilities = []
    self.cooldowns = []

  def __getitem__(self, key):
    return self.abilities[key]

  def append(self, ability):
    self.abilities.append(ability)
    self.cooldowns.append(0)

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
    self.cooldowns[index] = a.cooldown
    return True

  def __iter__(self):
    for i in self.abilities:
      yield i

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