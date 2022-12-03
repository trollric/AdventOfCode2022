"""
Rock paper scissors.

Points = (Value of selected shape + win/loss/draw)

Shape | points
Stone   = 1
Paper   = 2
Scissor = 3

Win  = 6
Draw = 3
Loss = 0
"""


def point_calculator(player_shape : str, opponent_shape : str) -> int:
    """Takes a player rock, paper, scissor strategy from the player and their opponents
    perspective and returns the total amount of points granted.

    A: Rock
    B: Paper
    C: Scissors

    X: Rock
    Y: Paper
    Z: Scissors

    Args:
        player_shape (str): X, Y or Z
        opponent_shape (str): A, B or C

    Returns:
        int: The total amount of points
    """

    # Determine victor.
    victor = determine_victory(player_shape, opponent_shape)

    # Add points for victory.
    points = 0
    if victor == 'loss':
        points += 0
    elif victor == 'draw':
        points += 3
    elif victor == 'win':
        points += 6
    
    # Add the value of the player_shape.
    if player_shape.lower() == 'x':
        points += 1
    elif player_shape.lower() == 'y':
        points += 2
    elif player_shape.lower() == 'z':
        points += 3

    # Return points.
    return points


def determine_victory(player_shape : str, opponent_shape : str) -> str:
    """Returns victory status determined by the rules of Rock, Paper, Scissors.

    A: Rock
    B: Paper
    C: Scissors

    X: Rock
    Y: Paper
    Z: Scissors

    Args:
        player_shape (str): X, Y or Z
        opponent_shape (str): A, B or C

    Returns:
        str: loss, draw or win
    """
    victor = ''
    if opponent_shape.lower() == 'a':
        if player_shape.lower() == 'x':
            victor = 'draw'
        elif player_shape.lower() == 'y':
            victor = 'win'
        elif player_shape.lower() == 'z':
            victor = 'loss'
    if opponent_shape.lower() == 'b':
        if player_shape.lower() == 'x':
            victor = 'loss'
        elif player_shape.lower() == 'y':
            victor = 'draw'
        elif player_shape.lower() == 'z':
            victor = 'win'
    if opponent_shape.lower() == 'c':
        if player_shape.lower() == 'x':
            victor = 'win'
        elif player_shape.lower() == 'y':
            victor = 'loss'
        elif player_shape.lower() == 'z':
            victor = 'draw'

    return victor


if __name__ == '__main__':
    # Read lines

    # Clean the data

    # Loop through each game
        # Var +=  Send to a point calculator returning points.
    pass