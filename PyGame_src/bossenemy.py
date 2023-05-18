# Imports 
import pygame

import game
from enemy import Enemy

# Static variables 
POISON_TIMER = 150

### SUBCLASS INHERITING FROM THE ENEMY CLASS TO IMPLEMENT THE BOSS ENEMY ###
class BossEnemy(Enemy):
    def __init__(self, hp, image, x, y, nodes):
        super().__init__(hp, image, x, y, nodes)    # Sets self.frozen to True to allow the game engine to freeze enemies
        self.speed = 1

    # Boss enemies immune to freeze effects
    def freeze(self):
        pass
    
    def unfreeze(self):
        pass
        
    def is_frozen(self):
        pass
    
    # Sets self.poisoned to True to allow the game engine to poison enemies
    def poison(self):
        self.poisoned = True
    
    # Sets self.poisoned to False ONLY IF the poison timer has timed out
    def unpoison(self):
        if self.is_poisoned() and self.poison_counter <= POISON_TIMER:
            if self.poison_counter in [50, 100, 150]:
                self.take_damage(1)
            self.poison_counter += 1
        else:
            self.poison_counter = 0
            self.poisoned = False
    
    # Returns the self.poison variable (boolean)
    def is_poisoned(self):
        return self.poisoned 
    
    # Draws the enemy and it's current HP
    def draw(self, surface):
        if self.is_poisoned():
            hp_txt = "hp: {hp}/{max_health}".format(hp=self.hp, max_health=self.max_health)
            text = game.FONT_3.render(hp_txt, True, game.POISON_COL)
            text_rect = text.get_rect(center=(self.x, self.y - 50))
            surface.blit(text, text_rect)
        else:
            hp_txt = "hp: {hp}/{max_health}".format(hp=self.hp, max_health=self.max_health)
            text = game.FONT_3.render(hp_txt, True, game.TEXT_COL)
            text_rect = text.get_rect(center=(self.x, self.y - 50))
            surface.blit(text, text_rect)
            
        if self.is_frozen():
            img = pygame.image.load('assets/frozen_basic_enemy.png').convert_alpha()
            img = pygame.transform.scale(img, (100, 100))
            surface.blit(img, (self.rect.x, self.rect.y))
        else:

            surface.blit(self.image, (self.rect.x, self.rect.y))