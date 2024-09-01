import pygame
import random




class Monster(pygame.sprite.Sprite):
    def __init__(self, player, game, monster_type):
        super().__init__()
        self.player = player
        self.game = game
        self.monster_type = monster_type
        self.health = 40
        self.max_health = 40
        self.speed = 1
        self.attack = 5
        self.image = pygame.image.load("image/mumy.png")
        self.base_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(10,910)
        self.rect.y = 570
        self.last_damage_time = 0
        self.damage_cooldown = 1000
        self.dead_time = None

    def forward(self, player):
        if self.rect.x < player.rect.x:
            self.image = pygame.transform.flip(self.base_image, True, False)
            self.rect.x += self.speed
        elif self.rect.x > player.rect.x:
            self.image = self.base_image
            self.rect.x -= self.speed
        elif self.rect.x == player.rect.x:
            self.attack_player(player)

    def attack_player(self, player):
        current_time = pygame.time.get_ticks()
        if pygame.sprite.collide_rect(self, player):
            if current_time - self.last_damage_time >= self.damage_cooldown:
                print("Le joueur a pris des dégâts \tVie du joueur : ", player.vie)
                player.vie -= self.attack
                self.last_damage_time = current_time

    def monstre_vie_bar(self, surface):
        pygame.draw.rect(surface, (92, 78, 78), [self.rect.x + 100, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (87, 198, 43), [self.rect.x + 100, self.rect.y - 20, self.health, 5])

    def monstre_mort(self):
        from game import Game
        print("Monstre mort appelé")
        if self.health <= 0:
            if self.dead_time is None:
                print(f"{self.monster_type.capitalize()} est mort")
                self.dead_time = pygame.time.get_ticks()
                self.kill()


            if isinstance(self, Mummy):
                print("Mummy cooldown a fonctionné")
                new_monster = Mummy(self.player, self.game)
                self.game.all_monster.add(new_monster)
                print(f"Un nouveau Mummy a été ajouté : {new_monster}")
                self.game.add_points(10)
            elif isinstance(self, Allien):
                print("Allien cooldown a fonctionné")
                new_monster = Allien(self.player, self.game)
                self.game.all_monster.add(new_monster)
                print(f"Un nouveau Allien a été ajouté : {new_monster}")

                self.game.add_points(10)

                self.dead_time = None


class Mummy(Monster):
    def __init__(self, player, game):
        super().__init__(player, game, "mummy")
        self.image = pygame.image.load("image/mumy.png")
        self.base_image = self.image

    def __repr__(self):
        return f"Allien(id={id(self)}, health={self.health})"

class Allien(Monster):
    def __init__(self, player, game):
        super().__init__(player, game, "allien")
        self.image = pygame.image.load("image/alien1.png")
        self.image = pygame.transform.scale(self.image, (170, 170))

        self.base_image = self.image
        self.attack = 20
        self.health = 20
        self.max_health = 20
        self.speed = 2


    def __repr__(self):
        return f"Allien(id={id(self)}, health={self.health})"