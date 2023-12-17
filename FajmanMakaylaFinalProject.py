Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Name: Makayla Fajman
>>> #Date: Dec 17, 2023
>>> #Final Project SDEV140
>>> from tkinter import *
>>> #create check box for toppings page
>>> #define checked_boxes and create global name
>>> #get user entry for name, set price per burger to 6, and get num of burgers
>>> def checked_boxes(second_window, var0, var1, var2, var3, var4):
	print(var0.get(), var1.get(), var2.get(), var3.get(), var4.get())
	global name
	name = user_entry.get()
	price_per_burger = 6
	num_burgers = int(num_burgers_entry.get())
#create empty list for toppings so each topping can be appended 
	toppings = []
	if var0.get() == 1:
		toppings.append("lettuce")
	if var1.get() == 1:
		toppings.append("Tomato")
	if var2.get() == 1:
		toppings.append("Onion")
	if var3.get() == 1:
		toppings.append("Bacon")
	if var4.get() == 1:
		toppings.append("Pickle")
	text = ', '.join(toppings)
	myLabel3 = Label(second_window, text=text, bg="white", font=("Arial", 12))
	myLabel3.grid(row=3, column=0)
	#return the toppings
	return toppings

>>> #define second window, make global for num_burgers
>>> def open_second():
	global num_burgers
	num_burgers_str = num_burgers_entry.get()
	#make error box if user types something wrong
	try:
		#attempt to convert the input to an integer
		num_burgers = int(num_burgers_str)
	except ValueError:
		#Handle the case where the input is not a valid integer
		messagebox.showerror("Error", "Please enter a valid number of burgers.")
		return
	#create second window title, geometry, etc.
	#make buttons for second window for submit and go back
	#add info for the checkbox on this page with checkButton
	second_window = Toplevel(root)
	var0 = IntVar()
	var1 = IntVar()
	var2 = IntVar()
	var3 = IntVar()
	var4 = IntVar()
	second_window.title("Choose Your Toppings!")
	second_window.geometry("400x300")
	second_window.configure(bg="skyblue")
	myLabel2 = Label(second_window, text="Please choose your toppings: ", bg="white", font=("Arial", 10))
	myLabel2.grid(row=1, column=0)
	myButton3 = Button(second_window, text="Go Back", command=second_window.destroy)
	myButton3.grid(row=12, column=0)
	checkButton = Checkbutton(second_window, text="Lettuce", variable=var0, onvalue=1, offvalue=0, bg="white", font=('Arial', 10))
	checkButton.grid(row=2, column=0)
	checkButton1 = Checkbutton(second_window, text="Tomato", variable=var1, onvalue=1, offvalue=0, bg="white", font=('Arial', 10))
	checkButton1.grid(row=3, column=0)
	checkButton2 = Checkbutton(second_window, text="Onion", variable=var2, onvalue=1, offvalue=0, bg="white", font=('Arial', 10))
	checkButton2.grid(row=4, column=0)
	checkButton3 = Checkbutton(second_window, text="Bacon", variable=var3, onvalue=1, offvalue=0, bg="white", font=('Arial', 10))
	checkButton3.grid(row=5, column=0)
	checkButton4 = Checkbutton(second_window, text="Pickle", variable=var4, onvalue=1, offvalue=0, bg="white", font=('Arial', 10))
	checkButton4.grid(row=6, column=0)
	myButton4 = Button(second_window, text="Submit", command=lambda: open_third(checked_boxes(second_window, var0, var1, var2, var3, var4)), bg="white", font=("Arial", 10))
	myButton4.grid(row=7, column=0)

	
>>> #define third window that comes from toppings page
>>> #add global num_burgers, and create labels
>>> #show that price per burger is $6
>>> #create the close button
>>> #show the price, wait time, and toppings
>>> #calculate the price_total
>>> def open_third(toppings):
	global num_burgers
	third_window = Toplevel(root)
	third_window.title("Price and wait time")
	third_window.geometry("400x300")
	third_window.configure(bg="beige")
	price_per_burger = 6
	price_total = num_burgers * price_per_burger
	myLabel7 = Label(third_window, text="{name}, your price comes to ${price}".format(name=name, price=price_total), bg="white", font=("Arial", 10))
	myLabel7.grid(row=0, column=0)
	myLabel9 = Label(third_window, text="Toppings: {}".format(', '.join(toppings)), bg="white", font=("Arial", 10))
	myLabel9.grid(row=1, column=0)
	myButton6 = Button(third_window, text="Close", command=third_window.destroy)
	myButton6.grid(row=4, column=0)
	myLabel8 = Label(third_window, text="Your burger(s) will be ready in 5-10 minutes. Thank you for ordering from Patty Palace!", bg="white", font=("Arial", 10))
	myLabel8.grid(row=2, column=0)

	
>>> #make home page
>>> #create buttons for home page, and create the logo
>>> #make name entry, amount of patties entry, and num of burgers entry
>>> root = Tk()
>>> root.title("Patty Palace")
''
>>> root.geometry("400x300")
''
>>> root.configure(bg="beige")
>>> myLabel1 = Label(root, text="Patty Palace: Where Every Bite is Royal Delicious!", bg="white", font=("Arial", 10))
>>> myLabel1.grid(row=0, column=0)
>>> myButton1 = Button(root, text="Choose Toppings", command=open_second)
>>> myButton1.grid(row=5, column=4)
>>> myLabel4 = Label(root, text="What is your name?: ", bg= "white", font=("Arial", 10))
>>> myLabel4.grid(row=2, column=0)
>>> user_entry = Entry(root)
>>> user_entry.grid(row=2, column=1)
>>> myLabel5 = Label(root, text="Would you like a double patty or only one?", bg="white", font=("Arial", 10))
>>> myLabel5.grid(row=3, column=0)
>>> num_burgers_entry = Entry(root)
>>> num_burgers_entry.grid(row=3, column=1)
>>> myLabel6 = Label(root, text="How many burgers would you like?", bg="white", font=("Arial", 10))
>>> myLabel6.grid(row=4, column=0)
>>> num_burgers_entry = Entry(root)
>>> num_burgers_entry.grid(row=4, column=1)
>>> #pull it all together
>>> root.mainloop()
1 0 1 0 1
1 1 1 1 1
