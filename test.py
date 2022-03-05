import pygame
from window import Window

if __name__ == "__main__":
  window = Window(500, 500)

  def update(window, data):
    window.screen.fill((0, 0, 0))
    pygame.draw.circle(window.screen, (0, 255, 80), (250, 250), 75)
    pygame.display.flip()

  window.mainloop(update, {})
