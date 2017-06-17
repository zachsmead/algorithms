def recursive_palindrome(word):
	print 'Is %s a palindrome?' % word

	if len(word) == 1: #or len(word) == 0:
		return True
	elif word[0] != word[len(word) - 1]:
		return False
	elif word[0] == word[len(word) - 1]:
		return recursive_palindrome(word[1:len(word) - 1])


print recursive_palindrome('amanaplanacanalpanama')
print recursive_palindrome('racecar')
print recursive_palindrome('racekar')
print recursive_palindrome('carrot')