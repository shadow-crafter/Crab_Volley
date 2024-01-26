import pygame, sys
from src.bodies import Physics_Body
from src.util import load_image

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Crab Volley")
        self.window = pygame.display.set_mode((640, 320))
        self.display = pygame.Surface((320, 160))

        self.clock = pygame.time.Clock()
        
        self.assets = {
            'player': load_image("Player.png"),
        }

        self.player = Physics_Body(self, (160 - 16, 120), (16, 16), self.assets['player'])
        self.movement_dir = [False, False]
        self.move_speed = 2
    
    def run(self):
        while True:
            self.display.fill((0, 100, 200))
            
            self.player.update(((self.movement_dir[1] - self.movement_dir[0]) * self.move_speed, 0))
            self.player.render(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement_dir[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement_dir[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement_dir[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement_dir[1] = False
            
            self.window.blit(pygame.transform.scale(self.display, self.window.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()
