import pygame, sys

class App:
    def __init__(self):
        pygame.init()
        
        display = pygame.display.set_mode([1280, 720])
        clock = pygame.time.Clock()
        framerate = 60
    
    def poll(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()    
    
    def update(self):
        pass
    
    def draw(self, surf:pygame.surface):
        surf.fill([0, 0, 0])
        
        pygame.display.update()
        self.clock.tick(self.framerate)
    

app = App()

while True:
    app.poll()
    app.update()
    app.draw(app.display)