while True:
    player1 = input('Player 1\nChoose one:\nRock - R\nPaper - P\nScissors - S\n')
    player2 = input('Player 2\nChoose one:\nRock - R\nPaper - P\nScissors - S\n')

    if(player1=='R' and player2=='P'):
        print('player2 wins!')
    elif(player1=='R' and player2=='S'):
        print('player1 wins!')
    elif(player1=='P' and player2=='R'):
        print('player1 wins!')
    elif (player1 == 'P' and player2 == 'S'):
        print('player2 wins!')
    elif (player1 == 'S' and player2 == 'R'):
        print('player2 wins!')
    elif (player1 == 'S' and player2 == 'P'):
        print('player1 wins!')
    elif(player1==player2):
        print('Draw!')
    else:
        print('Someone wrote wrong letter!')

    if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
        continue
    else:
        print('Game over!')
        break
