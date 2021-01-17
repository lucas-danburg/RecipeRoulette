from utilities import iterate_directory, write_list, write_dict, get_lines, get_conversions

lines = get_lines('information/actions.txt')
write_list('otherstuff.js', lines, 'actions')
dict = get_conversions('information/actions.csv')
write_dict('otherstuff.js', dict, 'action_occurances')
for filename in iterate_directory('information/associations'):
	conversions = get_conversions('information/associations/' + filename)
	write_dict('otherstuff.js', conversions, filename[: -3].strip(', .\\/<>?{}[]|;:"\'=-0987654321`~!@#$%^&*()_+').lower())

