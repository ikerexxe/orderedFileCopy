'''
 ' configurationGui.py
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

#Imported modules
from Tkinter import *

class configurationGUI:
    def __init__(self, master):
		#Window title
		self.master = master
		master.title("Configuration menu")
		
		#Window position and size
		windowWidth = 330
		windowHeight = 100
		screenWidth = master.winfo_screenwidth()
		screenHeight = master.winfo_screenheight()
		print("screenWidth %d" % screenWidth)
		print("screenHeight %d" % screenHeight)
		windowWidthPosition = (screenWidth - windowWidth) / 2
		windowHeightPosition = ((screenHeight - windowHeight) / 2) - windowHeight
		print("windowWidthPosition %d" % windowWidthPosition)
		print("windowHeightPosition %d" % windowHeightPosition)
		master.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, windowWidthPosition, windowHeightPosition))
		
		#Default origin information
		self.textDefaultOriginPath = Text(master, height = 1, width = 30)
		self.textDefaultOriginPath.grid(row = 0, column = 0)
		self.textDefaultOriginPath.insert(END, "Path of origin")
		self.buttonDefaultOriginPath = Button(master, text = "...", command = self.something)
		self.buttonDefaultOriginPath.grid(row = 0, column = 1)
	#Finished __init__

    def something(self):
		print("Something")
	#Finished something
#Finished configurationGUI