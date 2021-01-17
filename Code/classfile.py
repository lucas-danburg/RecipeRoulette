from utilities import get_lines, get_conversions, iterate_directory, get_ingredients

#this function generates ingredient classes based on your input file
#returns a list of ingredient objects for the file
def generate_ingredients(filename):
	lines = get_lines(filename)
	ingredients = get_ingredients(lines)
	result = []
	for ing in ingredients:
		result.append(ingredient(ing))
	return result

#this is the 'ingredient' class
#it will contain methods that it will use to build itself based on the ingredient string that you feed it
class ingredient:
	def __init__(self, string):
		new = string.strip(' ')
		string = ''
		for character in new:
			if character != '\u2009':
				string += character
		#the lists of units and fraction conversions
		self.units = get_lines('/home/user/Projects/Python/Recipes/Data/ingredients/references/units.txt')
		self.fractions = get_conversions('/home/user/Projects/Python/Recipes/Data/ingredients/references/fractions.csv')
		self.conversions = get_conversions('/home/user/Projects/Python/Recipes/Data/ingredients/references/conversions.csv')
		#makes a list for the ingredient - [amount, 'unit', 'item']
		#as well as instance variables
		divided = self.divide(string)
		amount = self.clarify_amount(divided[0])
		if len(divided) < 3:
			self.item = self.clarify_item(divided[1])
			self.listed = [amount, self.item]
		else:
			unit = self.clarify_unit(divided[1])
			self.amount = self.convert(amount, unit)
			self.unit = 'tablespoon'
			self.item = self.clarify_item(divided[2])
			self.listed = [self.amount, self.unit, self.item]

	#breaks the string up into a rough amount, unit, item
	def divide(self, string):
		words = string.split(' ')
		found = False
		global divider
		for unit in self.units:
			for word in words:
				if word.strip(' ') in unit or word.strip(' ') == unit:
					found = True
					divider = ' ' + unit + ' '
					break
			if found == True:
				return [string.split(divider)[0], divider, string.split(divider)[1]]
		#assume there is no unit
		global first
		for word in words:
			if word[0] in 'qwertyuiopasdfghjklzxcvbnm,;\'\\-=!@#$%^&*()_+{}|:"<>?':
				first = words.index(word)
				thing = [' '.join(words[: first]), ' '.join(words[first :])]
				return [thing[0], thing[1]]
	#takes your unit string and cleans it up :)
	def clarify_unit(self, string):
		teaspoon = ['teaspoon', 'teaspoons', 'tsp', 'tsps']
		tablespoon = ['tablespoon', 'tablespoons', 'tbsp', 'tbsps']
		cup = ['cup', 'cups', 'c']
		for unit in self.units:
			if unit in string or string in unit or unit == string:
				if unit in teaspoon:
					return 'teaspoon'
				if unit in tablespoon:
					return 'tablespoon'
				if unit in cup:
					return 'cup'
				else:
					return 'DISREGARD'

	#takes your amount string and tries to add it up into a float
	#it does the best it can :)
	def clarify_amount(self, string):
		total = 0.0
		numbers = ''
		string = string.strip(' ')
		for character in string:
			if character in self.fractions:
				total += self.fractions[character]
			elif character in '.0123456789':
				numbers += character
		if numbers != '':
			total += float(numbers)
		return total
	#this cleans up your item a little bit maybe
	#its not 100% necessary
	def clarify_item(self, string):
		return string.strip('\n\t\\|,. ')

	#converts anything to tablespoons for easy stat building
	def convert(self, amount, unit):
		return self.conversions[unit] * amount

	def string(self):
		if len(self.listed) < 3:
			print('Amount: ' + str(self.listed[0]))
			print('Item:   ' + self.listed[1])
		else:
			print('Amount: ' + str(self.listed[0]))
			print('Unit:   ' + self.listed[1])
			print('Item:   ' + self.listed[2])
