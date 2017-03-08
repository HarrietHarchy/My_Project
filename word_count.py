def words(remarks):
	my_dict={}
	break_data = remarks.split()
	for i in break_data:
		if i.isdigit():
			count=break_data.count(i)
			my_dict[i]=count
		else:
			count = break_data.count(i)
			my_dict[i]= count
	return my_dict
			


print (words("this is my house 9876"))

