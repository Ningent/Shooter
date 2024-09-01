import pygame
from player import PLayer
from monster import Monster, Mummy, Allien
from grafic import Grafic


class Game:
    def __init__(self):
        self.player = PLayer()
        self.presed = {}
        self.all_monster = pygame.sprite.Group()
        self.spawn_monster()
        self.grafic = Grafic(self)
        self.rip = False
        self.last_time = pygame.time.get_ticks()
        self.point = 0
        self.recort_poit = 0

    def add_points(self, points):
        self.point += points
        print(f"Points: {self.point}")
    def spawn_monster(self):
        self.all_monster.add(Mummy(self.player, self))
        self.all_monster.add(Allien(self.player, self))

    def reinstall(self,player):
        self.player.vie = 40
        self.player.max_vie = 40
        self.player.rect.x = 0
        self.player.rect.y = 550
        self.player.all_projectile.empty()

        self.point = 0

        self.all_monster.empty()
        self.spawn_monster()

        print("Le jeu a été réinstallé")
        self.rip = False

    def update_points(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_time > 10000:
            self.point += 1
            self.last_time = current_time
        blanc = (255, 255, 255)
        font = pygame.font.Font(None, 50)
        pts = font.render(f"point: {self.point}", True, blanc)
        return pts, self.point

    def monster_mort_pts(self, monster):
        if isinstance(monster, Mummy):
            self.point += 10
        elif isinstance(monster, Allien):
            self.point += 15
        print(f"Points: {self.point}")


    def record_pts(self):
        with open("az.txt", "r") as az_r:
            lignes = az_r.readlines()
            if lignes:
                meilleur_score = max([int(ligne.strip()) for ligne in lignes])
            else:
                meilleur_score = 0

        if self.point > meilleur_score:
            with open("az.txt", "w") as az_w:
                az_w.write(str(self.point) + "\n")
            meilleur_score = self.point

        self.record_point = meilleur_score

        blanc = (255, 255, 255)
        font = pygame.font.Font(None, 50)
        pts = font.render(f"Record point: {meilleur_score}", True, blanc)
        return pts, self.point

