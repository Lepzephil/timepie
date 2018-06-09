import tkinter

root = tkinter.Tk()

# 2 - placing buttons on the screen
# topFrame=tkinter.Frame(root)
# topFrame.pack()
# bottomFrame=tkinter.Frame(root)
# bottomFrame.pack(side="bottom")
#
# buttom1=tkinter.Button(topFrame, text="Yoga", bg="white")
# buttom2=tkinter.Button(topFrame, text="Meditation", bg="black")
# buttom3=tkinter.Button(topFrame, text="Prayer", bg="yellow")
# buttom4=tkinter.Button(topFrame, text="Nothing", bg="green")
#
# buttom1.pack(side="left")
# buttom2.pack(side="left")
# buttom3.pack(side="left")
# buttom4.pack(side="bottom")

# 3 - filling buttons on the screen
# one = tkinter.Label(root, text="one", fg="blue", bg="yellow")
# one.pack()
# two = tkinter.Label(root, text="two", fg="black", bg="blue")
# two.pack(fill="x")
# three = tkinter.Label(root, text="three", fg="purple", bg="green")
# three.pack(side="left", fill="y")


# 4 - placing lables entries in specific positions based on a grid
# lable_1 = tkinter.Label(root, text="Why don't you want to do yoga anymore?")
# entry_1 = tkinter.Entry(root)
#
# lable_1.grid(row=1,column=1)
# entry_1.grid(row=1,column=2)
#
# check_button = tkinter.Checkbutton(root, text="Save this entry.")
# check_button.grid(columnspan=2)


# 5 buttons that print test
# def print_text(text = "Yes I did"):
#     print(text)
#
# buttom_1 = tkinter.Button(root, text="Yoga", command=print_text)
# buttom_1.pack()


# 6 - my first a class

class add_time():

    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack()

        self.add_time = tkinter.Button(frame, text="I did yoga", command=self.add_time_unit)
        self.add_time.pack()

        self.quit_buttom = tkinter.Button(frame, text="Don't mother me today", command=frame.quit)
        self.quit_buttom.pack()


    def add_time_unit(self):
        print('Added one time unit!')

add_yoga_time = add_time(root)

root.mainloop()




