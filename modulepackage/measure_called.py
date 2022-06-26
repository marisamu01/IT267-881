from secrets import choice
from tkinter.colorchooser import Chooser
from measure import Measure
if __name__== '__main__':
    mobj = Measure()

    choice = input('Choose menu (1: inch, 2cm): ')
    number = float(input('Enter number: '))

    if choice == '1':
        print(f'{number} cm = {mobj.cm_inch(number):.2f} inch')
    elif choice == '2':
        print(f'{number} inch = {mobj.cm_inch(number):.2f} inch')
    else:
        print('Choose wrong menu')
