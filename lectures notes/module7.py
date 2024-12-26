import tkinter
from tkinter import filedialog
import os
import platform, sys, subprocess

# to do: Menu
# to do: About
def file_select():
    filename = filedialog.askopenfilename(initialdir="/", title="Choose a file",
                                          filetypes=(('Text file', 'txt'),
                                                     ('All files', '*')))
    text['text'] = text['text'] + filename
    if platform.system() == "Windows":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

window = tkinter.Tk()
window.title('Проводник')
window.geometry('350x150')
window.configure(bg='yellow')
window.resizable(False, False)
text = tkinter.Label(window, text='File', height=3, width=45, background='pink')
text.grid(column=1, row=1)
button_select = tkinter.Button(window, width=20, height=3, text='Choose a file', 
                               background='pink', command=file_select)
button_select.grid(column=1, row=2)
window.mainloop()
# filename = '/home/ruslan/urbn/assignments/files/file1.txt'
# # os.system(filename)
# os.system('open %s' % filename)



