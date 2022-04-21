import pygame
import random

# creer une classe pour gerer cette comete
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # definir l'image associee a cette cmette
        self.image = pygame.image.load("assets/comet.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 2)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event
        self.attack = 5

    def remove(self):
        self.comet_event.all_comets.remove(self)

        # verifier si le nombre de cometes est de zero
        if len(self.comet_event.all_comets) == 0:
            # remettre la barre a zero
            self.comet_event.reset_percent()
            # apparaitre les 2 premiers monstres
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()

    def fall(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y >= 500:
            # retirer la boule de feu
            self.remove()

            # si il n'y a plus de boule de feu
            if len(self.comet_event.all_comets) == 0:
                # remettre la jaune au depart
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        # verifier i la boule de feu touche le joueur
        if self.comet_event.game.check_collision(
            self,
            self.comet_event.game.all_players
        ):
            # retirer la boule de feu
            self.remove()
            # subir les points de degats
            self.comet_event.game.player.damage(self.attack)