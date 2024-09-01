import pygame

import game


class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.attak = 10

        self.player = player
        self.speed = 3
        self.image = pygame.image.load("image/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.player.rect.x + 120
        self.rect.y = self.player.rect.y + 75
        self.origine_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 6
        self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectile.remove(self)

    def move(self, all_monsters):
        if not self.player.animating:
            self.rect.x += self.speed
            self.rotate()
            if self.rect.x > 1080:
                self.remove()
            else:
                self.projectil_collistion(all_monsters)

    def projectil_collistion(self, all_monsters):
        # Vérifie la collision avec chaque monstre individuellement
        for monster in all_monsters:
            if pygame.sprite.collide_rect(self, monster):
                monster.health -= self.attak  # Réduit les points de vie du monstre
                if monster.health <= 0:
                    monster.monstre_mort()
                self.remove()
                break

