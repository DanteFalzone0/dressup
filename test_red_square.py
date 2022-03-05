import pygame
from window import *

if __name__ == "__main__":
  window = Window(100, 100)
  square = Image("red-square.pxl")
  window.layers[0].add_image(
    square,
    48,
    48,
    (255, 255, 255, 255)
  )

  def update(window, data, event_queue):
    pass

  window.mainloop(update, {})
