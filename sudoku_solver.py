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
	'5': [0, 0],
	'3': [0, 1],
	'7': [0, 4],
	'6': [1, 0],
	'1': [1, 3],
	'9': [1, 4],
	'5': [1, 5],
	'9': [2, 1],
	'8': [2, 2],
	'6': [2, 7],
	'8': [3, 0],
	'6': [3, 4],
	'3': [3, 8],
	'4': [4, 0],
	'8': [4, 3],
	'3': [4, 5],
	'1': [4, 8],
	'7': [5, 0],
	'2': [5, 4],
	'6': [5, 8],
	'6': [6, 1],
	'2': [6, 6],
	'8': [6, 7],
	'4': [7, 7],
	'1': [7, 7],
	'9': [7, 7],
	'5': [7, 7],
	'8': [8, 4],
	'7': [8, 7],
	'9': [8, 8],
}

# print 'generating a blank board...'
# print sudoku_board
# print 'populating the board...'
# populate_board(coordinate_pairs_1)
# print sudoku_board