#from tkinter import Tk, Label, Button, Entry
#class AppWindow:
#    def __init__(self, master):
#        self.master = master
#        #: :type: list of str
#        self.matrixInputFields = [];
#        master.title("A simple GUI")
#
#        self.label = Label(master, text="This is our first GUI!")
#        #self.label.pack()
#
#        self.greet_button = Button(master, text="+", bg="#FFCC00", command=self.getDataFromInput)
#        self.greet_button.grid(row = 0, column = 1)
#       # self.greet_button.pack()
#
#        self.close_button = Button(master, text="Close", command=master.quit)
#        #self.close_button.pack()
#        self.matrixInputField()
#
#    def greet(self):
#        print("Greetings!")
#
#    def matrixInputField(self):
#        for i in range(3):
#            self.matrixInputFields.append(Entry(self.master))
#            self.matrixInputFields[i].grid(row = 4, column = i)
#
#    def getDataFromInput(self):
#        sum = 0
#        for x in self.matrixInputFields:
#            input_value = x.get() 
#            if (input_value != ''):
#                sum += int(input_value)
#        print(sum)
#
#root = Tk()
#root.geometry("500x200")
#my_gui = AppWindow(root)
#root.mainloop()
