import turtle as tur


class GridElement:

    def __init__(self, shape, centre_x, centre_y):
        self.shape = shape
        self.centreX = centre_x
        self.centreY = centre_y


squares = [[-3, -2, -1, 0, 1, 2, 3],
           [-3, -2, -1, 0, 1, 2, 3],
           [-3, -2, -1, 0, 1, 2, 3],
           [-3, -2, -1, 0, 1, 2, 3],
           [-3, -2, -1, 0, 1, 2, 3],
           [-3, -2, -1, 0, 1, 2, 3],
           [-3, -2, -1, 0, 1, 2, 3]]


class game_variables:

    def __init__(self, elements, current_player, player1, player2, next_shape, board_full):
        self.elements = elements
        self.currentPlayer = current_player
        self.player1 = player1
        self.player2 = player2
        self.nextShape = next_shape
        self.boardFull = board_full


def getGridElements():
    return game_variables.elements


# make the number of grid elements a public variable with get/set to be used throughout

def drawGrid():
    elements = getGridElements()
    # insure elements is odd
    elements |= 1;
    # calc spacing between lines
    segment = 600 / elements
    tur.penup()
    tur.goto(segment - 300, 300)
    tur.pendown()
    tur.width(2)
    # draw vertical inner lines
    for var in range(int((elements - 1) / 2)):
        tur.setheading(270)
        tur.fd(600)
        tur.penup()
        tur.setheading(0)
        tur.fd(segment)
        tur.pendown()
        tur.setheading(90)
        tur.fd(600)
        tur.penup()
        tur.setheading(0)
        tur.fd(segment)
        tur.pendown()
    tur.penup()
    tur.setheading(270)
    tur.fd(segment)
    tur.pendown()
    # draw horizontal inner lines
    for var in range(int((elements - 1) / 2)):
        tur.setheading(180)
        tur.fd(600)
        tur.penup()
        tur.setheading(270)
        tur.fd(segment)
        tur.pendown()
        tur.setheading(0)
        tur.fd(600)
        tur.penup()
        tur.setheading(270)
        tur.fd(segment)
        tur.pendown()
    # draw outer boundary
    for var in range(4):
        tur.right(90)
        tur.fd(600)


def drawNought(x, y):
    tur.onscreenclick(wait)
    elements = getGridElements()
    # scale size of symbol to fit grid
    radius = 600 / elements
    radius *= 0.33
    tur.penup()
    tur.goto(x, y)
    tur.setheading(270)
    tur.fd(radius)
    tur.setheading(0)
    tur.pendown()
    tur.circle(radius, 360)
    tur.onscreenclick(move)


def drawCross(x, y):
    tur.onscreenclick(wait)
    elements = getGridElements()
    # scale size of symbol to fit grid
    radius = 600 / elements
    radius *= 0.33
    for var in range(4):
        tur.penup()
        tur.goto(x, y)
        tur.setheading(45 + (var * 90))
        tur.pendown()
        tur.fd(radius)
    tur.onscreenclick(move)


def initElements():
    for var in range(7):
        squares[-3][var] = GridElement(' ', 500, 500)
        squares[-2][var] = GridElement(' ', 500, 500)
        squares[-1][var] = GridElement(' ', 500, 500)
        squares[0][var] = GridElement(' ', 500, 500)
        squares[1][var] = GridElement(' ', 500, 500)
        squares[2][var] = GridElement(' ', 500, 500)
        squares[3][var] = GridElement(' ', 500, 500)


def initCentres(elements):
    radius = 600 / elements
    offset = int((elements - 1) / 2)
    for var in range(elements):
        squares[-3][var - offset].centreX = radius * -3
        squares[-2][var - offset].centreX = radius * -2
        squares[-1][var - offset].centreX = radius * -1
        squares[0][var - offset].centreX = radius * 0
        squares[1][var - offset].centreX = radius * 1
        squares[2][var - offset].centreX = radius * 2
        squares[3][var - offset].centreX = radius * 3
    for var in range(elements):
        squares[var - offset][-3].centreY = radius * -3
        squares[var - offset][-2].centreY = radius * -2
        squares[var - offset][-1].centreY = radius * -1
        squares[var - offset][0].centreY = radius * 0
        squares[var - offset][1].centreY = radius * 1
        squares[var - offset][2].centreY = radius * 2
        squares[var - offset][3].centreY = radius * 3


def getGridPositionX(x):
    elements = getGridElements();
    radius = 600 / elements
    offset = int((elements - 1) / 2)
    if (x < -300):
        return 100  # error
    else:
        for var in range(elements):
            if (x < (radius * (var - offset + 0.5))):
                return var - offset
        return 200  # error


def getGrisPositionY(y):
    elements = getGridElements();
    radius = 600 / elements
    offset = int((elements - 1) / 2)
    if (y < -300.0):
        return 100  # error
    else:
        for var in range(elements):
            if (y < (radius * (var - offset + 0.5))):
                return var - offset
        return 200


def checkWinThree(lastShape):
    if ((squares[-1][-1].shape == lastShape and squares[-1][0].shape == lastShape and squares[-1][
        1].shape == lastShape) or
            (squares[0][-1].shape == lastShape and squares[0][0].shape == lastShape and squares[0][
                1].shape == lastShape) or
            (squares[1][-1].shape == lastShape and squares[1][0].shape == lastShape and squares[1][
                1].shape == lastShape) or
            (squares[-1][-1].shape == lastShape and squares[0][-1].shape == lastShape and squares[1][
                -1].shape == lastShape) or
            (squares[-1][0].shape == lastShape and squares[0][0].shape == lastShape and squares[1][
                0].shape == lastShape) or
            (squares[-1][1].shape == lastShape and squares[0][1].shape == lastShape and squares[1][
                1].shape == lastShape) or
            (squares[-1][-1].shape == lastShape and squares[0][0].shape == lastShape and squares[1][
                1].shape == lastShape) or
            (squares[1][-1].shape == lastShape and squares[0][0].shape == lastShape and squares[-1][
                1].shape == lastShape)):
        return 0
    else:
        return 2


# 0 = win, 1 = draw, 2 = else
def checkWinComplicated(elements, lastShape):
    offset = int((elements - 1) / 2)
    count = 0
    # colums
    for var in range(elements):
        for ret in range(elements):
            if (squares[var - offset][ret - offset].shape == lastShape):
                count += 1
            else:
                count = 0
            if (count == elements):
                return 0
    count = 0
    # rows
    for var in range(elements):
        for ret in range(elements):
            if (squares[ret - offset][var - offset].shape == lastShape):
                count += 1
            else:
                count = 0
            if (count == elements):
                return 0
    count = 0
    # diagonals
    for var in range(elements):
        if (squares[var - offset][var - offset].shape == lastShape):
            count += 1
        else:
            count = 0
        if (count == elements):
            return 0
    for var in range(elements):
        if (squares[offset - var][var - offset].shape == lastShape):
            count += 1
        else:
            count = 0
        if (count == elements):
            return 0
    return 2


# 0 = win, 1 = draw, 2 = else
# last shape is the opposite to the one passed in
def checkWin(elements, lastShape):
    print("checkWin", elements, lastShape)
    boundary = elements * elements
    if (game_variables.boardFull < boundary):
        if (lastShape == 'X'):
            return checkWinComplicated(elements, 'O')
        else:
            return checkWinComplicated(elements, 'X')
    else:
        return 1


def wait(x, y):
    print("It's not your turn yet")


def move(x, y):
    X = getGridPositionX(x)
    Y = getGrisPositionY(y)
    print(x, y)
    print(X, Y);
    if (X == 100 or Y == 100 or X == 200 or Y == 200):
        print("Select another spot")
    elif (squares[X][Y].shape == 'O'):
        if (game_variables.nextShape == 'O'):
            print("You've already gone there")
        else:
            print("No Cheating!")
    elif (squares[X][Y].shape == 'X'):
        if (game_variables.nextShape == 'X'):
            print("You've already gone there")
        else:
            print("No Cheating!")
    else:
        game_variables.boardFull = game_variables.boardFull + 1
        if (game_variables.nextShape == 'X'):
            drawCross(squares[X][Y].centreX, squares[X][Y].centreY)
            squares[X][Y].shape = 'X'
            game_variables.nextShape = 'O'
        else:
            drawNought(squares[X][Y].centreX, squares[X][Y].centreY)
            game_variables.nextShape = 'X'
            squares[X][Y].shape = 'O'

        # set up next player only if the selection was valid
        if (game_variables.currentPlayer == 1):
            game_variables.currentPlayer = 0
            nextplayer = game_variables.player1
        else:
            game_variables.currentPlayer = 1
            nextplayer = game_variables.player2

        # is it human or AI
        if (nextplayer == 'H'):
            # set up next input to be from mouse click
            tur.onscreenclick(move)
        else:
            # set up next input to be from an AI in such a way that it doesn't call move recursively
            print("AI is not currently supported")
            # getAIDecision(coordX, coordY)
            # move(coordX, coordY)
            # disable clicking making move be called
            tur.onscreenclick(wait)

        # check for win condition if the selection was valid
        result = checkWin(game_variables.elements, game_variables.nextShape)
        print("result = ", result)
        if (result == 0):
            if (game_variables.currentPlayer == 1):
                print("Player 2 Wins!")
                tur.onscreenclick(wait)
            else:
                print("Player 1 Wins!")
                tur.onscreenclick(wait)
        # else if board full
        elif (result == 1):
            print("Its a draw")
            tur.onscreenclick(wait)
