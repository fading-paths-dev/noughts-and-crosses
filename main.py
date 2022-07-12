from Grids import *

# enter odd number of elements less than or equal to 7
GameVariables.elements = 5
GameVariables.boardFull = 0
# enter player type (human or AI)
GameVariables.player1 = 'H'
GameVariables.player2 = 'H'
GameVariables.currentPlayer = 1
# draw grid
draw_grid()
# define all grid elements
init_elements()
# add centre for each grid element (make unused squares centre off the screen)
init_centres(get_grid_elements())
# set up next element to be cross
GameVariables.nextShape = 'X'
# if next player is a human
if GameVariables.player1 == 'H':
    # set up next input to be from mouse click
    tur.onscreenclick(move)
else:
    # set up next input to be from an AI
    print("AI is not currently supported")
    # getAIDecision(coordX, coordY)
    # move(coordX, coordY)

tur.mainloop()
