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


def ensure_victor(player_desired_outcome : str, opponent_shape : str) -> str:
    """Takes a player desired outcome of Rock, Paper, Scissors and returns
    the player shape they need to use to aquire the desired outcome.

    A: Rock
    B: Paper
    C: Scissors

    X: Rock
    Y: Paper
    Z: Scissors

    Args:
        player_desired_outcome (str): win, draw, loss
        opponent_shape (str): A, B, C

    Returns:
        str: X, Y, Z
    """

    player_shape = ''
    opponent_shape = opponent_shape.lower()
    if player_desired_outcome == 'win':
        if opponent_shape == 'a':
            player_shape = 'Y'
        elif opponent_shape == 'b':
            player_shape = 'Z'
        elif opponent_shape == 'c':
            player_shape = 'X'

    if player_desired_outcome == 'draw':
        if opponent_shape == 'a':
            player_shape = 'X'
        elif opponent_shape == 'b':
            player_shape = 'Y'
        elif opponent_shape == 'c':
            player_shape = 'Z'

    if player_desired_outcome == 'lose':
        if opponent_shape == 'a':
            player_shape = 'Z'
        elif opponent_shape == 'b':
            player_shape = 'X'
        elif opponent_shape == 'c':
            player_shape = 'Y'

    return player_shape


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
    lines = []
    with open('Day2/strategy_guide.txt') as file:
        # Append and clean the data.
        [lines.append(line.strip()) for line in file.readlines()]
    
    # Loop through each game
    total_points = 0
    for round in lines:
        # Get player and opponents strategy.
        opponent, player = round.split(' ')
    
        # Decide if we wish to win, lose or score a draw.
        if player.lower() == 'x':
            player = 'lose'
        elif player.lower() == 'y':
            player = 'draw'
        elif player.lower() == 'z':
            player = 'win'
        
        # Decide what shape to use.
        player = ensure_victor(player, opponent)

        # Add points for the strategy.
        total_points += point_calculator(player, opponent)
    
    print(total_points)