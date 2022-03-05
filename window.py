import pygame


class Window:
  def __init__(
    self,
    width: int,
    height: int
  ):
    pygame.init()
    self.screen = pygame.display.set_mode([width, height])

  def mainloop(
    self,
    update, # must be a callable object taking a Window and a dict
    data: dict
  ):
    self.running = True
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
      update(self, data)
    pygame.quit()
