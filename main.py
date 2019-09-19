from displayStockInformation import showEarnings
from displayStockInformation import showDividends
from displayStockInformation import showWeeklyEarnings
from tkinter import *

# Testing functions
#showEarnings( 'APPL')
#showDividends( 'APPL')

# Creating a blank window 'root'
root = Tk()
root.title( 'Getting your day started right ٩(- ̮̮̃-̃)۶')
dividendDates = Button( root, text = 'Dividend Dates', width = 25, command = lambda: showDividends( 'AAPL'))
earningsDates = Button( root, text = 'Earnings Dates', width = 25, command = lambda: showEarnings( 'AAPL'))
dividendDates.pack()
root.mainloop()


'''
topHeader = Label( root, text = 'Cup of Stonks', bg = 'black', fg = 'white')
topFrame = Frame( root)
bottomFrame = Frame( root)

topHeader.pack( fill = X)
topFrame.pack()
bottomFrame.pack( side = BOTTOM)

button1 = Button( topFrame, text = 'Morning News', fg = 'red')
button2 = Button( topFrame, text = 'Change News List', fg = 'blue')
button3 = Button( bottomFrame, text = 'Earnings Dates')
button4 = Button( bottomFrame, text = 'Dividend Dates')
button1.pack( side = LEFT)
button2.pack( side = LEFT)
button3.pack( side = LEFT)
button4.pack( side = LEFT)
root.mainloop()

label = Label( root, text = 'Company Symbol')
# Positions the text in label in the window 'root'
label.pack()
# Window on the screen continuously until prompted to close
root.mainloop()
'''
