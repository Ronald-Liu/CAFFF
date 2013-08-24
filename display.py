from Tkinter import *

root = Tk()
x = 1
callback = None
t = None

def refreshMain():
	global callback,root
	if not callback == None:
		callback()
	root.after(200, refreshMain)

def load(cb):
	global callback, root
	callback = cb
	root.after(30,refreshMain)
	root.can = Canvas(width=640,height=480,bg='grey')
	root.can.pack()
	root.mainloop()

def refresh(map, status):
	global root
	root.can.delete('all')
	v = root.can.create_text(30,30,text=status, fill='yellow',font=('verdana', 36))
	root.update()
	
def printv():
	global x
	refresh(None, str(x))
	x+=1

if __name__=="__main__":
	load(printv)