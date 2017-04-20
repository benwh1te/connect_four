#Connect 4

import os;
import random;

inf = 999
negInf = -999

human = 'x'
comp = 'o'
board = [' ' for x in range(42)];
inputVals = {'1': 1, '2': 2, '3':3, '4':4, '5':5, '6':6, '7':7}
#21 total
winningVerticalCombos = {0: [0, 7, 14, 21], 1: [7, 14, 21, 28], 2:[14, 21, 28, 35], 3: [1, 8, 15, 22],
				4: [8, 15, 22, 29], 5: [15, 22, 29, 36], 6: [2, 9, 16, 23], 7: [9, 16, 23, 30],
				8: [16, 23, 30, 37], 9: [3, 10, 17, 24], 10: [10, 17, 24, 31], 11: [17, 24, 31, 38],
				12: [4, 11, 18, 25], 13: [11, 18, 25, 32], 14: [18, 25, 32, 39], 15: [5, 12, 19, 26],
				16: [12, 19, 26, 33], 17: [19, 26, 33, 40], 18: [6, 13, 20, 27], 19: [13, 20, 27, 34],
				20: [ 20, 27, 34, 41]};

#24 total
winningHorizontalCombos = {0: [0, 1, 2, 3], 1: [1, 2, 3, 4], 2: [2, 3, 4, 5], 3: [3, 4, 5, 6],
							4: [7, 8, 9, 10], 5: [8, 9, 10, 11], 6: [9, 10, 11, 12], 7: [10, 11, 12, 13], 
							8: [14, 15, 16, 17], 9: [15, 16, 17, 18], 10: [16, 17, 18, 19], 11: [17, 18, 19, 20],
							12: [21, 22, 23, 24], 13: [22, 23, 24, 25], 14: [23, 24, 25, 26], 15: [24, 25, 26, 27], 
							16: [28, 29, 30, 31], 17: [29, 30, 31, 32], 18: [30, 31, 32, 33], 19: [31, 32, 33, 34],
							20: [35, 36, 37, 38], 21: [36, 37, 38, 39], 22: [37, 38, 39, 40], 23: [38, 39, 40, 41]};
#24 total
winningDiagonalCombos = {0: [0, 8, 16, 24], 1: [7, 15, 23, 31], 2: [14, 22, 30, 38],
							3: [1, 9, 17, 25], 4: [8, 16, 24, 32], 5: [15, 23, 31, 34], 
							6: [2, 10, 18, 26], 7: [9, 17, 25, 33], 8: [16, 24, 32, 40],
							9: [3, 11, 19, 27], 10: [10, 18, 26, 34], 11: [17, 25, 33, 41],
							12: [3, 9, 15, 21], 13: [10, 16, 22, 28], 14: [17, 23, 29, 35],
							15: [4, 10, 16, 22], 16: [11, 17, 23, 29], 17: [18, 24, 30, 36],
							18: [5, 11, 17, 23], 19: [12, 18, 24, 30],20: [19, 25, 31, 37],
							21: [6, 12, 18, 24], 22: [13, 19, 25, 31], 23: [20, 26, 32, 38]};

def movesLeft(board):
	for i in range(42):
		if board[i] is ' ':
			return True;
	return False;

def eval(board):
	for i in range(24):
		winningMoves = winningHorizontalCombos[i]
		if (board[winningMoves[0]] == board[winningMoves[1]] and board[winningMoves[1]] == board[winningMoves[2]]) and board[winningMoves[2]] == board[winningMoves[3]]:
			if board[winningMoves[0]] is comp:
				return 50
			if board[winningMoves[0]] is human:
				return -50
	for j in range(24):
		winningMoves = winningDiagonalCombos[j]
		if (board[winningMoves[0]] == board[winningMoves[1]] and board[winningMoves[1]] == board[winningMoves[2]]) and board[winningMoves[2]] == board[winningMoves[3]]:
			if board[winningMoves[0]] is comp:
				return 50
			if board[winningMoves[0]] is human:
				return -50
	for k in range(21):
		winningMoves = winningVerticalCombos[k]
		if (board[winningMoves[0]] == board[winningMoves[1]] and board[winningMoves[1]] == board[winningMoves[2]]) and board[winningMoves[2]] == board[winningMoves[3]]:
			if board[winningMoves[0]] is comp:
				return 50
			if board[winningMoves[0]] is human:
				return -50
	return 0;


def minimax(board, depth, isHuman, alpha, beta):
    score = eval(board);
    #print(depth)
    if score == 50:
        return score-depth
    elif score == -50:
        return score-depth
    elif movesLeft(board) is False:
        return 0-depth
    elif depth == 8:
    	return 0-depth

    possibleMoves = findPossibleMoves(board)

    if(isHuman):
        best = inf
        for i in possibleMoves:
            if board[i] is ' ':
                board[i] = human
                best = min(best, minimax(board, depth+1, False, alpha, beta))
                board[i] = ' '
                if best < beta:
                	beta = best
                if alpha >= beta:
                	break
    else:
        best = negInf
        for i in possibleMoves:
            if board[i] is ' ':
                board[i] = comp
                best = max(best, minimax(board, depth+1, True, alpha, beta))
                board[i] = ' '
                if best > alpha:
                	alpha = best
                if alpha >= beta:
                	break
    return best;

def findPossibleMoves(board):
    possibleMoves = [];
    for i in range(7):
        if board[i] is ' ':
            possibleMoves.append(i)
        elif board[7+i] is ' ':
            possibleMoves.append(7+i)
        elif board[14+i] is ' ':
            possibleMoves.append(14+i)
        elif board[21+i] is ' ':
            possibleMoves.append(21+i)
        elif board[28+i] is ' ':
            possibleMoves.append(28+i)
        elif board[35+i] is ' ':
            possibleMoves.append(35+i)
    return possibleMoves

def findBestMove(board):
    bestMove = -1  
    bestVal = -1000
    possibleMoves = findPossibleMoves(board)
    #print(possibleMoves)
    for i in possibleMoves:
        if board[i] is ' ': #should be but no reason not to have a sanity check
            board[i] = comp;
            tempVal = minimax(board, 1, True, negInf, inf)
            #print(i) 
            if tempVal > bestVal:
                bestMove = i
                bestVal = tempVal
            #print(bestVal)
            board[i] = ' '
    return bestMove

def printInstructions():
	print("Welcome to Connect 4!\n")
	print("The goal of the game is to get 4 in a row.\n")
	print("The person who goes first will be chosen at random.\n")
	print("Instructions for the game are as follows:")
	print("Choose the column you want to place your piece.")
	print("The columns are numbered 1-7.")

def printBoard(board):
	print(board[35:42])
	print(board[28:35])
	print(board[21:28])
	print(board[14:21])
	print(board[7:14])
	print(board[0:7])
	print('\n')

def main():
	printInstructions()
	printBoard(board)
	os.system('pause')
	first = random.random()
	compsTurn = True
	if first >= 0.5:
		print("The computer will make the first move.\n")
		compsTurn = True
	else:
		print("You will make the first move.\n")
		compsTurn = False
	print("Are you ready?")
	os.system("pause")

	while eval(board) is 0 and movesLeft(board) is True:
		if compsTurn is True:
			compsMove = findBestMove(board)
			board[compsMove] = comp
			compsTurn = False;
		else:
			charMove = input("What is your move? Value must be between 1-7.\n")
			move = inputVals[charMove];
			move = move-1
			possibleMoves = findPossibleMoves(board)
			for i in possibleMoves:
				if (i%7) == move:
					board[i] = human
					compsTurn = True
		printBoard(board)

	if eval(board) < 0:
		print("YOU WON!!")
	elif eval(board) > 0:
		print("You lost :(")
	else:
		print("The game ended in a tie")



main()


