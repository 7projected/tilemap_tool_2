import ui_elements

class MainMenu:
    def __init__(self):
        self.button_list = []
        
        ui_elements.Button(10, 10, 300, 70, "Load Map", self.load_map, list=self.button_list)
        ui_elements.Button(10, 80, 300, 70, "Create Map", self.create_map, list=self.button_list)
        ui_elements.Button(10, 150, 300, 70, "Create Tileset", self.create_tileset, list=self.button_list)
    
    def load_map(self):
        pass

    def create_map(self):
        pass

    def create_tileset(self):
        pass