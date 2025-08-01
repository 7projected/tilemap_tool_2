import pygame, sys, ui_elements, main_menu

class App:
    def __init__(self):
        pygame.init()
        
        self.display = pygame.display.set_mode([1280, 720])
        self.clock = pygame.time.Clock()
        self.framerate = 60
        
        
        self.main_menu = main_menu.MainMenu()
        
        self.button_list = self.main_menu.button_list
        
    
    def poll(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()    
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in self.button_list:
                        button.click(event.pos)
    
    def update(self):
        pass
    
    def draw(self, surf:pygame.surface):
        surf.fill([0, 0, 0])
        
        for button in self.button_list:
            button.draw(surf)
        
        pygame.display.update()
        self.clock.tick(self.framerate)
    

app = App()

while True:
    app.poll()
    app.update()
    app.draw(app.display)