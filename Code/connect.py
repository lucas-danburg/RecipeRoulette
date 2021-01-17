from utilities import get_lines, iterate_directory, get_ingredients, get_occurances, write_csv
from classfile import ingredient, generate_ingredients

class recipe:
	def __init__(self, ingredients):
		self.items = []
		for ingredient in ingredients:
			self.items.append(ingredient.item)

all_items = get_lines('information/items.txt')
total_associations = []
for item in all_items:
	try:
		for file in iterate_directory('/home/user/Projects/Python/Recipes/Cookbook'):
			ings = generate_ingredients('/home/user/Projects/Python/Recipes/Cookbook/' + file)
			r = recipe(ings)
			if item in r.items:
				for it in r.items:
					total_associations.append(it)
			log = open('log_connect.txt', 'w')
			log.write('item: ' + item + ', file: ' + file + ', associations: ' + str(len(total_associations)))
			log.close()

		global dict
		dict = {}
		if len(total_associations) > 0:
			dict = get_occurances(total_associations)

		name = '_'.join(item.strip(' "\'').split(' ')).strip(' "\'').strip("'").strip('"') + 'csv'

		if len(total_associations) < 1:
			for item in all_items:
				dict[item] = 0

		write_csv('information/associations/' + name, dict)
	except:
		pee = 'poo'
