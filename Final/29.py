gpas = ['B+','C+','D','A','B+','A','A-']
new_list = []
for gpa in gpas:
	if gpa == 'D':
		grade = '65-67'
	elif gpa == 'D+':
		grade = "67-69"
	elif gpa == 'C-':
		grade = "70-72"
	elif gpa == 'C':
		grade = "73-76"
	elif gpa == 'C+':
		grade = "77-79"
	elif gpa == 'B-':
		grade = "80-82"
	elif gpa == 'B':
		grade = "83-86"
	elif gpa == 'B+':
		grade = "87-89"
	elif gpa == 'A-':
		grade = "90-92"
	elif gpa == 'A':
		grade = "93-96"
	elif gpa == 'A+':
		grade = "97-100"
	else:
		raise Exception(f"There was a problem with {gpa}")
	new_list.append(grade)


print(new_list)