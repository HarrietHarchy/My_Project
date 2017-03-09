def find_max_min(i_list):
	if type(i_list)==list:
		maximum= max(i_list)
		minimum = min(i_list)

	if maximum==minimum:
		z=len(i_list)
		return [z]
	else:
			print([maximum,minimum])
	
find_max_min([4,4,4,4])
find_max_min([1,2,3,4])
find_max_min([6,4])
find_max_min([4,66,6,44,7,78,8,68,2 ])

     


  

 