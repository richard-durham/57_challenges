#!/usr/bin/python

import Tkinter

window = Tkinter.Tk()
window.title("Challenge 2")

char_count = 0





entry = ent.get()

while True:
	def exit():
		sys.exit()

	instructions = Tkinter.Label(window, text="Enter your text below")
	ent = Tkinter.Entry(window)
	lbl1 = Tkinter.Label(window, text="Number of charaters")
	lbl2 = Tkinter.Label(window, text=char_count)
	button = Tkinter.Button(window, text="Close", command = exit)

	window.mainloop()

	if entry.strip() != 0:
		char_count = len(entry.strip())

	instructions.pack()
	ent.pack()
	lbl1.pack()
	lbl2.pack()
