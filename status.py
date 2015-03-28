from enum import Enum

class StatusList(object):
  def __init__(self):
    self.statuses = []
    self.durations = []

  def append(self, status):
    self.statuses.append(status)
    self.durations.append(status.duration+1)

  def search(self, kind):
    for status in self.statuses:
      if status.kind == kind:
        return True
    return False

  def tick(self):
    deleted = 0 
    for i in range(len(self.durations)):
      index = i - deleted
      self.durations[index] -= 1
      if self.durations[index] == 0:
        del self.durations[index]
        del self.statuses[index]
        deleted += 1

  def __iter__(self):
    for i in self.statuses:
      yield i

  def __len__(self):
    return len(self.statuses)

  def __getitem__(self, key):
    return self.statuses[key]

class Status(object):
  def __init__(self, name, kind, damage, duration):
    self.name = name
    self.kind = kind
    self.damage = damage
    self.duration = duration
