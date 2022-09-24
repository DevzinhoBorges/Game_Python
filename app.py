import pygame as pg

pg.init()
screen = pg.display.set_mode([840, 480])
pg.display.set_caption("Spacedown")

def draw():
  screen.fill((19,173,235))

gameloop = True
if __name__ == "__main__":
  while gameloop:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        gameloop = False

    draw()
    pg.display.update()