import pygame
import random


# creer une classe qui va gerer la notion de monstre sur notre jeu
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 2)

    def damage(self, amount):
        # infliger les degats
        self.health -= amount

        # verifier si son nouveau nombre de point de vie est <= 0
        if self.health <= 0:
            # Reapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(1, 2)

            # si la barre d'evenement est chargee a son maximum
            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)

                # appel a la methode pour essayer de declancher la pluie de cometes
                self.game.comet_event.attempt_fall()

    def update_health_bar(self, surface):
        # dessiner la bar de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        # le deplacement ne se fait que s'il n'y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else:
            # infliger des degats (au joueur)
            self.game.player.damage(self.attack)
