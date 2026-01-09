import pygame

from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, LINE_WIDTH, PLAYER_SHOT_RADIUS, PLAYER_SHOT_SPEED, PLAYER_SHOT_COOLDOWN_SECOND

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer_shot_cooldown = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        u_vect = pygame.Vector2(0, 1)
        rot_vect = u_vect.rotate(self.rotation)
        speed_vect = rot_vect * PLAYER_SPEED * dt
        self.position += speed_vect

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.timer_shot_cooldown < 0:
                self.shoot(dt)
                self.timer_shot_cooldown = PLAYER_SHOT_COOLDOWN_SECOND
        
        self.timer_shot_cooldown -= dt

    def shoot(self, dt):
        shot = Shot(self.position.x, self.position.y, PLAYER_SHOT_RADIUS)
        vect_ = pygame.Vector2(0, 1)
        shot.velocity = vect_.rotate(self.rotation) * PLAYER_SHOT_SPEED