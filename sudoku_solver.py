sudoku_board = [['.'] * 9] * 9

def populate_board(coordinate_pairs):
	for number in coordinate_pairs:
		place_number_on_board(number, coordinate_pairs(number))

def place_number_on_board(number, coordinate):
	global sudoku_board
	sudoku_board[coordinate[0]][coordinate[1]] = number

def sudoku_solver():
	pass



coordinate_pairs_1 = {
	[0, 0]: '5',
	[0, 1]: '3',
	[0, 4]: '7',
	[1, 0]: '6',
	[1, 3]: '1',
	[1, 4]: '9',
	[1, 5]: '5',
	[2, 1]: '9',
	[2, 2]: '8',
	[2, 7]: '6',
	[3, 0]: '8',
	[3, 4]: '6',
	[3, 8]: '3',
	[4, 0]: '4',
	[4, 3]: '8',
	[4, 5]: '3',
	[4, 8]: '1',
	[5, 0]: '7',
	[5, 4]: '2',
	[5, 8]: '6',
	[6, 1]: '6',
	[6, 6]: '2',
	[6, 7]: '8',
	[7, 7]: '4',
	[7, 7]: '1',
	[7, 7]: '9',
	[7, 7]: '5',
	[8, 4]: '8',
	[8, 7]: '7',
	[8, 8]: '9'
}

# print 'generating a blank board...'
# print sudoku_board
# print 'populating the board...'
# populate_board(coordinate_pairs_1)
# print sudoku_board

print coordinate_pairs_1
print coordinate_pairs_1(5)








