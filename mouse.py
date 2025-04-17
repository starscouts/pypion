import constants
import game
import util

mouse_on_cell = None


# permet de placer les X et les O sur la grille, en fonction de la position de la souris
def click(x, y, grid, player, playing, winner):
    if 20 < x < 167 and 20 < y < 167:
        _place = game.place(0, 0, grid, player, playing)
        grid = _place[0]
        player = _place[1]
        util.log("Click: Place top left")
    elif 20 < x < 167 < y < 314:
        _place = game.place(1, 0, grid, player, playing)
        grid = _place[0]
        player = _place[1]
        util.log("Click: Place center left")
    elif 20 < x < 167 and 314 < y < 461:
        _place = game.place(2, 0, grid, player, playing)
        grid = _place[0]
        player = _place[1]
        util.log("Click: Place bottom left")
    elif 314 > x > 167 > y > 20:
        _place = game.place(0, 1, grid, player, playing)
        grid = _place[0]
        player = _place[1]
        util.log("Click: Place top center")
    elif 167 < x < 314 and 167 < y < 314:
        _place = game.place(1, 1, grid, player, playing)
        grid = _place[0]
        player = _place[1]
        util.log("Click: Place center center")
    elif 167 < x < 314 < y < 461:
        _place = game.place(2, 1, grid, player, playing)
        grid = _place[0]
        player = _place[1]
        util.log("Click: Place bottom center")
    elif 314 < x < 461 and 20 < y < 167:
        _place = game.place(0, 2, grid, player, playing)
        grid = _place[0]
        player = _place[1]
        util.log("Click: Place top right")
    elif 461 > x > 314 > y > 167:
        _place = game.place(1, 2, grid, player, playing)
        grid = _place[0]
        player = _place[1]
        util.log("Click: Place center right")
    elif 314 < x < 461 and 314 < y < 461:
        _place = game.place(2, 2, grid, player, playing)
        grid = _place[0]
        player = _place[1]
        util.log("Click: Place bottom right")
    elif 480 < x < 620 and 348 < y < 428:
        _restart = game.restart()
        grid = _restart[0]
        player = _restart[1]
        playing = _restart[2]
        winner = _restart[3]
        util.log("Click: Restart")
    else:
        util.log(f"Click: X = {x}, Y = {y}")

    return grid, player, playing, winner


# permet de jouer un son quand la souris est au-dessus d'une case
def hover(x, y, grid, player, playing, screen):
    global mouse_on_cell

    if playing and 20 < x < 167 and 20 < y < 167:
        if mouse_on_cell != "tl":
            util.sound(constants.SOUND_HOVER)
            mouse_on_cell = "tl"
    elif playing and 20 < x < 167 < y < 314:
        if mouse_on_cell != "cl":
            util.sound(constants.SOUND_HOVER)
            mouse_on_cell = "cl"
    elif playing and 20 < x < 167 and 314 < y < 461:
        if mouse_on_cell != "bl":
            util.sound(constants.SOUND_HOVER)
            mouse_on_cell = "bl"
    elif playing and 314 > x > 167 > y > 20:
        if mouse_on_cell != "tc":
            util.sound(constants.SOUND_HOVER)
            mouse_on_cell = "tc"
    elif playing and 167 < x < 314 and 167 < y < 314:
        if mouse_on_cell != "cc":
            util.sound(constants.SOUND_HOVER)
            mouse_on_cell = "cc"
    elif playing and 167 < x < 314 < y < 461:
        if mouse_on_cell != "bc":
            util.sound(constants.SOUND_HOVER)
            mouse_on_cell = "bc"
    elif playing and 314 < x < 461 and 20 < y < 167:
        if mouse_on_cell != "tr":
            util.sound(constants.SOUND_HOVER)
            mouse_on_cell = "tr"
    elif playing and 461 > x > 314 > y > 167:
        if mouse_on_cell != "cr":
            util.sound(constants.SOUND_HOVER)
            mouse_on_cell = "cr"
    elif playing and 314 < x < 461 and 314 < y < 461:
        if mouse_on_cell != "br":
            util.sound(constants.SOUND_HOVER)
            mouse_on_cell = "br"
    elif 480 < x < 620 and 348 < y < 428:
        if mouse_on_cell != "r":
            util.sound(constants.SOUND_HOVER)
            mouse_on_cell = "r"
    else:
        mouse_on_cell = None
