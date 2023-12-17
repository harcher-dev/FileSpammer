# I AM NOT ACCOUNTABLE FOR THE IMPROPER USE OF THIS APPLICATION
# Please use responsibly & carefully!
# antivirus may stop the program in a worst case scenario but do not rely on it.

import tkinter as tk
import time
from random import randint

def makeFiles():
    amnt = amntVar.get()
    contents = textEntryVar.get()
    count = 0
    if not useLinearFileBool.get():
        count = int(time.mktime(time.localtime()))
        
    for i in range(amnt):
        if useLinearFileBool.get(): count += 1
        else: count += randint(1,15)
        
        fileName = str(count) + '.txt'
        
        with open(fileName, 'w') as file:
            file.write(str(contents))            
            
window = tk.Tk()
window.geometry("400x200")
window.title("File Spammer")
window.configure(bg = "#3A3A3A")

textEntryVar = tk.StringVar(value=" ")
amntVar = tk.IntVar(value = 1)
useLinearFileBool = tk.BooleanVar(value = True)

makeFilesBtn = tk.Button(
    window,
    text = "Create files",
    command = makeFiles
)

amntToMakeEntry = tk.Entry(
    window,
    textvariable = amntVar,
    width = 6,
    font=("Arial", 17)
)

textEntry = tk.Entry(
    window,
    textvariable = textEntryVar,
    width = 15,
    font=("Arial", 17)
)

amntLbl = tk.Label(
    window,
    text = "Amount:",
    font = ("Arial", 16),
    bg = "#3A3A3A",
    fg = "White"
)

textLbl = tk.Label(
    window,
    text = "Text to go in files:",
    font = ("Arial", 16),
    bg = "#3A3A3A",
    fg = "White"
)

DropDownLbl = tk.Label(
    window,
    text = "Use linear file naming system (normal)?\n 0 means no, 1 means yes",
    font = ("Arial", 10),
    bg = "#3A3A3A",
    fg = "White"
)

dropDown = tk.OptionMenu(
    window,
    variable=useLinearFileBool,
    value=False
)

amntToMakeEntry.place(anchor = 'nw', relx = 0.24, rely = 0.04)
amntLbl.place(anchor = 'nw', relx = 0.02, rely = 0.04)
makeFilesBtn.place(anchor = 'nw', relx = 0.02, rely = 0.44)
textEntry.place(anchor = 'nw', relx = 0.47, rely = 0.24)
textLbl.place(anchor = 'nw', relx = 0.02, rely = 0.24)
dropDown.place(anchor = 'nw', relx = 0.64, rely = 0.65)
DropDownLbl.place(anchor = 'nw', relx = 0.02, rely = 0.64)

window.mainloop()