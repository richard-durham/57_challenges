#!/usr/bin/python

'''Excercises for Programmers
	57 Challenges to Develop your Coding Skills
	Excercise # 1

	Create a program that prompts for your name
		and prints a greeting using your name

	Constraint: keep input, string concatination, and output seperate

	Challenges: 
		Write a new version of the program without variables

		Write a version that displays different greetings for different people
'''

def get_name():
	print "Hello, what is your name?"
	name = raw_input(':')
	return name


def hello_name(name):
	greeting = "Greetings, " + name + '!'
	print greeting, "\n"

# main program
hello_name(get_name())


# Challenge - same object but use NO variables
print "Now without variables!  :) \n"

print "Yo, what do they call you?", raw_input(':'), "?  Cool name, nice to meet you!"