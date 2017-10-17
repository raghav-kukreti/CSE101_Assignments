# IP Homework No 2
# Name    : Raghav Dev Kukreti
# Roll no : 2017082

import random 
player1=1
player2=2
tile1= 0	   
tile2= 0
tile3= 0
tile4= 0
tile5= 0
tile6= 0
tile7= 0
tile8= 0
tile9= 0
turn = player1

def validmove(move):
	if (move == 1):
		if (tile1 == 0):
			return True
	elif (move == 2):
		if (tile2 == 0):
			return True
	elif (move == 3):
		if (tile3 == 0):
			return True
	elif (move == 4):
		if (tile4 == 0):
			return True
	elif (move == 5):
		if (tile5 == 0):
			return True
	elif (move == 6):
		if (tile6 == 0):
			return True
	elif (move == 7):
		if (tile7 == 0):
			return True
	elif (move == 8):
		if (tile8 == 0):
			return True
	elif (move == 9):
		if (tile9 == 0):
			return True

def win():
	if( ((tile1 == 1) and (tile2 == 1) and (tile3 == 1)) or ((tile1 == 2) and (tile2 == 2) and (tile3 == 2)) or ((tile2 == 1) and (tile5 == 1) and (tile8 == 1)) or ((tile2 == 2) and (tile5 == 2) and (tile8 == 2)) or ((tile3 == 1) and (tile5 == 1) and (tile7 == 1)) or
		((tile3 == 2) and (tile5 == 2) and (tile7 == 2)) or
		((tile1 == 1) and (tile5 == 1) and (tile9 == 1)) or
		((tile1 == 2) and (tile5 == 2) and (tile9 == 2)) or
		((tile1 == 1) and (tile4 == 1) and (tile7 == 1)) or
		((tile1 == 2) and (tile4 == 2) and (tile7 == 2)) or
		((tile4 == 1) and (tile5 == 1) and (tile6 == 1)) or
		((tile4 == 2) and (tile5 == 2) and (tile6 == 2)) or
		((tile3 == 1) and (tile6 == 1) and (tile9 == 1)) or
		((tile3 == 2) and (tile6 == 2) and (tile9 == 2)) or
		((tile7 == 1) and (tile8 == 1) and (tile9 == 1)) or
		((tile7 == 2) and (tile8 == 2) and (tile9 == 2))):
			return True
	else:
		return False

	
def takeNaiveMove():
	n = None
	while not validmove(n):
		n = random.randint(1, 9)
	return(n)


def takeStrategicMove():
	global tile1,tile2,tile3, tile4, tile5, tile6, tile7, tile8, tile9			
	n = 1
	while not validmove(n):
		if(tile1 == 0 or tile3 == 0 or tile7 == 0 or tile9 ==0):
			ch = random.randint(1,4)
			if(ch == 1):
				n = 1
			elif(ch == 2):
				n = 3
			elif(ch == 3):
				n = 7
			elif(ch ==4):
				n = 9
		elif(tile5 == 0):
			n = 5
		elif(tile2 ==0 or tile4 ==0 or tile6 ==0 or tile8 ==0):
			k = random.randint(1,4)
			if(k == 1):
				n = 2
			elif(k == 2):
				n = 4
			elif(k == 3):
				n = 6
			elif(k ==4):
				n = 8
	return n

def validBoard():
	num_one = 0
	num_two = 0
	if (tile1 == 1):
		num_one = num_one+1
	elif (tile1 == 2):
		num_two = num_two+1
	if (tile2 == 1):
		num_one = num_one+1
	elif (tile2 == 2):
		num_two = num_two+1
	if (tile3 == 1):
		num_one = num_one+1
	elif (tile3 == 2):
		num_two = num_two+1
	if (tile4 == 1):
		num_one = num_one+1
	elif (tile4 == 2):
		num_two = num_two+1
	if (tile5 == 1):
		num_one = num_one+1
	elif (tile5 == 2):
		num_two = num_two+1
	if (tile6 == 1):
		num_one = num_one+1
	elif (tile6 == 2):
		num_two = num_two+1
	if (tile7 == 1):
		num_one = num_one+1
	elif (tile7 == 2):
		num_two = num_two+1
	if (tile8 == 1):
		num_one = num_one+1
	elif (tile8 == 2):
		num_two = num_two+1
	if (tile9 == 1):
		num_one = num_one+1
	elif (tile9 == 2):
		num_two = num_two+1

	if(num_one == num_two):
		return True

def game(gametype=1):
	if(win()):
		if((num_one - num_two) == 1):
			return 1
		elif((num_two - num_one) == 1):
			return 2
		else :
			return 0
def game1(n):
	p1=0
	p2=0
	d=0
	global tile1,tile2,tile3, tile4, tile5, tile6, tile7, tile8, tile9							
	index = takeNaiveMove()
	for i in range(n):
		for i in range(9):
			while not validmove(index):
				index = takeNaiveMove()
			if(index ==None):
				break
			if (i%2 == 0):
				turn = player1
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
				turn = player2
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
			if(win()):
				break
		print(tile1,tile2,tile3, tile4, tile5, tile6, tile7, tile8, tile9)
		if(win()):
			if(turn == player1):
				p1 += 1
			elif (turn == player2):
				p2 += 1
		else :
			d += 1
		# print(p1,p2)
		tile1=tile2=tile3= tile4= tile5= tile6= tile7= tile8= tile9=0
	probability_1 = float(p1/n)
	probability_2 = float(p2/n)
	probability_d = float(d/n)
	return probability_1
# print(game1(1000))		

def game2(n):
	pr1 = pr2 = dr = 0
	global tile1,tile2,tile3, tile4, tile5, tile6, tile7, tile8, tile9							
	naive = takeNaiveMove()
	strat = takeStrategicMove()
	for i in range(n):
		for i in range(9):
			while not validmove(naive):
				naive = takeNaiveMove()
			while not validmove(strat):
				strat = takeStrategicMove()
			if (i%2 == 0):
				turn = 2
				if(naive == 1):
					tile1 = 1
				elif(naive == 2):	
					tile2 = 1
				elif(naive == 3):
					tile3 = 1
				elif(naive == 4):
					tile4 = 1
				elif(naive == 5):
					tile5 = 1
				elif(naive == 6):
					tile6 = 1
				elif(naive == 7):
					tile7 = 1
				elif(naive == 8):
					tile8 = 1
				elif(naive == 9):
					tile9 = 1
			elif (i%2 == 1):
				turn = 1
				if(strat == 1):
					tile1 = 2
				elif(strat == 2):
					tile2 = 2
				elif(strat == 3):
					tile3 = 2
				elif(strat == 4):
					tile4 = 2
				elif(strat == 5):
					tile5 = 2
				elif(strat == 6):
					tile6 = 2
				elif(strat == 7):
					tile7 = 2
				elif(strat == 8):
					tile8 = 2
				elif(strat == 9):
					tile9 = 2
		# print(tile1,tile2,tile3, tile4, tile5, tile6, tile7, tile8, tile9)
		# print(win(), turn)
		if(win()):
			if(turn == 1):
				 pr1 = pr1 + 1
			elif (turn == 2):
				pr2 = pr2 + 1
			else:
				dr += 1

		tile1=tile2=tile3= tile4= tile5= tile6= tile7= tile8= tile9=0
	prob_1 = pr1/n
	prob_2 = pr2/n
	draw_p = 1 - (prob_1 + prob_2)
	return prob_1	

def game3(n):
	pr1 = pr2 = dr = 0
	global tile1,tile2,tile3, tile4, tile5, tile6, tile7, tile8, tile9							
	strat_1 = takeStrategicMove()
	strat = takeStrategicMove()
	for i in range(n):
		for i in range(9):
			turn = 1
			while not validmove(strat_1):
				strat_1 = takeStrategicMove()
			while not validmove(strat):
				strat = takeStrategicMove()
			if (i%2 == 0):
				turn = 1
				if(strat_1 == 1):
					tile1 = 1
				elif(strat_1 == 2):	
					tile2 = 1
				elif(strat_1 == 3):
					tile3 = 1
				elif(strat_1 == 4):
					tile4 = 1
				elif(strat_1 == 5):
					tile5 = 1
				elif(strat_1 == 6):
					tile6 = 1
				elif(strat_1 == 7):
					tile7 = 1
				elif(strat_1 == 8):
					tile8 = 1
				elif(strat_1 == 9):
					tile9 = 1
			elif (i%2 == 1):
				turn = 2
				if(strat == 1):
					tile1 = 2
				elif(strat == 2):
					tile2 = 2
				elif(strat == 3):
					tile3 = 2
				elif(strat == 4):
					tile4 = 2
				elif(strat == 5):
					tile5 = 2
				elif(strat == 6):
					tile6 = 2
				elif(strat == 7):
					tile7 = 2
				elif(strat == 8):
					tile8 = 2
				elif(strat == 9):
					tile9 = 2
		if(win()):
			if(turn == 1):
				 pr1 = pr1 + 1
			elif (turn == 2):
				pr2 = pr2 + 1
		else:
			dr += 1
		tile1=tile2=tile3= tile4= tile5= tile6= tile7= tile8= tile9=0
	prob_1 = pr1/n
	prob_2 = pr2/n
	draw_p = 1 - (prob_1 + prob_2)
	return(prob_2)

# print(game1(1000))
# print(game2(1000))	
# print(game3(1000))

