# tilemap_tool_2
Python 3.11.2     Pygame 2.4.0

UI:
    Main Menu: Load map, Create map, Create tileset
    Load map: Dropdown of tileset configs, Dropdown of available .map files
    Create map: Dropdown of tileset configs, info fields for needed things to create a .map file (hex characters, map dimensions, etc.)
    Create tileset: TILESIZE field, tile .img path field with a + button to add more, - button on eat path that deletes the path
    Map editor: Save button, Save as button, dimension editor, tileset viewer, map editor

Map file:
    .map file extension
    holds map info in hexidecimal format
    settings that decides how many hex characters there are (eg 1 = A, 2 = A1, 3 = A11,     default = 2 places (255 in base 10))
    holds map dimensions

Tileset config file:
    .tcfg file extension
    Holds a independent const variable TILESIZE (vec2)
    Holds file addresses for multiple png files for each tile