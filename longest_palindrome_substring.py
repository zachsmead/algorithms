longest = ''

# substring reduces the original word from right to left. addstring reduces the original word from left to right. 
def longest_palindrome_substring_2(word):
	longest_substring = longest_palindrome_substring(word, word)
	return '"%s" is the longest palindrome substring in "%s."' % (longest_substring, word)

def longest_palindrome_substring(word, substring):
	print 'STARTING POINT: %s' % word
	if recursive_palindrome(substring) == True:
		longest = substring
		if len(substring) == 1 and len(substring) < len(word):
			word = word[1:len(word)]
			substring = word
			return longest_palindrome_substring(word, substring)
	elif recursive_palindrome(substring) == False:
		return longest_palindrome_substring(word, substring[0:len(substring) - 1])

	return longest

def recursive_palindrome(word):
	print 'Is "%s" a palindrome?' % word

	if len(word) == 1: #or len(word) == 0:
		return True
	elif len(word) == 2 and word[0] == word[1]:
		return True
	elif word[0] != word[len(word) - 1]:
		return False
	elif word[0] == word[len(word) - 1]:
		return recursive_palindrome(word[1:len(word) - 1])


# print recursive_palindrome('amanaplanacanalpanama')
# print recursive_palindrome('racecar')
# print recursive_palindrome('racekar')
# print recursive_palindrome('aracekar')
# print recursive_palindrome('carrot')


print longest_palindrome_substring('aracekar', 'aracekar')
print longest_palindrome_substring('amanaplanacanalpanama', 'amanaplanacanalpanama')
print longest_palindrome_substring('carrot', 'carrot')

print longest_palindrome_substring_2('carrot')
