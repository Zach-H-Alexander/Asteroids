import pygame

from circleshape import CircleShape
from constants import PLAYER_SHOOT_SPEED
SHOT_RADIUS = 5
class Shot(CircleShape):
    def __init__(self, x, y, player_rotation, player_velocity):
        super().__init__(x, y, SHOT_RADIUS)
        shot_vector = pygame.Vector2(0,1)
        self.velocity = shot_vector.rotate(player_rotation) * PLAYER_SHOOT_SPEED
        self.velocity += player_velocity
        
    
    def draw(self, screen):
        position = (self.position.x, self.position.y)
        pygame.draw.circle(screen, (255,255,255), position, self.radius, 5)

    def update(self, dt):
        self.position += self.velocity * dt  