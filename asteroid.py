import pygame, random

from logger import log_event

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        split_angle = random.uniform(20, 50)
        vect_new_ast_1 = self.velocity.rotate(split_angle)
        vect_new_ast_2 = self.velocity.rotate(-split_angle)
        radius_new_ast = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroids(self.position.x, self.position.y, radius_new_ast)
        asteroid_1.velocity = vect_new_ast_1 * 1.2
        asteroid_2 = Asteroids(self.position.x, self.position.y, radius_new_ast)
        asteroid_2.velocity = vect_new_ast_2 * 1.2