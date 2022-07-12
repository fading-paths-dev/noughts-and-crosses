
from Grids import *

#enter odd number of elements less than or equal to 7
game_variables.elements = 5
game_variables.boardFull = 0
#enter player type (human or AI)
game_variables.player1 = 'H'
game_variables.player2 = 'H'
game_variables.currentPlayer = 1
#draw grid
drawGrid()
#define all grid elements
initElements()
#add centre for each grid element (make unused squares centre off the screen)
initCentres(getGridElements())
#set up next element to be cross
game_variables.nextShape = 'X'
#if next player is a human
if (game_variables.player1 == 'H'):
    #set up next input to be from mouse click
    tur.onscreenclick(move)
else:
    #set up next input to be from an AI
    print("AI is not currently supported")
    #getAIDecision(coordX, coordY)
    #move(coordX, coordY)

tur.mainloop()