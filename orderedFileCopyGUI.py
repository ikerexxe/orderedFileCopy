'''
 ' orderedFileCopyGUI.py
 ' Author: Iker Pedrosa
 ' 
 ' License:
 ' This file is part of orderedFileCopy.
 ' 
 ' orderedFileCopy is free software: you can redistribute it and/or modify
 ' it under the terms of the GNU General Public License as published by
 ' the Free Software Foundation, either version 3 of the License, or
 ' (at your option) any later version.
 ' 
 ' orderedFileCopy is distributed in the hope that it will be useful,
 ' but WITHOUT ANY WARRANTY; without even the implied warranty of
 ' MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 ' GNU General Public License for more details.
 ' 
 ' You should have received a copy of the GNU General Public License
 ' along with orderedFileCopy.  If not, see <http://www.gnu.org/licenses/>.
 ' 
'''

from Tkinter import *

class orderedFileCopyGUI:
    def __init__(self, master):
		#Window title
		self.master = master
		master.title("Ordered file copy")
		
		#Windows position and size
		windowWidth = 330
		windowHeight = 150
		screenWidth = root.winfo_screenwidth()
		screenHeight = root.winfo_screenheight()
		print("screenWidth %d" % screenWidth)
		print("screenHeight %d" % screenHeight)
		windowWidthPosition = (screenWidth - windowWidth) / 2
		windowHeightPosition = ((screenHeight - windowHeight) / 2) - windowHeight
		print("windowWidthPosition %d" % windowWidthPosition)
		print("windowHeightPosition %d" % windowHeightPosition)
		root.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, windowWidthPosition, windowHeightPosition))
		
		#Origin information
		self.textOriginPath = Text(master, height = 1, width = 30)
		self.textOriginPath.grid(row = 0, column = 0)
		self.textOriginPath.insert(END, "Path of origin")
		self.buttonOriginPath = Button(master, text = "...", command = self.something)
		self.buttonOriginPath.grid(row = 0, column = 1)
		
		#Destination information
		self.textDestinationPath = Text(master, height = 1, width = 30)
		self.textDestinationPath.grid(row = 1, column = 0)
		self.textDestinationPath.insert(END, "Path of destination")
		self.buttonDestinationPath = Button(master, text = "...", command = self.something)
		self.buttonDestinationPath.grid(row = 1, column = 1)
		
		#Copies left information
		self.labelFilesLeft = Label(master, text = "0 files left to copy")
		self.labelFilesLeft.grid(row = 2)
		
		#Copy button
		self.buttonCopy = Button(master, text = "Copy", command = self.something)
		self.buttonCopy.grid(row = 3)
	#Finished __init__

    def something(self):
        print("Something")
	#Finished greet
#Finished orderedFileCopyGUI

root = Tk()
my_gui = orderedFileCopyGUI(root)
root.mainloop()