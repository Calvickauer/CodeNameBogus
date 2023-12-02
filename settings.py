SCREEN_WIDTH = 1200
SCREEN_HEIGHT =  1200
TILE_W = 62
TILE_H = 93
SCROLL_T = SCREEN_WIDTH / 3
SHIFT_AMOUNT = 8

MAPS = {
    "map_one":[
        " P                                                        ",
        "                                                          ",
        "                                                          ",
        "                                                          ",
        "                                                          ",
        "                                                          ",
        "                                                          ",
        "                                                          ",
        "                                                          ",
        "                                                          ",
        "         E                                                ",
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    ],
    "maptwo": []
}

level_map = [
'                            ',
'                            ',
'                            ',
'                            ',
'    P                       ',
'                            ',
'                            ',
'                            ',
'      E                     ',
'          E    E            ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']

PRIMARY_WEAPONS = {
    'handgun': {'name': 'handgun', 'fire_rate': 0.4, 'damage': 2},
    'revolver': {'name': 'revolver', 'fire_rate': 0.7, 'damage': 3}
}
SECONDARY_WEAPONS = {
    'shotgun': {'name': 'shotgun','fire_rate': 0.9, 'damage': 6}
}
HEAVY_WEAPONS = {
    'machinegun': {'name':'machinegun','fire_rate': 0.1, 'damage': 4}
}