import constants
import gamedata
import util


def winning(winner, game, grid, start):
    # détermine le gagnant (via les l)
    for line in grid:
        if "o" not in line and None not in line:
            winner = "x"
        elif "x" not in line and None not in line:
            winner = "o"

    # détermine le gagnant (via les colonnes)
    if winner is None:
        for c in range(len(grid[0])):
            if grid[0][c] is not None and grid[0][c] == grid[1][c] == grid[2][c]:
                winner = grid[0][c]
                break

    if winner is None:
        for p in ["x", "o"]:
            if grid[0][0] == grid[1][1] == grid[2][2] == p or grid[0][2] == grid[1][1] == grid[2][0] == p:
                winner = p
                break

    if winner is not None:
        game = False
        util.log(f"Game ended, winner is {winner}")
        gamedata.save(grid, winner, start)
    elif None not in grid[0] and None not in grid[1] and None not in grid[2]:
        game = False
        gamedata.save(grid, winner, start)

    return game, winner


def show_winner(screen, winner):
    if winner is not None:
        util.text(constants.LANG_WINNER, 502, 151, screen, 30, constants.BORDER_COLOR, constants.FONT_FILE)
        util.image(485, 200, constants.IMG_PLAYER_O_WIN if winner == "o" else constants.IMG_PLAYER_X_WIN, screen)
    else:
        util.text(constants.LANG_DRAW[0], 512, 221 - 15, screen, 30, constants.BORDER_COLOR, constants.FONT_FILE)
        util.text(constants.LANG_DRAW[1], 527, 252 - 15, screen, 30, constants.BORDER_COLOR, constants.FONT_FILE)
