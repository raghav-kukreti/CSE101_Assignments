#Assignment-2, Game Tic-tac-toe

#State: Tiles are numbered 1 to 9

"""
Tick-Tac-Toe game state is defined as follows: 

tile1 |  tile2  | tile3
______|_________|______
tile4 |  tile5  | tile6
______|_________|______
tile7 |  tile8  | tile9
______|_________|______

A player can belong to one of the following two categories:
1. Naive: Player checks a tile randomly.
2. Intelligent: Player follows some strategy to win a game. You shall define a strategy that an intelligent player can take.

We will estimate probability of winning for a player for different scenarios.
 
Game1: A number of games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.

Game2: A number of games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.

Game3: A number of games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.  
"""

import random 
from random import randint as randi
# There are 2 players: player1 and player2
player1=1
player2=2


# There are 9 tiles numbered tile1 to tile9
# 0 value of a tile indicates that tile has not been ticked
# 1 value indicates that the tile is ticked by player-1
# 2 value indicates that the tile is ticked by player-2

tile1= 0    
tile2= 0
tile3= 0
tile4= 0
tile5= 0
tile6= 0
tile7= 0
tile8= 0
tile9= 0

# turn variable defines whose turn is now
turn = player1

def reset():
	""" Resets the values of all tiles to zero."""
	global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9
	tile1=tile2=tile3=tile4=tile5=tile6=tile7=tile8=tile9=0

def validmove(move):
	""" Checks whether a move played by a player is valid or invalid.
		Return True if move is valid. 
		
		A move is valid if the corresponding tile for the move is not ticked.
	"""
	global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9
	if(move==1):
		if(tile1==0):
			return True
	elif(move==2):
		if(tile2==0):
			return True
	elif(move==3):
		if(tile3==0):
			return True
	elif(move==4):
		if(tile4==0):
			return True
	elif(move==5):
		if(tile5==0):
			return True
	elif(move==6):
		if(tile6==0):
			return True
	elif(move==7):
		if(tile7==0):
			return True
	elif(move==8):
		if(tile8==0):
			return True
	elif(move==9):
		if(tile9==0):
			return True
	return False
def win():
	""" Returns True if the board state specifies a winning state for some player.
		
		A player wins if ticks made by the player are present either
		i) in a row
		ii) in a cloumn
		iii) in a diagonal
	"""
	global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9
	if(tile1==tile2==tile3==1 or tile1==tile2==tile3==2):
		return True
	elif(tile4==tile5==tile6==1 or tile4==tile5==tile6==2):
		return True
	elif(tile7==tile8==tile9==1 or tile7==tile8==tile9==2):
		return True
	elif(tile4==tile5==tile6==1 or tile4==tile5==tile6==2):
		return True
	elif(tile1==tile4==tile7==1 or tile1==tile4==tile7==2):
		return True
	elif(tile2==tile5==tile8==1 or tile2==tile5==tile8==2):
		return True
	elif(tile3==tile6==tile9==1 or tile3==tile6==tile9==2):
		return True
	elif(tile1==tile5==tile9==1 or tile1==tile5==tile9==2):
		return True
	elif(tile3==tile5==tile7==1 or tile3==tile5==tile7==2):
		return True
	return False

def takeNaiveMove():
	""" Returns a tile number randomly from the set of unchecked tiles with uniform probability distribution.    
	"""
	mv=randi(1,9)
	while(validmove(mv)==False):
		mv=randi(1,9)
	return mv

def takeStrategicMove():
	""" Returns a tile number from the set of unchecked tiles
	using some rules.
	
	"""	
def validBoard():
	""" Return True if board state is valid.
		
		A board state is valid if number of ticks by player1 is always either equal to or one more than the ticks by player2.
	"""
	c1=0
	c2=0
	global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9
	if(tile1==1):
		c1=c1+1
	elif(tile1==2):
		c2=c2+1
	if(tile2==1):
		c1=c1+1
	elif(tile2==2):
		c2=c2+1
	if(tile3==1):
		c1=c1+1
	elif(tile3==2):
		c2=c2+1
	if(tile4==1):
		c1=c1+1
	elif(tile4==2):
		c2=c2+1
	if(tile5==1):
		c1=c1+1
	elif(tile5==2):
		c2=c2+1
	if(tile6==1):
		c1=c1+1
	elif(tile6==2):
		c2=c2+1
	if(tile7==1):
		c1=c1+1
	elif(tile7==2):
		c2=c2+1
	if(tile8==1):
		c1=c1+1
	elif(tile8==2):
		c2=c2+1
	if(tile9==1):
		c1=c1+1
	elif(tile9==2):
		c2=c2+1
	if(c1-c2 >= 0):
		return True
	else:
		return False

def game(gametype=1):
	""" Returns 1 if player1 wins and 2 if player2 wins
		and 0 if it is a draw.
	
		gametype defines three types of games discussed above.
		i.e., game1, game2, game3
	"""
	global turn
	j=0
	global w1
	if(gametype==1):
		for j in range(9):
				if(turn==player1):
					mv1=takeNaiveMove()
					validBoard()
					if(mv1==1):
						tile1=1
					elif(mv1==2):
						tile2=1
					elif(mv1==3):
						tile3=1	
					elif(mv1==4):
						tile4=1
					elif(mv1==5):
						tile5=1
					elif(mv1==6):
						tile6=1
					elif(mv1==7):
						tile7=1
					elif(mv1==8):
						tile8=1
					elif(mv1==9):
						tile9=1
				elif(turn==player2):
					mv2=takeNaiveMove()
					validBoard()
					if(mv2==1):
						tile1=2
					elif(mv2==2):
						tile2=2
					elif(mv2==3):
						tile3=2	
					elif(mv2==4):
						tile4=2
					elif(mv2==5):
						tile5=2
					elif(mv2==6):
						tile6=2
					elif(mv2==7):
						tile7=2
					elif(mv2==8):
						tile8=2
					elif(mv2==9):
						tile9=2
				if(turn==player1):
					turn=player2
				elif(turn==player2):
					turn=player1
		if(win()==True):
			if(turn==player1):
				w1=w1+1
			else:
				w2=w2+1	
		"""if(w1>w2):
			return (1)
		elif(w1<w2):
			return (2)
		elif(w1==w2):
			return (0)"""
def game1(n):
	""" Returns the winning probability for player1. 
	
	n games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	global tile1,tile2,tile3, tile4, tile5, tile6, tile7, tile8, tile9							
	index = takeNaiveMove()
	for i in range(n):
		for i in range(9):
			while not validmove(index):
				index = takeNaiveMove()
			if (i%2 == 0):
				if(index == 1):
					tile1 = 1
				elif(index == 2):	
					tile2 = 1
				elif(index == 3):
					tile3 = 1
				elif(index == 4):
					tile4 = 1
				elif(index == 5):
					tile5 = 1
				elif(index == 6):
					tile6 = 1
				elif(index == 7):
					tile7 = 1
				elif(index == 8):
					tile8 = 1
				elif(index == 9):
					tile9 = 1
			elif (i%2 == 1):
				if(index == 1):
					tile1 = 2
				elif(index == 2):
					tile2 = 2
				elif(index == 3):
					tile3 = 2
				elif(index == 4):
					tile4 = 2
				elif(index == 5):
					tile5 = 2
				elif(index == 6):
					tile6 = 2
				elif(index == 7):
					tile7 = 2
				elif(index == 8):
					tile8 = 2
				elif(index == 9):
					tile9 = 2
		print(tile1,tile2,tile3, tile4, tile5, tile6, tile7, tile8, tile9)
		print(win())
		tile1=tile2=tile3= tile4= tile5= tile6= tile7= tile8= tile9=0


def game2(n):
	"""Returns the winning probability for player1.
	
	n games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
	"""
	i=0
	while(n>i):
		reset()
	pass

def game3(n):
	"""Returns the winning probability for player1. 
	
	n games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	i=0
	while(n>i):
		reset()
	pass

game1(10)