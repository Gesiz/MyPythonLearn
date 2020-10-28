# print("Hello World!")
# print("Hello Again")
# print("I like typing this.")
# print("This is fun.")
# print('Yay! Printing.')
# print("I'd much rather you 'not'.")
# print('I "said" do not touch this.')

# A comment,this is so you can read your program later
# Anything after the # is ignored by python

# print("I could have code like this.")  # and the comment after is ignored

# You can also use a comment to "disable" or comment out code:
# print(This won't run.)

# print("This will run")

# print("I will now cunt my chickens")

# print("hens", 25+30 / 6)

# print("Roosters", 100.0 - 25.0 * 3 % 4)

# print("Now I will count the eggs:")

# print(3.0 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

# print("Is it true that 3+ 2 < 5 - 7 ?")

# print(3 + 2 < 5 - 7)

# print("What is 3 + 2", 3.0 + 2)
# print("What is 5 - 7", 5 - 7)

# print("Oh, that's why it's False ")

# print("How about some more.")
# print("Is it greater ?", 5 > -2)
# print("Is it greater or equal?", 5 >= -2)
# print("Is it less or equal>", 5 <= -2)

# cars = 100
# space_in_a_car = 4.0
# drivers = 30
# passengers = 90
# cars_not_driven = cars - drivers
# cars_driven = drivers
# carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car = passengers / cars_driven

# print("There are", cars, "cars available")
# print("There are only", drivers, "drivers available")
# print("There will be", cars_not_driven, "empty cars today")
# print("We can transport", carpool_capacity, "people today")
# print("We have", passengers, "to carpool today")
# print("We need to put about", average_passengers_per_car, "in each car")

# my_name = 'zed A. Shaw'
# my_age = 35  # not a lie
# my_height = 74  # inches
# my_weight = 180  # lbs
# my_eyes = 'Blue'
# my_teeth = 'White'
# my_hair = 'Brown'

# print(f"Let's talk about {my_name}.")
# print(f"He's {my_height} inches tall.")
# print(f"He's {my_weight} pounds heavy.")
# print("Actually that's not too heavy")
# print(f"He's got{my_eyes} eyes and {my_hair}hair")
# print(f"His teeth are usually {my_teeth} depending on the coffee")

# types_of_people = 10  # 赋值为10
# x = f"There are {types_of_people} type of people"  # 创建一个格式化字符串

# binary = "binary"  # 创建一个普通字符串
# do_not = "don't"   # 创建一个普通字符串
# y = f"Those who know {binary} and those who {do_not}"  # 创建一个格式化字符串

# print(x)  # 打印x
# print(y)  # 打印y

# print(f"I said :{x}")  # 创建格式化字符串
# print(f"I also said:'{y}'")  # 创建格式化字符串

# hilarious = False  # 赋值一个boolean 类型数据
# joke_evaluation = "Isn't that joke so funny? {}!"  # 创建一个普通字符串
# print(joke_evaluation.format(hilarious))  # 在合适的中括号内赋值

# print(f"{0}, {0}, {1}".format("hello", "world"))

# hilarious = True

# w = "This is the left side of ..."
# e = "a string with a right side"
# print(w+e)
"""
print("Mary had a little lamb")

print("Its fleece was white as {}".format('snow'))

print("And everywhere that Mary went .")

print("." * 10)  # what'd that do

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end . try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)



formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter.format("hello", "world", "my", "honor"), formatter, formatter, formatter))
print(formatter.format("Try your", "Own text here", "Maybe a poem", "or a song about fear"))
"""

# Here's some new strange stuff remember type it exactly

# days = "Mon Tue Wed Thu Fri Sat Sun"
# months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# print("Here are the days:", days)
# print("Here are the months: ", months)

# print("""
# There's something going on here . With the three double-quotes . We'll be able to type as much as we like.
# Even 4 lines if we want , or 5, or 6.
# """
#      )

# tabby_cat = "\t I'm tabbed in."
# persian_cat = "I'm split \non a line"
# backslash_cat = "I'm \\ a \\ cat"

# fat_cat = """
# I'll do a list:
# \t* Cat food
# \t* Fishies
# \t* Catnip\n\t* Grass
# """

# fat_cat = '''
# I'll do a list:"A"
# \t* Cat food
# \t* Fishies
# \t* Catnip\n\t* Grass
# '''

# print(tabby_cat)
# print(persian_cat)
# print(backslash_cat)
# print(fat_cat)

# print("How old are you ?", end=' ')
# age = input()
# print("How tall are you?", end=' ')
# height = input()
# print("How much do you weight?", end='')
# weight = input()
# print(f"So, you're {age} old, {height} tall and {weight} heavy.")
# age = input("How old are you ?")
# height = input("How tall are you ?")
# weight = input("How much do you weight ?")
# print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# from sys import argv
# read the WYSS section for how to run this
# script, first, second, third = argv
# print("The script is called :", script)
# print("Your first variable is:", first)
# print("Your second variable id:", second)
# print("Your third variable is:", third)
# from sys import argv
#
#
# script, user_name = argv
# prompt = '>'
#
# print(f"Hi {user_name },I'm the {script} script")
# print("I'd like to ask you a few questions.")
# print(f"Do you like me {user_name}")
# likes = input(prompt)
#
# print("What kind of computer do you have")
# computer = input(prompt)
#
# print(f"""
#     Alright,so you said {likes} about liking me. You live in {likes}.Not sure where that is.
# And you have a{computer} computer. Nice.
# """)
#
# from sys import argv
#
# script, filename = argv
#
# txt = open(filename)
#
# print(f"Here's your file {filename}:")
# print(txt.read())
#
# print("Type the filename again:")
# file_again = input("> ")
# text_again = open(file_again)
#
# print(text_again.read())

# from sys import argv
#
# script, filename = argv
#
# print(f"We're going to erase {filename}.")
# print("If you don't want that, hit CTRL-C(^C).")
# print("If you do want that, hit RETURN")
#
# input("?")
#
# print("Opening the file...")
# target = open(filename, 'w')
#
# print("Truncating the file Goodbye")
# target.truncate()
# print("Now I'm going to ask you for three lines.")
# line1 = input("line 1 :")
# line2 = input("line 2 :")
# line3 = input("line 3 :")
#
# print("I'm going to write these to the file.")
#
# target.write(line1+"\n")
# target.write(line2+"\n")
# target.write(line3+"\n")
#
# print("And finally ,we close it.")
# target.close()

# from sys import argv
# from os.path import exists
#
# script, from_file, to_file = argv
#
# print(f"Copying from {from_file} to {to_file}")
#
# # we could do these two on one line ,how?
# in_file = open(from_file)
# indata = in_file.read()
#
# print(f"The input file is {len(indata)} bytes long")
#
# print(f"Does the output file exist ? {exists(to_file)}")
# print("Ready ,hit RETURN to continue, CTRL-C to abort.")
# input(">: ")
#
# out_file = open(to_file, 'w')
# out_file.write(indata)
#
# print("Alright ,all done")
#
# out_file.close()
# in_file.close()

# this one is like your scripts with argv

# def print_two(*args):
#     arg1, arg2 = args
#     print(f"arg1:{arg1},arg2:{arg2}")
#
#
# # ok, that *args is actually pointless , we can just do this
# def print_two_again(arg1, arg2):
#     print(f"arg1:{arg1},arg2:{arg2}")
#
#
# # this just takes one argument
# def print_one(arg1):
#     print(f"arg1:{arg1}")
#
#
# def print_none():
#     print("I got nothing'.")
#
#
# print_two("zed", "shaw")
# print_two_again("zed", "shaw")
# print_one("First")
# print_none()


# def cheese_and_crackers(cheese_count, boxes_of_crackers):
#     print(f"You have {cheese_count} cheeses!")
#     print(f"You have {boxes_of_crackers} boxes of crackers!")
#     print(f"Man that's enough for a party!")
#     print("Get a blanket .\n")
#
#
# print("we can just give the function numbers directly:")
# cheese_and_crackers(20, 30)
#
#
# print("OR, we can use variables from our script:")
# amount_of_cheese = 10
# amount_of_crackers = 50
#
# cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#
# print("We can even do math inside too:")
# cheese_and_crackers(10+20, 5+6)
#
# print("And we can combine the two, variables and math:")
# cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)
#
# from sys import argv
#
# script, input_file = argv
#
#
# def print_all(f):
#     print(f.read())
#
#
# def rewind(f):
#     f.seek(0)
#
#
# def print_a_line(line_count, f):
#     print(line_count, f.readline(), end="")
#
#
# current_file = open(input_file)
#
# print("First let's print the whole file:\n")
#
# print_all(current_file)
#
# print("Now let's rewind, kind of like a tape")
#
# rewind(current_file)
#
# print("Let's print three lines:")
#
# current_line = 1
# print_a_line(current_line, current_file)
#
# print_a_line(current_line+1, current_file)
#
# print_a_line(current_line+2, current_file)

#
# def add(a, b):
#     print(f"ADDING{a}+{b}")
#     return a + b
#
#
# def subtract(a, b):
#     print(f"SUBTRACTING {a} - {b}")
#     return a - b
#
#
# def multiply(a, b):
#     print(f"MULTIPLYING {a} * {b}")
#     return a * b
#
#
# def divide(a, b):
#     print(f"DIVIDING {a} / {b}")
#     return a / b
#
#
# print("Let's do some math with just functions!")
#
# age = add(30, 5)
# height = subtract(78, 4)
# weight = multiply(90, 2)
# iq = divide(100, 2)
#
# print(f"Age: {age}, Height: {height},Weight: {weight}, iq: {iq}")
#
# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#
# print("That becomes:", what,"Can you do it by hand?")

# import sys
# from sys import argv
#
#
# script, encoding, error = argv
#
#
# def main(language_file, encoding, errors):
#     line = language_file.readline()
#
#     if line:
#         print_line(line, encoding, errors)
#         return main(language_file, encoding, errors)
#
#
# def print_line(line, encoding, errors):
#     next_lang = line.strip()
#     raw_bytes = next_lang.encode(encoding, errors=errors)
#     cooked_string = raw_bytes.decode(encoding, errors=errors)
#
#     print(raw_bytes, "<==>", cooked_string)
#
#
# languages = open("languages.txt", encoding="utf-8")
#
# main(languages, encoding, error)

# print("Let;s practice everything.")
# print('You\'d need to know \'bout escapes with \\ that do:')
# print('\n newlines and \t tabs.')
#
# poem = """
# \t The lovely world
# with logic so firmly planted
# cannot discern \n the needs of love
# nor comprehend passion from intuition
# and requires an explanation
# """
#
# print("-"*10)
# print(poem)
# print("-"*10)
#
# five = 10 - 2 + 3 - 6
# print(f"This should be five: {five}")
#
#
# def secret_formula(started):
#     jelly_beans = started * 500
#     jars = jelly_beans / 1000
#     crates = jars / 100
#     return jelly_beans, jars, crates
#
#
# start_point = 10000
# beans, jars, creates = secret_formula(start_point)
#
# # remember that this is another way to format a string
# print("With a starting point of: {}".format(start_point))
# # it's just like with an f"" string
# print(f"we'd have {beans} beans, {jars} jars, {creates} creates.")
#
# start_point = start_point / 10
#
# print("We can also do that this way:")
# formula = secret_formula(start_point)
# # this is an easy way to apply a list to a format string
#
# print("We'd have{}beans,{}jars,{}creates".format(*formula))
#
# def break_word(stuff):
#     """This function will break up words for us."""
#     words = stuff.split(' ')
#     return words
#
#
# def sort_word(words):
#     """Sort the words"""
#     return sorted(words)
#
#
# def print_first_word(word):
#     """Prints the first word after popping it off."""
#     word = word.pop(0)
#     print(word)
#
#
# def print_last_word(words):
#     """Prints the last word after popping it off."""
#     word = words.pop(-1)
#     print(word)
#
#
# def sort_sentence(sentence):
#     """Takes in a full sentence and returns the sorted words"""
#     words = break_word(sentence)
#     return sort_word(words)
#
#
# def print_first_and_last(sentence):
#     """Prints the first and last words of the sentence."""
#     words = break_word(sentence)
#     print_first_word(words)
#     print_last_word(words)
#
#
# def print_first_and_last_sorted(sentence):
#     """Sorts the words then prints the first and last one."""
#     words = sort_sentence(sentence)
#     print_first_word(words)
#     print_last_word(words)
#

# print("True and True :", True and True)
# print("False and True :", False and True)
# print("1 == 1 and 2 == 1 :", 1 == 1 and 2 == 1)
# print("\"test\" == \"test\":", "test" == "test")
#
# people = 20
# cats = 30
# dogs = 15
#
# if people < cats:
#     print("Too many cats")
#
# if people > cats:
#     print("Not many cats")
#
# if people < dogs:
#     print("The word is drooled on")
#
# if people > dogs:
#     print("The word is dry")
#
# dogs += 5
#
# if people >= dogs:
#     print("People are greater than or equal to dogs")
#
# if people <= dogs:
#     print("People are less than or equal to dogs")
#
# if people == dogs:
#     print("People are dogs.")
#
# people = 30
# cars = 40
# trucks = 15
#
# if cars > people:
#     print("We should take the cars.")
# elif cars < people:
#     print("We should not take the cars.")
# else:
#     print("We can't decide")
#
# if trucks > cars:
#     print("That's too many truck.")
# elif trucks < cars:
#     print("That's too many truck.")
# else:
#     print("We still can't decide")
#
# if people > trucks:
#     print("Alright , let' just take the trucks")
# else:
#     print("Fine, let's stay home then .")
#
# print("""You enter a dark room with two doors. Do you go through door #1 or door #2""")
# door = input("> ")
#
# if door == "1":
#     print("There's a giant bear here eating a cheese cake.")
#     print("What do you do ?")
#     print("1. Take the cake.")
#     print("2. Scream at the bear ")
#
#     bear = input("> ")
#
#     if bear == "1":
#         print("The bear eats your face off. good job")
#     elif bear == "2":
#         print("The bear eats your legs off.Good job")
#     else:
#         print(f"Well, doing {bear} is probably better")
#         print("bear run away")
#
# elif door == "2":
#     print("You stare into the endless abyss at cthulhu's retina.")
#     print("1. Blueberries.")
#     print("2. Yellow jacket clothespins.")
#     print("3. Understanding revolvers yelling melodies.")
#
#     insanity = input("> ")
#
#     if insanity == "1" or insanity == "2":
#         print("Your body survives powered by a mind of jello.")
#         print("Good job")
#     else:
#         print("The insanity rots your eyes into a pool of muck")
#         print("Good job!")
#
# else:
#     print("You stumble around and fall on a knife and die . Good job")
#

# the_count = [1, 2, 3, 4, 5]
# fruits = ['apples', 'oranges', 'pears', 'apricots']
# change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
#
# # this first kind of for-loop goes through a list
# for number in the_count:
#     print(f"This is count {number}")
#
# # same as above
#
# for fruit in fruits:
#     print(f"A fruit of type:{fruit}")
#
# # also we can go through mixed lists too
# # notice we have to use {} since we don't know what;s in it
#
# for i in change:
#     print(f"I got {i}")
#
# # we can also build lists , first start with an empty one
# elements = []
#
# # then use the range function to do 0 to 5 counts
# for i in range(0, 6):
#     print(f"Adding {i} to the list")
#     # append is a function that lists understand
#     elements.append(i)
#
# # now we can print them out too
# for i in elements:
#     print(f"Element was: {i}")

# i = 0
# numbers = []
#
# while i < 6:
#     print(f"At the top i is{i}")
#     numbers.append(i)
#
#     i = i + 1
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")
#
# print("The numbers")
#
# for num in numbers:
#     print(num)

#
# number = []
# for i in range(1, 6):
#     number.append(i)
#
# for i in number:
#     print(i)


# from sys import exit
#
#
# def gold_room():
#     print("This room is full of gold. How much do you take")
#
#     choice = input("> ")
#
#     if "0" in choice or "1" in choice:
#         how_much = int(choice)
#     else:
#         dead("Man, learn to type a number")
#
#     if how_much < 50:
#         print("Nice, you're not greedy, you win")
#         exit(0)
#     else:
#         dead("You greedy bastard")
#
#
# def dead(why):
#     print(why, "Good job!")
#     exit(0)
#
#
# def bear_room():
#     print("There is a bear here.")
#     print("The bear has a bunch of honey")
#     print("The fat bear is in front of another door.")
#     print("How are you going to move the bear ?")
#     bear_moved = False
#
#     while True:
#         choice = input("> ")
#
#         if choice == "take honey":
#             dead("The bear looks at you then slaps your face off.")
#         elif choice == "taunt bear" and not bear_moved:
#             print("The bear has moved from the door")
#             print("You can go through it now ")
#             bear_moved = True
#         elif choice == "taunt bear" and bear_moved:
#             dead("The bear gets pissed off and chews your leg off.")
#         elif choice == "open door" and bear_moved:
#             gold_room()
#         else:
#             print("I got no idea what that means")
#
#
# def cthulhu_room():
#     print("Here you see the great evil cthulhu")
#     print("He, it, whatever stares at you and you go insane.")
#     print("Do you flee for your life or eat you head")
#
#     choice = input("> ")
#     if "flee" in choice:
#         start()
#     elif "head" in choice:
#         dead("Well that was tasty!")
#     else:
#         cthulhu_room()
#
#
# def start():
#     print("you are in a dark room")
#     print("There is a door to your right and left.")
#     print("Which one do you take")
#
#     choice = input("> ")
#
#     if choice == "left":
#         bear_room()
#     elif choice == "right":
#         cthulhu_room()
#     else:
#         dead("You stumble around the room until you starve.")
#
#
# start()
#
# ten_things = "Apples Oranges crows Telephone Light Sugar"
#
# print("Wait there are not 10 thing in that list . Let's fix that.")
# stuff = ten_things.split(' ')
#
# more_stuff = {"Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"}
#
# print(len(stuff))
#
# while len(stuff) != 10:
#     next_one = more_stuff.pop()
#     print("Adding :", next_one)
#
#     stuff.append(next_one)
#     print(f"There are {len(stuff)} items now")
#
# print("There we go", stuff)
#
# print("Let's do some things with stuff.")
#
# print("stuff[1]", stuff[1])
# print("stuff[-1]", stuff[-1])
#
# print(stuff.pop())
#
# print(' '.join(stuff))
# print(' '.join(stuff[3:5]))

# thing = ['a', 'b', 'c', 'd']
#
# print(thing)

# create a mapping of state to abbreviation

# states = {
#     'Oregon': 'OR',
#     'Florida': 'FL',
#     'California': 'CA',
#     'New York': 'NY',
#     'Michigan': 'MI'
# }
#
# # create basic set of states and some cities in them
#
# cities = {
#     'CA': 'San Francisco',
#     'MI': 'Detroit',
#     'FL': 'Jacksonville'
# }
#
# # add some more cities
# cities['NY'] = 'New York'
# cities['OR'] = 'Portland'
#
# # print out some cities
# print('-' * 10)
# print("NY State has: ", cities['NY'])
# print("OR state has: ", cities['OR'])
#
# # print some states
#
# print('-' * 10)
# print("Michigan's abbreviation is ", states['Michigan'])
# print("Florida's abbreviation is ", states['Florida'])
#
# #  do it by using the state then cities dict
# print('-' * 10)
# print("Michigan has", cities[states['Michigan']])
# print("Florida has", cities[states['Florida']])
#
# # print every state abbreviation
# print('-' * 10)
# for state, abbrev in list(states.items()): # 首先将states 转换成可遍历元组数组 在后来转为列表元组 元祖的元素值不能修改 列表可以
#     # {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
#     # [('Google', 'www.google.com'), ('taobao', 'www.taobao.com'), ('Runoob', 'www.runoob.com')]
#     print(f"{state} is abbreviated {abbrev}")
#
# # print every city in state
# print('-' * 10)
# for abbrev,city in list(cities.items()):
#     print(f"{abbrev} has the city {city}")
#
#
# # now do both at the same time
# print('-' * 10)
# for state, abbrev in list(states.items()):
#     print(f"{state} state is abbreviated {abbrev}")
#     print(f"and has city {cities[abbrev]}")
#
# # safely get a abbreviation by state that might not be there 安全的get 方法
# state = states.get('Texas')
#
# if not state:
#     print("Sorry . no Texas.")
#
# # get a city with a default value
# city = cities.get('Tx', 'Does Not Exist')
# print(f"The city for the state 'Tx' is :{city}")

# class Song(object):
#
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)
#
#
# happy_bday = Song(["Happy birthday to you"])
#
# bulls_on_parade = Song(["happy"])
#
# happy_bday.sing_me_a_song()
#
# bulls_on_parade.sing_me_a_song()

