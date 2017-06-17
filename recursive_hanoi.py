# in Towers of Hanoi, think of both aux and target, together, as a pair of pegs that you switch between repeatedly,
# when you recursively call recursive_hanoi.

def recursive_hanoi(n, source, aux, target): # n = number of disks; source, aux and target = 'pegs' that hold disks
	print(n, source, aux, target)
	if n >= 1:
		# target.append(source.pop())
		recursive_hanoi(n - 1, source, target, aux)
		move_disk(source, target)
		recursive_hanoi(n - 1, target, aux, source)

def move_disk(fp, tp):
    print 'moving from %s to %s' % (fp, tp)



# source, aux, target = range(5, 1, -1) [], []
recursive_hanoi(5, 'a', 'b', 'c')

