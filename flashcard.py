from tkinter import *
from tkinter import colorchooser
from random import randint

root = Tk()
root.title("Cody's Flashcard App")
root.geometry("500x700")
root.iconbitmap('c:/guis/icon.ico')




#create func to determine if addition answer is correct
def add_correct(num1, num2):
	#calcuate the actual answer
	correct = num1 + num2

	#correct and incorrect message
	output_answer_correct = StringVar()
	output_answer_incorrect = StringVar()
	output_answer_correct.set("Correct")
	output_answer_incorrect.set("Incorrect")


	if int(addAnswer.get()) == correct:
		add_correct_label.config(text=output_answer_correct.get())

	else:
		add_correct_label.config(text=output_answer_incorrect.get())



#create math functions
def add():
	hideMenuFrames()
	addFrame.pack(fill="both", expand=1)
	#create two random numbers
	global num1
	global num2
	num1 = IntVar()
	num2 = IntVar()
	num1.set(randint(1,10))
	num2.set(randint(1,10))


	#put our rand numbers on screen
	addFlash = Label(addFrame, text=str(num1.get()) + " + " + str(num2.get()), font=("arial", 32))
	addFlash.pack(pady=10)

	#answer box
	global addAnswer
	addAnswer = Entry(addFrame)
	addAnswer.pack(pady=5)

	#answer button
	addButton = Button(addFrame, text="Answer", command=lambda: add_correct(num1.get(), num2.get()))
	addButton.pack(pady=5)

	#correct or incorrect message
	global add_correct_label
	add_correct_label = Label(addFrame, text="Enter Your Answer Above")
	add_correct_label.pack(pady=5)

def subtract():
	hideMenuFrames()
	subtractFrame.pack(fill="both", expand=1)


def multiply():
	hideMenuFrames()
	multiplyFrame.pack(fill="both", expand=1)


def divide():
	hideMenuFrames()
	divideFrame.pack(fill="both", expand=1)

#hide frame function
def hideMenuFrames():
	addFrame.pack_forget()
	subtractFrame.pack_forget()
	multiplyFrame.pack_forget()
	divideFrame.pack_forget()







#define main menu
myMenu = Menu(root)
root.config(menu=myMenu)

#create menu items
mathMenu = Menu(myMenu)
myMenu.add_cascade(label="MathCards", menu=mathMenu)
mathMenu.add_command(label="Add", command=add)
mathMenu.add_command(label="Subtract", command=subtract)
mathMenu.add_command(label="Multiply", command=multiply)
mathMenu.add_command(label="Divide", command=divide)
mathMenu.add_separator()
mathMenu.add_command(label="Exit", command=root.quit)

#create math frames
addFrame = Frame(root, width=400, height=400)
subtractFrame = Frame(root, width=400, height=400, bg="red")
multiplyFrame = Frame(root, width=400, height=400, bg="yellow")
divideFrame = Frame(root, width=400, height=400, bg="green")

root.mainloop()
