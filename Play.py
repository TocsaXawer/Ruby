import os 
from tkinter import * 
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer

root = Tk()

mixer.init()

menubar = Menu(root, bg="white")
root.config(menu=menubar)


def browse_file():
	global filename
	filename = filedialog.askopenfilename()


subMenu = Menu(menubar, bg="white", tearoff=0)
menubar.add_cascade(label="File", menu=subMenu, font=("manjari", 8, "bold"))
subMenu.add_command(label="Open", font=("manjari", 8, "bold"), command=browse_file)


root.configure(bg="white")
root.title("Play")

text = Label(root, text="Make a now world", bg="white")
text.configure(font=("manjari", 8, "bold"))
text.pack()


def play_btn():
	try:
		paused
	except NameError:
		try: 
			mixer.music.load(filename)
			mixer.music.play()
			statusbar["text"] = "Playing music" + " " + os.path.basename(filename)
		except:
			tkinter.messagebox.showerror(title="File not found", message="Sorry")
	else:
		mixer.music.unpause()
		statusbar["text"] = "Music resumed"


def stop_btn():
	global paused
	paused = True
	mixer.music.pause()
	statusbar["text"] = "Music pause"

def set_vol(val):
	volume = int(val)/100
	mixer.music.set_volume(volume)


middleframe = Frame(root, bg="white")
middleframe.pack()


playPhoto = PhotoImage(file="play.png")
PlayBtn = Button(middleframe, image=playPhoto, command=play_btn, bg="white")
PlayBtn.pack(side=LEFT)

stopPhoto = PhotoImage(file="pause.png")
stopBtn = Button(middleframe, image=stopPhoto, command=stop_btn, bg="white")
stopBtn.pack(side=LEFT)

scale = Scale(root, from_=0, to=100, bg="white", orient=HORIZONTAL, command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.pack()

statusbar = Label(root, text="Good Work", bg="white", relief=SUNKEN, anchor=W)
statusbar.configure(font=("manjari", 10, "italic"))
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
