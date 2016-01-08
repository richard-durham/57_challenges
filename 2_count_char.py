#!/usr/bin/python

'''Excercises for Programmers
	57 Challenges to Develop your Coding Skills
	Excercise # 2

	Goal:
		prompt for input string
		display output that shows:
			the input string
			the number of characters in the string

	Constraints:
		use single output statement to construct the output
		use a built-in function of the language to count the number of characters

	Challenges:
		If user enters nothing, state that they must enter something
'''

attempt = 0

def get_string():
	if attempt == 0:
		request = "What is the input string? "
	else:
		request = "I can not continue without an input string. "
	string = raw_input(request)
	return string.strip()


def count_chars(string):
	return len(string)


def output(string, char_count):
	print string, "has", char_count, "characters."


while True:
	string = get_string()
	if len(string) == 0:
		attempt += 1
	else:
		output(string, count_chars(string))
		break
