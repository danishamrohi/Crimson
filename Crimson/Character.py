import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, size, position_x, position_y, idle_sprites, attack_sprites, heal_sprites=[]):
        super().__init__()
        self.sprites = idle_sprites
        self.idle_sprites = idle_sprites
        self.attack_sprites = attack_sprites
        self.heal_sprites = heal_sprites
        self.attacking = False
        self.healing = False
        self.current_sprite = 0
        self.position_x = position_x
        self.position_y = position_y
        self.size = size
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [position_x, position_y]

    def attack(self):
        self.attacking = True
        self.sprites = self.attack_sprites
        self.current_sprite = 0

    def heal(self):
        self.healing = True
        self.sprites = self.heal_sprites
        self.current_sprite = 0

    def update(self):
        self.current_sprite += 1
        if int(self.current_sprite) >= len(self.sprites):
            self.current_sprite = 0
            if self.attacking == True:
                self.attacking = False
                self.sprites = self.idle_sprites
            if self.healing == True:
                self.healing = False
                self.sprites = self.idle_sprites
        self.image = self.sprites[int(self.current_sprite)]
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
