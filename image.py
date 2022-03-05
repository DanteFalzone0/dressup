import json

class Image:
  def __init__(self, filepath):
    self.data = json.loads(open(filepath).read())

  def
