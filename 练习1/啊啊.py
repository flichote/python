# squares = [i **0.5 for i in range(1,11)]
# print(squares)
# a = [ i for i in range(1,1000001)]
# print(max(a))
# print(min(a))
# print(sum(a))
#
#
# a = [i for i in range(1,20,2)]
# print(a)
#
# a = [i*3 for i in range(1,10)]
# # print(a)
# #
# b = [i**3 for i in range(1,11)]
# #if len(b)<=2:
# print("The first three items in the list are:")
# for i in b[-3:]:
#     print(i)
#
#
# print(b)
# for i in range(len(b)-3,len(b)):
#
#     print(b[i])
#
#
#
# my_food = ['pizza','falafel','carrot cake']
# li_food = my_food[:]
# li_food.append('a_pazza')
# print('lifood:',li_food)
# print('myfood:',my_food)
#
# print("my favorite pizzas are: ")
# for i in my_food:
#     print(i)
#
# print("li favorite pizzas are:")
#
# for i in li_food:
#     print(i)
#
#
# dimensions = (200,50)
#
# print(dimensions[0])
#
# print(dimensions[1])
# print("~~~~~~~~~~~~~~")
# for dimension in dimensions:
#     print(dimension)
#
#


# dimensions = (200,50)
# print("Orginal dimensions: ")
# for dimension in dimensions:
#     print(dimension)
# dimensions = (400,100)
# print("Modidied dimensions: ")
# for dimension in dimensions:
#     print(dimension)

# frults = ('apple', 'pear', 'banana', 'grope', 'peach')
# print('The frults are: ')
# for frult in frults:
#     print(frult)

# requested_toppings = ['mushrooms','green peppers','extra cheese']
#
# for requested_topping in requested_toppings:
#     print("Adding "+ requested_topping + ".")
#
# print("\nFinished mading your pizza!")
#
#
alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])
#
# new_points = alien_0['points']
# print("You just earned " + str(new_points) + " points!")
#
# del alien_0['points']
# print(alien_0)
#
# dict = {
#     'a':'123',
#     'b':'456'
#
# }
#
# for k,v in dict.items():
#     print(v)
#
#
# for k,v in enumerate(dict):
#     print(dict[v])
#
# for key in dict:
#     print(key)
#
# for value in dict.values():
#     print(value)
#

# favorite_languages = {
#     'jen':'python',
#     'sarch':'c',
#     'edward':'ruby',
#     'phil':'python',
# }
#
# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for taking the poll.")
#
# for language in set(favorite_languages.values()):
#     print(language)
#

# aliens = []
# for alien_number in range(30):
#     new_aliens = {'color':'green','points':5,'speed':'slow'}
#     aliens.append(new_aliens)
#
# for alien in aliens[:5]:
#     print(alien)
# print('...')

# x = 1
# while x < 10:
#
#     x +=1
#     print(x)

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/ no) ")

    if repeat == 'no':
        polling_active = False
print("\n --- Poll Results --- ")
for name,response in responses.items():
    print(name + " would like to climb " + response + ".")

print(responses)
