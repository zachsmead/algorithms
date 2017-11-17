length_record = 0

def longest_valid_parenthesis(string, length):
	global length_record

	print 'examining "%s"' % string

	if len(string) == 1:
		print 'reached the end of the string.'
		print 'the longest valid parenthetical substring is %d characters long!' % length_record
	elif string[len(string) - 1] == '(':
		print 'open parenthesis at the last character - lets cut it off first.'
		return longest_valid_parenthesis(string[0:len(string) - 1], length)
	elif string[0] == ')':
		print 'open parenthesis at the first character - lets cut it off.'
		length = 0
		return longest_valid_parenthesis(string[1:len(string)], length)
	elif string[0] == '(':
		print 'the first character is valid. lets look at the next one.'
		if string[1] == '(':
			length = 0
			print 'the next character is not valid, so lets cut off the first character and re-examine the new string.'
			return longest_valid_parenthesis(string[1:len(string)], length)
		elif string[1] == ')':
			print 'the next character is valid, so lets count it and move on.'
			length += 2
			if length > length_record:
				length_record = length
				print 'we have a new record!'
			print 'current length is %d.' % length
			print 'greatest length so far is %d.' % length_record
			return longest_valid_parenthesis(string[2:len(string)], length)
	return length


string_1 = ')()())'
string_2 = '(())()()))()()()()())('
string_3 = '(())()()))()()()()())((((((((('

longest_valid_parenthesis(string_2, 0)
longest_valid_parenthesis(string_3, 0)


