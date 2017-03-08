def data_type(z):
	if type(z) == str:
		return len(z)
	elif z is None:
	  return str('no value')

	elif type(z) == bool:
		return z
	elif type(z) == int:
		if z < 100:
			return 'less than 100'
		elif z == 100:
			return 'equal to 100'
		else:
			return 'more than 100'
	elif type(z) == list:
		if len(z) > 2:
		  return z[2]
		if len(z) < 2:
		  return None
	