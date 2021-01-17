from utilities import get_conversions, write_dict, write_list, iterate_directory, get_lines

ingredient_names = get_lines('information/items.txt')
write_list('stuff.js', ingredient_names, 'names')

occurances = get_conversions('information/occurances.csv')
write_dict('stuff.js', occurances, 'occurances')

counter = 0
for filename in iterate_directory('information/associations'):
	associations = get_conversions('information/associations/' + filename)
	name = ''
	for character in filename:
		if character in ')(*&^%$#@!~`-=_+[]\\|}{;\'":<>?,./1234567890':
			name += '_'
		else:
			name += character
	if 'Dew' not in name and 'Nuts' not in name and 'Ruth' not in name and 'Jell' not in name:
		write_dict('stuff.js', associations, 'association_' + name)
		counter += 1
		print(str(counter), end = '\r')

#associations_reference = {}
#for filename in iterate_directory('information/associations'):
#	dict_name = 'association_' + filename
#	name = ' '.join(filename[: -3].split('_'))
#	associations_reference[name] = dict_name
#write_dict('stuff.js', associations_reference, 'associations_reference')


for filename in iterate_directory('information/proportions'):
	proportions = get_conversions('information/proportions/' + filename)
	name = ''
	for character in filename:
		if character in '`1234567890-=[]\\;\',./~!@#$%^&*()_+{}|:"<>?':
			name += '_'
		else:
			name += character
	if 'Dew' not in name and 'Nuts' not in name and 'Ruth' not in name and 'Jell' not in name:
		write_dict('stuff.js', proportions, 'proportions_' + name)
		counter += 1
		print(str(counter), end = '\r')

#proportions_reference = {}
#for filename in iterate_directory('information/proportions'):
#	proportions_reference[' '.join(filename[: -4].split('_'))] = 'proportion_' + filename
#write_dict('stuff.js', proportions_reference, 'proportions_reference')
