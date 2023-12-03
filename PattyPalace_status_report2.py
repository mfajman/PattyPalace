Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Makayla Fajman
>>> #Project submission #2, what I have completed so far:
>>> from tkinter import *
>>> #make the second window
>>> def open_second():
	second_window = Toplevel(root)
	second_window.title("Choose Your Toppings!")
	second_window.geometry("400x300")
	second_window.configure(bg="skyblue")
	myLabel2 = Label(second_window, text="Please enter your toppings: ", bg="white", font=("Ariel", 10))
	myLabel2.grid(row=1, column=0)
	user_entry = Entry(second_window)
	user_entry.grid(row=1, column=1)
	myButton2 = Button(second_window, text="Close", command=second_window.destroy)
	myButton2.grid(row=4, column=4)
	myButton3 = Button(second_window, text="Go Back", command=second_window.destroy)
	myButton3.grid(row=10, column=0)

	
>>> root = Tk()
>>> #make the home page
>>> #PattyPalace
>>> #title, slogan, bg color, button
>>> root.title("Patty Palace")
''
>>> root.geometry("400x300")
''
>>> root.configure(bg="beige")
>>> myLabel1 = Label(root, text="Patty Palace: Every Bite is Royally Delicious!", bg="white", font=("Ariel", 10))
>>> myLabel1.grid(row=0, column=0)
>>> myButton1 = Button(root, text="Choose Toppings", command=open_second)
>>> myButton1.grid(row=1, column=1)
>>> root.mainloop()
