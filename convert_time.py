def convert_time(string):
	print('converting %s...' % string)
	if 'AM' in string:
		print('the time is in the AM.')
		if string[:2] == '12':
			print('it starts with 12, so change it to 00 instead.')
			string = '00%s' % string[2:]
		return string[:len(string) - 2]
	elif 'PM' in string:
		print('the time is in the PM.')
		if string[:2] == '12':
			pass
		else:
			print('the time is after 12, so add 12 to get the military time.')
			string = '%s%s' % (str(int(string[:2]) + 12), string[2:])
		return string[:len(string) - 2]

print('AM tests:')
print(convert_time('12:00:01AM'))
print(convert_time('10:00:01AM'))
print(convert_time('09:00:01AM'))

print('PM tests:')
print(convert_time('12:00:01PM'))
print(convert_time('10:00:01PM'))
print(convert_time('09:00:01PM'))