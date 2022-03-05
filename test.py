import pygame
from window import *

if __name__ == "__main__":
  window = Window(150, 150)
  window.layers.append(PixelLayer(window.width, window.height))

  def update(window, data, event_queue):
    # midpoint circle algorithm
    # copied from here https://rosettacode.org/wiki/Bitmap/Midpoint_circle_algorithm#Python
    radius = 50
    x0 = 75
    y0 = 75
    color = (0, 255, 80, 255)
    f = 1 - radius
    ddf_x = 1
    ddf_y = -2 * radius
    x = 0
    y = radius
    window.layers[0].set_pixel(x0, y0 + radius, color)
    window.layers[0].set_pixel(x0, y0 - radius, color)
    window.layers[0].set_pixel(x0 + radius, y0, color)
    window.layers[0].set_pixel(x0 - radius, y0, color)

    while x < y:
      if f >= 0:
        y -= 1
        ddf_y += 2
        f += ddf_y
      x += 1
      ddf_x += 2
      f += ddf_x
      window.layers[0].set_pixel(x0 + x, y0 + y, color)
      window.layers[0].set_pixel(x0 - x, y0 + y, color)
      window.layers[0].set_pixel(x0 + x, y0 - y, color)
      window.layers[0].set_pixel(x0 - x, y0 - y, color)
      window.layers[0].set_pixel(x0 + y, y0 + x, color)
      window.layers[0].set_pixel(x0 - y, y0 + x, color)
      window.layers[0].set_pixel(x0 + y, y0 - x, color)
      window.layers[0].set_pixel(x0 - y, y0 - x, color)

    # let the user draw
    if pygame.mouse.get_pressed()[0]:
      mouse_pos = pygame.mouse.get_pos()
      window.layers[1].set_pixel(
        mouse_pos[0]//PIXEL_SIZE,
        mouse_pos[1]//PIXEL_SIZE,
        (20, 20, 255, 100)
      )

  window.mainloop(update, {})
