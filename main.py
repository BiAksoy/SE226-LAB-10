from tkinter import *

root = Tk()
root.title("Bilal Aksoy")
root.geometry("500x450")


def read_txt():
    f = open("Marvel.txt", "r")
    data = f.read()
    my_text.delete(1.0, END)
    my_text.insert(END, data)
    f.close()


def calculateFreqs():
    my_text.delete(1.0, END)
    f = open("Marvel.txt", "r")
    x = f.read()
    my_dict = {}
    for i in x.split():
        my_dict[i] = my_dict.get(i, 0) + 1
    for key in my_dict:
        my_text.insert(END, str("{}: {}".format(key, my_dict[key])))
        my_text.insert(END, "\n")


my_text = Text(root, width=55, height=15)
my_text.pack(pady=20)

read_button = Button(root, text="READ", command=read_txt)
read_button.pack(pady=20)
calculate_button = Button(root, text="CALCULATE", command=calculateFreqs)
calculate_button.pack(pady=20)

root.mainloop()
