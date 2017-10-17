from a import *

def check_valid_move():

	assert (validmove(1)==True), "Valid Move"
	assert (validmove(2)==True), "Valid Move"
	assert (validmove(3)==True), "Valid Move"
	assert (validmove(4)==True), "Valid Move"
	assert (validmove(5)==True), "Valid Move"
	assert (validmove(6)==True), "Valid Move"
	assert (validmove(7)==True), "Valid Move"
	assert (validmove(8)==True), "Valid Move"
	assert (validmove(9)==True), "Valid Move"

def check_win():
	tile1= 1	   
	tile2= 0
	tile3= 0
	tile4= 2
	tile5= 1
	tile6= 2
	tile7= 1
	tile8= 0
	tile9= 1
	assert (win()==False), "Game lost"

def check_valid_board():
	tile1= 1	   
	tile2= 2
	tile3= 1
	tile4= 2
	tile5= 1
	tile6= 2
	tile7= 1
	tile8= 2
	tile9= 1
	# num_one = 0
	# num_two = 0
	assert (validBoard()==True), "Board invalid"	

if __name__ == '__main__':
	check_valid_move()
	check_win()
	check_valid_board()
