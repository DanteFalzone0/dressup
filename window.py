import pygame
import json

PIXEL_SIZE = 4

class Pixel:
  def __init__(self, x, y, color):
    self.x = x
    self.y = y
    self.color = color


class Image:
  def __init__(self, filepath: str = None):
    if filepath is not None:
      self.data = json.loads(open(filepath).read())
    else:
      self.data = {"pixels": []}

  def __getitem__(self, key):
    return self.data[key]

  def __setitem__(self, key, value):
    self.data[key] = value

  def save(self, filepath: str):
    of = open(filepath, "w+")
    of.write(json.dumps(self.data, indent=2))
    of.close()

  def set_pixel(self, x, y, color):
    for obj in self.data["pixels"]:
      if (obj["x"], obj["y"]) == (x, y):
        del obj

    self.data["pixels"].append({
      "x": x,
      "y": y,
      "color": {
        "r": color[0],
        "g": color[1],
        "b": color[2],
        "alpha": color[3]
      }
    })


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

  def add_image(
    self,
    image: Image,
    xpos: int = 0,
    ypos: int = 0,
    bg = (0, 0, 0, 0) # tuple representing background color
  ):
    for obj in image["pixels"]:
      obj_color = obj["color"]
      color = (
        bg[0] if obj_color["r"] == "BG" else obj_color["r"],
        bg[1] if obj_color["g"] == "BG" else obj_color["g"],
        bg[2] if obj_color["b"] == "BG" else obj_color["b"],
        bg[3] if obj_color["alpha"] == "BG" else obj_color["alpha"]
      )
      try:
        self.set_pixel(obj["x"]+xpos, obj["y"]+ypos, color)
      except IndexError:
        pass


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
      self.surface.fill((0, 0, 0))
      event_queue = pygame.event.get()
      for event in event_queue:
        if event.type == pygame.QUIT:
          self.running = False
      update(self, data, event_queue)
      for layer in self.layers:
        layer.render(self.surface)
      pygame.display.update()
    pygame.quit()
