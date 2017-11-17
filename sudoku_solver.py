sudoku_board = [
	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	['.', '.', '.', '.', '.', '.', '.', '.', '.'],
	['.', '.', '.', '.', '.', '.', '.', '.', '.']
]

class Cell(object):
	global sudoku_board

	def __init__(self):
		self.value = '.'
		self.possible_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

	def eliminate_values(number_array):
		for value in number_array:
			if value != '.':
				self.possible_values.remove(value)
				if len(self.possible_values) == 1:
					self.value = self.possible_values[0]


def print_board(board):
	for row in board:
		print row
			

def populate_board(board, coordinate_pairs):
	for key in coordinate_pairs:
		print 'coordinate: %s' % key
		print 'number: %s' % coordinate_pairs[key]
		place_number_on_board(board, key, coordinate_pairs[key])

def place_number_on_board(board, coordinate, number):
	print_board(board)
	row = int(coordinate[0])
	column = int(coordinate[3])
	print '%s goes to row %s, column %s' % (number, row, column)
	board[row][column] = number

def row_check():
	pass

def column_check():
	pass

def square_check():
	pass

def sudoku_solver():
	pass



coordinate_pairs_1 = {
	'0, 0': '5',
	'0, 1': '3',
	'0, 4': '7',
	'1, 0': '6',
	'1, 3': '1',
	'1, 4': '9',
	'1, 5': '5',
	'2, 1': '9',
	'2, 2': '8',
	'2, 7': '6',
	'3, 0': '8',
	'3, 4': '6',
	'3, 8': '3',
	'4, 0': '4',
	'4, 3': '8',
	'4, 5': '3',
	'4, 8': '1',
	'5, 0': '7',
	'5, 4': '2',
	'5, 8': '6',
	'6, 1': '6',
	'6, 6': '2',
	'6, 7': '8',
	'7, 3': '4',
	'7, 4': '1',
	'7, 5': '9',
	'7, 8': '5',
	'8, 4': '8',
	'8, 7': '7',
	'8, 8': '9'
}

print 'generating a blank board...'
print sudoku_board
print 'populating the board...'
populate_board(sudoku_board, coordinate_pairs_1)
print_board(sudoku_board)








