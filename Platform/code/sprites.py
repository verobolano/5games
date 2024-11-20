from settings import * 

class Sprite(pygame.sprite.Sprite):
    def _init_(self, pos, surf, groups):
        super()._init_(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)