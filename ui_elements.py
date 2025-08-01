import pygame

class Button(pygame.Rect):
    def __init__(self, x, y, w, h, txt, callback:callable, font_size=16, font:pygame.font.Font=None, color=[255,255,255], list:list=None):
        super().__init__(x, y, w, h)
        self.clickable = True
        self.txt = txt
        self.callback = callback
        self.color = color
        if font == None:
            self.font = pygame.font.Font(None, font_size)
        else:
            self.font = font
        
        self.txt_surf = None
        
        self.redraw_txt_surf(self.txt)
        if list != None:
            list.append(self)
    
    def redraw_txt_surf(self, txt:str):
        self.txt = txt
        self.txt_surf = self.font.render(txt, True, self.color)
    
    def click(self, mouse_pos:list[int]):
        mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
        if mouse_rect.colliderect(self) == True:
            self.callback()
    
    def draw(self, surf):
        pygame.draw.rect(surf, self.color, self, 2)
        surf.blit(self.txt_surf, [self.centerx - (self.txt_surf.get_width() / 2), self.centery - (self.txt_surf.get_height() / 2)])