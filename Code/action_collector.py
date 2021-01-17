from utilities import get_lines, get_steps, iterate_directory, get_words, get_sentences, get_occurances, write_csv

actions = get_lines('information/actions.txt')
ingredients = get_lines('/home/user/Projects/Python/Recipes/Data/ingredients/information/items.txt')

a = 0
for action in actions:
	a += 1
	associated = []
	f = 0
	for filename in iterate_directory('/home/user/Projects/Python/Recipes/Cookbook'):
		f += 1
		for step in get_steps(get_lines('/home/user/Projects/Python/Recipes/Cookbook/' + filename)):
			s = 0
			for sentence in get_sentences(step):
				s += 1
				if action in get_words(sentence):
					for word in get_words(sentence):
						for ingredient in ingredients:
							if ingredient in word or word == ingredient:
								associated.append(ingredient)
				print('Action: ' + str(a) + '		File: ' + str(f) + '		Sentence: ' + str(s), end = '\r')

	occurance = {}
	try:
		occurance = get_occurances(associated)
	except:
		occurance['all'] = 0
	write_csv('information/associations/' + action + '.csv', occurance)
