from operator import truediv

import pygame
import time

import game
from projectile import Projectile


class PLayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.vie = 40
        self.max_vie = 40
        self.speed = 3
        self.base_image = pygame.image.load("image/batman.png")
        self.base_image = pygame.transform.scale(self.base_image, (200, 200))
        self.image = self.base_image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 550
        self.die_anim = self.rect.y

        self.animation_start_time = None
        self.animation_duration = 1.0
        self.animating = False

        self.all_projectile = pygame.sprite.Group()

    def player_life(self):
        blanc = (255, 255, 255)
        font = pygame.font.Font(None, 74)
        txt_player_life = font.render(f"Vie: {self.vie}", True, blanc)
        return txt_player_life

    def launch_projectil(self):
        if not self.animating:
            self.all_projectile.add(Projectile(self))
    def move_right(self):
        if not self.animating:
            self.rect.x += self.speed
    def move_left(self):
        if not self.animating:
            self.rect.x -= self.speed

    def start_animation(self):
        if not self.animating:
            self.animation_start_time = time.time()
            self.animating = True
            self.image = pygame.image.load("image/batman_anim.png")
            self.image = pygame.transform.scale(self.image, (200, 200))

    def player_animation(self):
        if self.animating:
            current_time = time.time()
            if current_time - self.animation_start_time >= self.animation_duration:
                self.image = self.base_image
                self.animating = False
                self.launch_projectil()

    def player_vie_bar(self, surface):
        pygame.draw.rect(surface, (208, 37, 37), [self.rect.x + 100, self.rect.y - 20, self.max_vie, 5])
        vie_actuelle_largeur = (self.vie / self.max_vie) * self.max_vie
        pygame.draw.rect(surface, (87, 198, 43), [self.rect.x + 100, self.rect.y - 20, vie_actuelle_largeur, 5])

    def regeneration(self, game):
        blanc = (255, 255, 255)
        font = pygame.font.Font(None, 25)
        if self.vie == self.max_vie:
            pass
        else:
            if game.point >= 10:
                game.point -= 10
                self.vie = self.max_vie
                print("Le joueur a été régénéré")
        return game.point
