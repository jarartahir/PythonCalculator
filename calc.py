from tkinter import *
from tkinter import ttk
import statistics

class Calculator:
    def __init__(self):
        self.inputValue = ""
        self.numRow = 0
        self.numcol = 0
        self.buttonttext = 0
        self.root = Tk()
        self.root.geometry("420x420")
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()

        self.equation = StringVar()

        # create the text entry box for
        # showing the expression .
        expression_field = Entry(self.root, textvariable=self.equation)

        # grid method is used for placing
        # the widgets at respective positions
        # in table like structure .
        expression_field.grid(columnspan=5, ipadx=100)

        self.GUI()
        self.root.mainloop()

    def GUI(self):
        for i in range(0, 25):

            if (i % 5 == 0):
                self.numRow += 1
                self.numcol = 0

            self.numGenerator(self.numRow, self.numcol)
            self.charactesAndSymbolsGenerator(self.numRow, self.numcol)
            self.specialFunctionsButton(self.numRow, self.numcol)
            self.numcol += 1

    def buttonGenerator(self, text, col, row, mode=""):
        if mode == "special":
            ttk.Button(self.frm, text=text, command=lambda: self.specialFunction(text)).grid(column=col, row=row)
        else:
            ttk.Button(self.frm, text=text, command=lambda: self.showData(text)).grid(column=col, row=row)

    def charactesAndSymbolsGenerator(self, numrow, numcol):
        if numcol == 3:
            if numrow == 2:
                self.buttonGenerator("/", numcol, numrow)
            elif self.numRow == 3:
                self.buttonGenerator("x", numcol, numrow)
            elif self.numRow == 4:
                self.buttonGenerator("-", numcol, numrow)
            elif self.numRow == 5:
                self.buttonGenerator("+", numcol, numrow)

        if numrow == 5 and numcol == 1:
            self.buttonGenerator(".", numcol, numrow)
        elif numrow == 5 and numcol == 2:
            self.buttonGenerator("=", numcol, numrow)
        elif numrow == 1 and numcol == 0:
            self.buttonGenerator("AC", numcol, numrow)
        elif numrow == 1 and numcol == 1:
            self.buttonGenerator(",", numcol, numrow)
        elif (numrow == 1 and numcol > 0) or (numrow > 1 and numcol ==4):
            self.buttonGenerator("", numcol, numrow)


    def numGenerator(self, numrow, numcol):
        if numrow != 1 and numcol < 3:
            self.buttonttext += 1
            if self.buttonttext == 10: self.buttonttext = 0

            self.buttonGenerator(self.buttonttext, numcol, numrow)

    def showData(self, buttonPress):
        try:
            dataInString = str(buttonPress)
            if dataInString == "x": dataInString = "*"
            if (dataInString == "=" and self.inputValue != ""):
                total = str(eval(self.inputValue))
                self.equation.set(total)
            elif dataInString == "AC":
                self.equation.set("")
                self.inputValue = ""
            elif dataInString != "=":
                self.inputValue = self.inputValue + dataInString
                self.equation.set(self.inputValue)
        except:
            self.equation.set("error")

    def specialFunctionsButton(self, row, col):
        if row == 1 and col ==2:
            self.buttonGenerator("Mean", col, row, "special")
        elif row == 1 and col ==3:
            self.buttonGenerator("Median", col, row, "special")
        elif row == 1 and col ==4:
            self.buttonGenerator("Mode", col, row, "special")
        elif row == 2 and col == 4:
            self.buttonGenerator("SD", col, row, "special")

    def specialFunction(self,text):
        try:
            data = list(map(int, self.inputValue.split(",")))
            result:any()
            if text == "Mean": result = statistics.mean(data)
            elif text == "Median": result = statistics.median(data)
            elif text == "Mode": result = statistics.mode(data)
            elif text == "SD": result = statistics.stdev(data)
            self.equation.set(result)
        except:
            self.equation.set("error")
