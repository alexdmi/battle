from enum import Enum

class StatusList(object):
  def __init__(self):
    self.statuses = []
    self.durations = []

  def append(self, status):
    self.statuses.append(status)
    self.durations.append(status.duration)

  def search(self, kind):
    for status in self.statuses:
      if status.kind == kind:
        return True
    return False

  def tick():
    deleted = 0 
    for i in range(len(self.durations)):
      index = i - deleted
      self.durations[index] -= 1
      if self.durations[index] = 0:
        del self.durations[index]
        del self.statuses[index]
        deleted += 1

  def __iter__(self):
    for i in self.statuses:
      yield i

class Status(object):
  def __init__(self, kind, damage, duration):
    self.name = name
    self.kind = kind
    self.damage = damage
    self.duration = duration

class StatusKind(Enum):
  Stun = 1
  Bleed = 2