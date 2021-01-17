#this is a simple function that returns an array of lines in a specified file
def get_lines(name):
	lines = []
	for line in open(name, 'r'):
		lines.append(line.strip('\n'))
	return lines

#return dictionary of conversions from a csv file
def get_conversions(name):
	conversions = {}
	for line in open(name, 'r'):
		line = line.strip('\n').split(', ')
		try:
			conversions[line[0]] = float(line[1])
		except:
			try:
				conversions[line[0]] = float(line[2])
			except:
				conversions[line[0]] = 'coundlnt find'
	return conversions

#iterates through and yeilds the file names in a directory as strings
def iterate_directory(path):
	names = []
	from os import listdir, fsencode, fsdecode
	path = fsencode(path)
	for file in listdir(path):
		names.append(fsdecode(file))
	return names

#finds the ingredients and returns a list of them
def get_ingredients(lines):
	start = lines.index('Ingredients')
	stop = lines.index('Steps') -1
	ingredients = []
	for ingredient in lines[start + 1 : stop]:
		ingredients.append(ingredient[3 :])
	return ingredients

#takes a list of items and returns a dictionary with their occurances in that list
def get_occurances(items):
	myHugeDict = {items[0]: 0}
	for item in items:
		if item in myHugeDict:
			myHugeDict[item] += 1
		else:
			myHugeDict[item] = 1
	return myHugeDict

#this puts a dictionary into a js file as a js dictionary
def write_dict(filename, dict, dictname):
	file = open(filename, 'a')
	file.write('var ' + dictname + ' = ' + str(dict) + ';\n')
	file.close

#write a list in a file as a js list
def write_list(filename, list, listname):
	file = open(filename, 'a')
	file.write('var ' + listname + ' = ' + str(list) + ';\n')
	file.close()

#writes a dict into a csv file
def write_csv(filename, dict):
	file = open(filename, 'a')
	for thing in dict:
		file.write(thing + ', ' + str(dict[thing]) + '\n')
	file.close()

#writes a dict based on a repeating dict
#it averages all the values with the same key
def average_dict(dict):
	product = {'example': 0}
	for thing in dict:
		if thing in product:
			if dict[thing] != 0 and dict[thing] != 0.0:
				product[thing] = (product[thing] + dict[thing]) / 2
			else:
				pee = 'poo'
		else:
			product[thing] = dict[thing]
	return product
