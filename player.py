
import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS
# Base class for game objects
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
   
     
    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotation = self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotation = self.rotate(dt)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt


