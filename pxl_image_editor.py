import pygame
from pygame.locals import *
import sys
from window import *

FONT_SIZE = 16

def main():
  output_filepath = sys.argv[1]
  window = Window(150, 150)
  window.layers.append(PixelLayer(window.width, window.height))
  title_text = "*.pxl image editor - press ctrl+S to save"
  pygame.display.set_caption(title_text)
  output_image = Image(output_filepath)

  def update(window, data, event_queue):
    window.layers[0].add_image(output_image)

    # let the user draw
    if pygame.mouse.get_pressed()[0]:
      mouse_x, mouse_y = pygame.mouse.get_pos()
      output_image.set_pixel(
        mouse_x//PIXEL_SIZE,
        mouse_y//PIXEL_SIZE,
        (20, 20, 255, 100)
      )

    keys = pygame.key.get_pressed()
    if keys[K_s] and (keys[K_RCTRL] or keys[K_LCTRL]):
      pygame.display.set_caption("Saving...")
      output_image.save(output_filepath)
      pygame.display.set_caption(title_text)

  window.mainloop(update, {})

main()
