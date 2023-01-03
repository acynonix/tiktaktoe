def disp_board(i):            #defining disp board
    print('\n' * 100)

    print(i[7] + ' | ' + i[8] + ' | ' + i[9])
    print('---------')
    print(i[4] + ' | ' + i[5] + ' | ' + i[6])
    print('---------')
    print(i[1] + ' | ' + i[2] + ' | ' + i[3])

def play(i,marker,position):          #defining play function
    i[position]=marker


def player_input():          #funtion to take input from user
    marker = ''

    while marker != 'x' and marker != 'o':
        marker = input('Player 1 , Choose x or o')
    player1 = marker

    if player1 == 'x':
        player2 = 'o'
    else:
        player2 = 'x'

    return player1, player2


def win(i,mark):          #defining win
    if (i[7]==i[8]==i[9] == mark ) or (i[4]==i[5]==i[6]==mark ) or (i[1]==i[2]==i[3]==mark) or (i[7]==i[4]==i[1]==mark) or (i[2]==i[8]==i[5]==mark) or (i[9]==i[6]==i[3]==mark) or (i[7]==i[5]==i[3]==mark) or (i[1]==i[5]==i[9]==mark) :
        if player_1 == mark:
            print(' Player 1 has won')
        elif player_2 == mark:
            print('Player 2 has won')
    else:
        print('Not yet')



import random          #importing random module
def choose_first():
    s = random.randint(1, 2)

    if s == 1:
        print(s)
        return 'Player 1'
    else:
        print(s)
        return 'Player 2'


def space_check(i, position):   #for checking if there is any space left
    if i[position] == ' ':     #chech if the board list has empty string
        return True
    else:
        return False


def board_full(i):     #board full or not
    for a in range(1,10):
        if space_check(i,a):  #board is not full
            return False
        else:                 #board is full
            return True


def player_choice(i):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(i, position):
        position = int(input('Enter the position (1-9)'))
    return position



def replay():
    choice=input('Do you want to play again y or n')
    if choice == 'y':
        return True




def tiktaktoe():          #defining the main game
    while True:

        print('Welcome to Tik Tak Toe')

    #board empty string list (initial)
        i=[' ']*11

        player_1,player_2 = player_input()

    #randomly selecting player for starting the game
        turn = choose_first()
        print(turn + ' will go first')

        playgame=input('Ready to play  y or n ?')
        if playgame == 'y':
            game_on = True
        else:
            game_on = False


    #player is ready to play the game
        while game_on:
            if turn == 'Player 1':
                disp_board(i)  #display the board to player1

                position = player_choice(i)  #position

                play(i,player_1,position)  #placing the marker of player1 (which was saved in tuple) on the given position

                if win(i,player_1):  #checking if player1 has won
                    disp_board(i)
                    game_on = False
                else:                #checking for tie by checking the board full condition
                    if board_full(i):
                        disp_board(i)
                        print('Match Tie')
                        game_on = False
                    else:
                        turn = 'Player 2'

            else:
                disp_board(i)  #display the board to player2

                position = player_choice(i)  #position

                play(i,player_2,position)  #placing the marker of player2 (which was saved in tuple) on the given position

                if win(i,player_2):  #checking if player2 has won
                    disp_board(i)
                    game_on = False
                else:                #checking for tie by checking the board full condition
                    if board_full(i):
                        disp_board(i)
                        print('Match Tie')
                        game_on = False
                    else:
                        turn = 'Player 1'


        if not replay():
            break



tiktaktoe()
