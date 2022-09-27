import pygame as pg

class Player(pg.sprite.Sprite):
  def __init__(self, *groups):
    super().__init__(*groups)

    self.image = pg.image.load("GameTutorial/img/nave.png") # Adiciona a imagem do sprite
    self.image = pg.transform.scale(self.image, [100, 100]) # Modifica o tamanho da imagem
    self.rect = pg.Rect(50, 50, 100, 100) # Defini o tamanho e a posição da imagem

  def update(self, *args):
    keys = pg.key.get_pressed()

    if keys[pg.K_a]:
      self.rect.x -= 1
    elif keys[pg.K_d]:
      self.rect.x += 1
    elif keys[pg.K_s]:
      self.rect.y += 1
    elif keys[pg.K_w]:
      self.rect.y -= 1