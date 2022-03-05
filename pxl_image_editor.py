import pygame
from window import *

FONT_SIZE = 16

if __name__ == "__main__":
  window = Window(150, 150)
  window.layers.append(PixelLayer(window.width, window.height))
  font = pygame.font.Font("hackerman.ttf", FONT_SIZE)
  label_text = "*.pxl image editor - ctrl+S to save"
  label = font.render(
    label_text,
    True,
    (255, 255, 255, 255),
    (0, 0, 0, 0)
  )
  label_rect = label.get_rect()
  label_rect.center = (150, 10)

  def update(window, data, event_queue):
    # let the user draw
    if pygame.mouse.get_pressed()[0]:
      mouse_pos = pygame.mouse.get_pos()
      window.layers[1].set_pixel(
        mouse_pos[0]//PIXEL_SIZE,
        mouse_pos[1]//PIXEL_SIZE,
        (20, 20, 255, 100)
      )

    window.surface.blit(label, label_rect)

  window.mainloop(update, {})
