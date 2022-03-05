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
    self.width = width
    self.height = height
    for x in range(self.width):
      self.pixels.append([])
      for y in range(self.height):
        self.pixels[x].append(Pixel(x, y, (0, 0, 0, 0)))

  def set_pixel(self, x, y, color):
    self.pixels[x][y].color = color

  # necessary to make the alpha channel work properly
  def _draw_rect_alpha(self, surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)

  def render(self, surface):
    for col in self.pixels:
      for pixel in col:
        self._draw_rect_alpha(
          surface,
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
    self.width = width
    self.height = height
    pygame.init()
    self.surface = pygame.display.set_mode(
      [width*PIXEL_SIZE, height*PIXEL_SIZE]
    )
    self.layers = [PixelLayer(width, height)]

  def mainloop(
    self,
    update, # must be a callable object taking a Window, a dict, and an iterable
    data: dict
  ):
    self.running = True
    while self.running:
      event_queue = pygame.event.get()
      for event in event_queue:
        if event.type == pygame.QUIT:
          self.running = False
      self.surface.fill((0, 0, 0))
      update(self, data, event_queue)
      for layer in self.layers:
        layer.render(self.surface)
      pygame.display.flip()
    pygame.quit()
