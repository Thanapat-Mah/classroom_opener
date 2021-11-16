from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import webbrowser
from dummy_config import *

# open the provided link
def open(link):
	try:
		webbrowser.open(link, new=2)
	except:
		messagebox.showerror('Something wrong', 'Please try again later')

# format time from 10.5 to 10.30
def formatTime(time):
	hour = str(int(time//1))
	minute = str(int((time%1)*60))
	return(f'{hour}.{minute}')

# initiate GUI
gui = Tk()
gui.title('Link Opener')
gui.state('zoomed')
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()

# define properties of Frame for each day
hourHeight = 50
frameHeight = 600
dayWidth = 200
tmpColor = 'white'
tmpThick = 0.5
weekFrame = Frame(gui, width=dayWidth*7, height=frameHeight, highlightbackground = tmpColor, highlightthickness = tmpThick)
weekX = (screen_width-dayWidth*7)/2
weekY = (screen_height-frameHeight)/3
weekFrame.place(x=weekX, y=weekY)

weekdayFrameDict = {
	weekday: Frame(weekFrame, bg=weekdayColor[weekday], width=dayWidth, height=frameHeight,
	highlightbackground = tmpColor, highlightthickness = tmpThick)
	for weekday in weekdayColor.keys()
	}
# weekdayFrameDict = {
# 	'sunday': Frame(weekFrame, bg='tomato', width=dayWidth, height=frameHeight, highlightbackground = tmpColor, highlightthickness = tmpThick),
# 	'monday': Frame(weekFrame, bg='lightyellow', width=dayWidth, height=frameHeight, highlightbackground = tmpColor, highlightthickness = tmpThick),
# 	'tuesday': Frame(weekFrame, bg='lightpink', width=dayWidth, height=frameHeight, highlightbackground = tmpColor, highlightthickness = tmpThick),
# 	'wednesday': Frame(weekFrame, bg='lightgreen', width=dayWidth, height=frameHeight, highlightbackground = tmpColor, highlightthickness = tmpThick),
# 	'thursday': Frame(weekFrame, bg='orange', width=dayWidth, height=frameHeight, highlightbackground = tmpColor, highlightthickness = tmpThick),
# 	'friday': Frame(weekFrame, bg='lightblue', width=dayWidth, height=frameHeight, highlightbackground = tmpColor, highlightthickness = tmpThick),
# 	'saturday': Frame(weekFrame, bg='magenta', width=dayWidth, height=frameHeight, highlightbackground = tmpColor, highlightthickness = tmpThick)
# }

# generate weekday frame
dayX = 0
for day in weekdayFrameDict:
	color = weekdayColor[day]
	# weekday label
	Label(weekFrame, text=day, font=('Helvatical bold',20),
		bg=color, width=13, height=2, justify='center').place(x=dayX, y=0)
	weekdayFrameDict[day].place(x=dayX, y=70)
	dayX += dayWidth

# generate each classroom
for c in classroomList:
	# extract info
	code, name, day, startTime, endTime, link, comment = c.code, subjectDict[c.code], c.day, c.startTime, c.endTime, c.link, c.comment
	if comment != '':
		comment = f'({comment})'
	classHeight = (endTime-startTime)*hourHeight
	classY = (startTime-8.5)*hourHeight
	startTime = formatTime(startTime)
	endTime = formatTime(endTime)

	# generate UI
	classFrame = Frame(weekdayFrameDict[day], width=dayWidth, height=classHeight, highlightbackground = tmpColor, highlightthickness = tmpThick)
	ttk.Label(classFrame, text=f'{code} {name} {comment}', wraplength=200).place(x=0, y=0)
	ttk.Label(classFrame, text=f'Time: {startTime} - {endTime}').place(x=0, y=30)
	classFrame.place(x=0, y=classY)

	# classromm link
	ttk.Button(weekdayFrameDict[day], text='launch link',
		command= lambda link=link: open(link)).place(x=120, y=classY+classHeight-30)

# some specail class embeded in existing class
ttk.Button(weekdayFrameDict['tuesday'], text=specail_label,
		command= lambda: open(specail_link)
		).place(x=60, y=320)

gui.mainloop()