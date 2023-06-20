from tkinter import *
import random
from tkinter import messagebox


root = Tk()
root.title('Tile Matching Game')
root.geometry('450x460')

global winner, matches
winner = 0

#creates our matches
matches = [1,1,2,2,3,3,4,4,5,5,6,6]
#shuffle our matches
random.shuffle(matches)

#create button frame
my_frame = Frame(root)
my_frame.pack(pady=10)

#define some variables
count =0
answer_list = []
answer_dict = {}

#reset the game
def reset():
    global matches, winner
    winner = 0
    matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    random.shuffle(matches)
    my_label.config(text='')
    button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11]
    # loop yhrough buttons and change colors
    for button in button_list:
        button.config(text='', bg='SystemButtonFace', state='normal')


#create winner function
def win():
    my_label.config(text='congrats! you won!!!!')
    button_list=[b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]
    #loop yhrough buttons and change colors
    for button in button_list:
        button.config(bg='yellow')


#a function for clicking buttons
def button_click(b, number):
    global count, answer_dict, answer_list, winner

    if b['text']=='' and count<2:
        b['text'] = matches[number]
        #keeps track of tiles you have clicked
        answer_list.append(number)
        #keeps track of the integers usead
        answer_dict[b] = matches[number]
        #increment our counter
        count+=1
    #determine correct or not
    if len(answer_list) == 2:
        if matches[answer_list[0]] == matches[answer_list[1]]:
            my_label.config(text='MATCH')
            for key in answer_dict:
                key['state'] = 'disabled'
            count = 0
            answer_list = []
            answer_dict = {}
            winner+=1
            if winner == 6:
                win()
        else:
            #my_label.config(text='DOH!')
            count = 0
            answer_list = []
            #pop message
            messagebox.showinfo('Incorrect!', 'Incorrect')
            for key in answer_dict:
                key['text'] = ''
            answer_dict = {}



#define our buttons
b0 = Button(my_frame, text='', font=('Helvetica', 20), height = 3, width=6, command=lambda: button_click(b0, 0), relief='groove' )
b1 = Button(my_frame, text='', font=('Helvetica', 20), height = 3, width=6, command=lambda: button_click(b1, 1), relief='groove'  )
b2 = Button(my_frame, text='', font=('Helvetica', 20), height = 3, width=6, command=lambda: button_click(b2, 2), relief='groove' )
b3 = Button(my_frame, text='', font=('Helvetica', 20), height = 3, width=6, command=lambda: button_click(b3, 3), relief='groove')
b4 = Button(my_frame, text='', font=('Helvetica', 20), height = 3, width=6, command=lambda: button_click(b4, 4), relief='groove')
b5 = Button(my_frame, text='', font=('Helvetica', 20), height = 3, width=6, command=lambda: button_click(b5, 5), relief='groove')
b6 = Button(my_frame, text='', font=('Helvetica', 20), height = 3, width=6, command=lambda: button_click(b6, 6), relief='groove' )
b7 = Button(my_frame, text='', font=('Helvetica', 20), height = 3, width=6, command=lambda: button_click(b7, 7), relief='groove' )
b8 = Button(my_frame, text='', font=('Helvetica', 20), height = 3, width=6, command=lambda: button_click(b8, 8), relief='groove' )
b9 = Button(my_frame, text='', font=('Helvetica', 20), height = 3, width=6, command=lambda: button_click(b9, 9), relief='groove' )
b10 = Button(my_frame, text='', font=('Helvetica', 20), height = 3, width=6, command=lambda: button_click(b10, 10), relief='groove' )
b11 = Button(my_frame, text='', font=('Helvetica', 20), height = 3, width=6, command=lambda: button_click(b11, 11), relief='groove' )


#grid our buttons
b0.grid(row=0, column=0)
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=1, column=3)

b8.grid(row=2, column=0)
b9.grid(row=2, column=1)
b10.grid(row=2, column=2)
b11.grid(row=2, column=3)

my_label = Label(root, text='')
my_label.pack(pady=20)

# create a menu
my_menu = Menu(root)
root.config(menu=my_menu)

#craete options
option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Options', menu=option_menu)
option_menu.add_command(label='Reset Game', command = reset)
option_menu.add_separator()
option_menu.add_command(label='Exit Game', command = root.quit)

root.mainloop()