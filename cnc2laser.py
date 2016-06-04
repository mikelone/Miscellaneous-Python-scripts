__author__ = 'mikelone'
'''
  this is the conversion for inkscapes cnc extensions
  it is to change

  first it will delete M3 and M5 from the files
  second it will place the M3 after penetration
  and place M5 before


'''

import Tkinter as tk
import tkFileDialog

myFormats = [
    ('cnc gcode', '*.nc'),
    ('Portable Network Graphics', '*.png'),
    ('JPEG / JFIF', '*.jpg')
]

root = tk.Tk()
root.withdraw()
file_path = tkFileDialog.askopenfilename(parent=root, filetypes=myFormats, title='Choose a file')
if file_path != None:
    print "%s" % file_path

    with open(file_path, mode='r') as nfile:
        data = nfile.read()
        # removes the M3 and M5
        data = data.replace('M3', '')  # replaces the laser on to newline
        data = data.replace('M5', '')  # replaces the laser off to newline
        # places a M3 after every (Penetrate)
        after_str = '(Penetrate)'  # addes the turn on function for the laser
        data = data.replace(after_str, after_str + '\nM3\n')
        before_str = '(End cutting path'  # addes before the turn off function for the laser
        data = data.replace(before_str, '\nM5\n' + before_str)
    nfile.close()

    print data

    with open(file_path, mode='w') as nfile:
        nfile.write(data)
    nfile.close()



