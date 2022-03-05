import pygame

PIXEL_SIZE = 3

class Pixel:
  def __init__(self, x, y, color):
    self.x = x
    self.y = y
    self.color = color


class PixelLayer:
  def __init__(self, width, height):
    self.pixels = []
    for x in range(width):
      self.pixels.append([])
      for y in range(width):
        self.pixels[x].append(Pixel(x, y, (0, 0, 0, 0)))

  def set_pixel(self, x, y, color):
    self.pixels[x][y].color = color

  def render(self, screen):
    for col in self.pixels:
      for pixel in col:
        pygame.draw.rect(
          screen,
          pixel.color,
          (
            pixel.x * PIXEL_SIZE,
            pixel.y * PIXEL_SIZE,
            PIXEL_SIZE, PIXEL_SIZE
          )
        )


class Window:
  def __init__(
    self,
    width: int,
    height: int
  ):
    pygame.init()
    self.screen = pygame.display.set_mode(
      [width*PIXEL_SIZE, height*PIXEL_SIZE]
    )
    self.layers = [PixelLayer(width, height)]

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
      for layer in self.layers:
        layer.render(self.screen)
      pygame.display.flip()
    pygame.quit()
