ingredient_list = #an array of the final ingredients to be used
action_list_full = #a list thats full of all the action vars, like var knead and stuff
possible_actions = #an array (empty) to be filled with actions
for ingredient in ingredient_list:
    for action in action_list_full:
        #is the ingreient string equal to any of the keys in that action var dictionary?
        if ingredient in action:
            #add that action to the list of possible actions
            possible_actions.add(action)

#now we have a list (possible_actions) of all the actions we could take
#based on the ingredients we have
#now lets see if we can narrow it down

#a loop that increases a threshold every time to narrow down ingredients
for(int threshold = 0; possible_actions.length > 9; threshold += 25):
    for action in possible_actions:
        if action_occurance[action] < threshold:
            #if the actions occurance doesnt make the threshold, it is removed
            #the threshold increases every time to narow things down
            possible_actions.remove(action)

#finally we have good-sized list of actions to use
#now lets figure out what to use them on
final_actions = {}#a dictionary mapping action to ingredient(s)
#this part should be simple
#for each action
for action in possible_actions:
    #this is a list of ingredients that the partiular action will be applied to
    action_ingredient_list = []
    #for each ingredient string in the 'var action ={...' dictionary
    for ingredient in action:
        #if that ingredient is also in our list of ingredients
        if ingredient in ingredient_list:
            #add that ingredient to the list of ingredients for that particular action
            action_ingredient_list.add(ingredient)
    #add the action to our final actions, pointing to the ingredients
    final_actions[action] = action_ingredient_list

#final actions should look like:
{mix = [eggs, flour, milk], knead = [flour, milk, yeast]}
