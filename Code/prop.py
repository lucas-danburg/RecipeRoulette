from utilities import get_lines, iterate_directory, get_ingredients, get_occurances, write_csv, average_dict
from classfile import ingredient, generate_ingredients

class recipe:
	def __init__(self, ingredients):
		self.items = {}
		for ingredient in ingredients:
			self.items[ingredient.item] = ingredient.listed[0]

all_items = get_lines('information/items.txt')
for item in all_items:
	try:
		all_props = {}
		for file in iterate_directory('/home/user/Projects/Python/Recipes/Cookbook'):
			temp = {}
			log = open('log_prop.txt', 'w')
			log.write('item: ' + item + ', file: ' + file)
			log.close()
			ingredients = generate_ingredients('/home/user/Projects/Python/Recipes/Cookbook/' + file)
			rec = recipe(ingredients)
			if item in rec.items:
				for food in rec.items:
					temp[food] = rec.items[item] / (rec.items[food] + 0.000001)
			else:
				for food in rec.items:
					temp[food] = 0
			for food in temp:
				if food not in all_props:
					all_props[food] = temp[food]
				else:
					if temp[food] != 0:
						all_props[food] = (all_props[food] + temp[food]) / 2
		name = '_'.join(item.strip(' "\'').split(' ')).strip(' "\'').strip("'").strip('"') + '.csv'
		write_csv('information/proportions/' + name, all_props)
		print('done')
	except:
		pee = 'poo'
