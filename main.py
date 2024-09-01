import pygame
from game import Game
from grafic import Grafic
from monster import Monster, Allien


def main():
    pygame.init()
    screen_width = 1080
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))

    try:
        fond = pygame.image.load("image/sky.png")
    except FileNotFoundError:
        print("L'image 'sky.png' est introuvable.")
        pygame.quit()
        exit()

    fond = pygame.transform.scale(fond, (1080, 720))

    game = Game()
    run = True

    while run:
        screen.blit(fond, (0, 0))

        game.player.player_animation()
        screen.blit(game.player.image, game.player.rect)
        screen.blit(game.player.player_life(), (910, 10))

        game.player.player_vie_bar(screen)

        screen.blit(game.update_points()[0], (10, 20))
        screen.blit(game.record_pts()[0],(10,60))

        game.all_monster.update()
        game.all_monster.draw(screen)


        for monster in game.all_monster:
            screen.blit(monster.image, monster.rect)
            monster.forward(game.player)
            monster.monstre_vie_bar(screen)

            if monster.health <= 0:
                monster.monstre_mort()
                game.monster_mort_pts(monster)

        for projectile in game.player.all_projectile:
            projectile.move(game.all_monster)
        game.player.all_projectile.draw(screen)

        if game.presed.get(pygame.K_a) or game.presed.get(pygame.K_LEFT):
            game.player.move_left()
            if game.player.rect.x < 0:
                game.player.rect.x = 1080
        elif game.presed.get(pygame.K_d) or game.presed.get(pygame.K_RIGHT):
            game.player.move_right()
            if game.player.rect.x > 910:
                game.player.rect.x = -350


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Le jeu a été fermé")
                run = False
            elif event.type == pygame.KEYDOWN:
                game.presed[event.key] = True
                if event.key == pygame.K_SPACE:
                    game.player.start_animation()
                    game.player.launch_projectil()

                if event.key == pygame.K_r:
                    print("r")
                    regeneration_text = game.player.regeneration(game)

            elif event.type == pygame.KEYUP:
                game.presed[event.key] = False

        if game.player.vie <= -5:
            run = False
            game.grafic.mort()

    pts_text, _ = game.update_points()
    screen.blit(pts_text, (10, 20))

    pygame.quit()

if __name__ == "__main__":
    grafic = Grafic()
    grafic.intro()
    grafic.menu()
