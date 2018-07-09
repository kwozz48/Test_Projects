

player1_input = input('Player 1, enter your choice (rock, paper, or scissors): ')

player2_input = input('Player 2, enter your choice (rock, paper, or scissors): ')

while player1_input != 'rock' and player1_input != 'paper' and player1_input != 'scissors':
    player1_input = input('Invalid input. Player 1, please reenter your choice (rock, paper, or scissors): ')

while player2_input != 'rock' and player2_input != 'paper' and player2_input != 'scissors':
    player2_input = input('Invalid input. Player 2, please reenter your choice (rock, paper, or scissors): ')

def compare (input1, input2):

    if input1 == input2:
        return ('Tie game!')
    elif input1 == 'rock' and input2 =='scissors':
        return ('Player 1 wins!')
    elif input1 == 'rock' and input2 == 'paper':
        return ('Player 2 wins')
    elif input1 == 'scissors' and input2 == 'rock':
        return ('Player 2 wins')
    elif input1 == 'scissors' and input2 == 'paper':
        return ('Player 1 wins')
    elif input1 == 'paper' and input2 == 'scissors':
        return ('Player 2 wins')
    elif input1 == 'paper' and input2 == 'rock':
        return ('Player 1 wins')

print (compare(player1_input, player2_input))