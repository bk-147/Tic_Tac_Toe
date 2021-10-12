# project -->2 tic tac toe in python 

#done by Bhaarath K



def play1():
	print("\t PLAYER 1 (X) :")
	grid_number_x = int(input('\tEnter Grid number [ number between 0 to 9] : '))

	if grid_number_x <= 3 :
		game[0][grid_number_x-1]='X'
	elif grid_number_x <= 6:
		game[1][grid_number_x-4] = 'X'
	else:
		game[2][grid_number_x-7] = 'X'

def play2():
	print("\t PLAYER 2 (O):")
	grid_number_o = int(input('\tEnter Grid number [ number between 0 to 9] : '))

	if grid_number_o <= 3 :
		game[0][grid_number_o-1]='O'
	elif grid_number_o <= 6:
		game[1][grid_number_o-4] = 'O'
	else:
		game[2][grid_number_o-7] = 'O'

def show():
	print('\n\n',)
	for i in game:
		for j in range(0,2):
			print(" ",end="")
			print(i[j],end='|')
		print(i[2])
		print(end='')
	print('\n\n')

def check_winner():
	if game[0][0] == 'X' and game[0][1] == 'X' and game[0][2] == 'X':
		Game_status = 'end'
		return 'X'
	elif game[1][0] == 'X' and game[1][1] == 'X' and game[1][2] == 'X':
		return 'X'
	elif game[2][0] == 'X' and game[2][1] == 'X' and game[2][2] == 'X':
		return 'X'
	elif game[0][0] == 'X' and game[1][1] == 'X' and game[2][2] == 'X':
		return 'X'
	elif game[2][0] == 'X' and game[1][1] == 'X' and game[0][2] == 'X':
		return 'X'
	elif game[0][0] == 'O' and game[0][1] == 'O' and game[0][2] == 'O':
		return 'O'
	elif game[1][0] == 'O' and game[1][1] == 'O' and game[1][2] == 'O':
		return 'O'
	elif game[2][0] == 'O' and game[2][1] == 'O' and game[2][2] == 'O':
		return 'O'
	elif game[0][0] == 'O' and game[1][1] == 'O' and game[2][2] == 'O':
		return 'O'
	elif game[2][0] == 'O' and game[1][1] == 'O' and game[0][2] == 'O':
		return 'O'
	else:
		pass



while True:
	game = [[" "," "," "],[" "," "," "],[" "," "," "]]
	Game_status = ''
	while True:
		show()
		play1()
		if check_winner() == 'X' :
			print('\n\n\t Player 1 (X) is the Winner')
			break
		elif check_winner() == 'O' :
			print('\n\n\t Player 2 (O) is the Winner')
			break
		show()
		play2()
		if check_winner() == 'X' :
			print('\n\n\t Player 1 (X) is the Winner')
			break
		if check_winner() == 'O' :
			print('\n\n\t Player 2 (O) is the Winner')
			break
	break


