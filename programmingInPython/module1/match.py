x = 'b'

match x:
	case 'a' | 'b':
		print('x is a OR b')
	case 'c':
		print('x is c')
	case _: # default case
		print('x did not match a case')
