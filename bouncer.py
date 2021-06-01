# as for age
print('How old are you?')
age = input()

if age:
	age = int(age)
	if age >=21:
		print('Drink')
	elif (age) >= 18:
		print('No drink')
	else:
		print('You can\'t come in little one. :(')
else:
	print('Please enter an age')


