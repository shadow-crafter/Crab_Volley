import pygame

class Physics_Body:
    def __init__(self, game, position, size, img: pygame.Surface, term_vel=5):
        self.game = game
        self.position = list(position)
        self.size = size
        self.img = img

        self.velocity = [0, 0]
        self.term_vel = term_vel
    
    def get_rect(self) -> pygame.Rect: #for future collisions
        return pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
    
    def update(self, movement=(0, 0)):
        cur_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        self.position[0] += cur_movement[0]
        self.position[1] += min(cur_movement[1], self.term_vel)

    def render(self, surface: pygame.Surface):
        surface.blit(self.img, (self.position[0], self.position[1]))
