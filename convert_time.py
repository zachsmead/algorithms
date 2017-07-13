def convert_time(string):
	if 'AM' in string:
		print('first if triggered')
		if string[:2] == '12':
			print('2nd if triggered')
			string = '00%s' % string[2:]
		return string[:len(string) - 2]
	elif 'PM' in string:
		print('3rd if triggered')
		if string[:2] == '12':
			print('4th if triggered')
			# string = '00%s' % string[2:]
		else:
			string = '%s%s' % (str(int(string[:2]) + 12), string[2:])
		return string[:len(string) - 2]


print(convert_time('12:00:01AM'))
print(convert_time('10:00:01AM'))
print(convert_time('09:00:01AM'))
print(convert_time('12:00:01PM'))
print(convert_time('10:00:01PM'))
print(convert_time('09:00:01PM'))