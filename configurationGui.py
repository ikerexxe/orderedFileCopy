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
from fileManager import *
import tkFileDialog
import globals

#Global variables

class configurationGUI:
	def __init__(self, master):
		master.grab_set()
		#The contrary is master.grab_release()
		
		#Window title
		self.master = master
		master.title("Configuration menu")
		
		#Window position and size
		windowWidth = 600
		windowHeight = 125
		screenWidth = master.winfo_screenwidth()
		screenHeight = master.winfo_screenheight()
		print("configurationGui: screenWidth %d" % screenWidth)
		print("configurationGui: screenHeight %d" % screenHeight)
		windowWidthPosition = (screenWidth - windowWidth) / 2
		windowHeightPosition = ((screenHeight - windowHeight) / 2) - windowHeight
		print("configurationGui: windowWidthPosition %d" % windowWidthPosition)
		print("configurationGui: windowHeightPosition %d" % windowHeightPosition)
		master.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, windowWidthPosition, windowHeightPosition))
		
		#Create layouts
		top_frame = Frame(master, width = 600, height = 50)
		centre_frame = Frame(master, width = 600, height = 50)
		bottom_frame = Frame(master, width = 600, height = 50)
		top_frame.grid(row = 0)
		centre_frame.grid(row = 1)
		bottom_frame.grid(row = 2)
		
		#Extension information
		self.labelExtension = Label(top_frame, height = 1, width = 30, text = "File extension to copy:")
		self.labelExtension.grid(row = 0, column = 0)
		self.textExtension = Text(top_frame, height = 1, width = 5)
		self.textExtension.grid(row = 0, column = 1)
		self.textExtension.insert(END, globals.extension)
		
		#Default origin information
		globals.windowDefaultOrigin = StringVar()
		globals.windowDefaultOrigin.set(globals.selectedDefaultOrigin)
		self.textDefaultOriginPath = Entry(centre_frame, width = 55, font = ("Helvetica", 11), textvariable = globals.windowDefaultOrigin)
		self.textDefaultOriginPath.grid(row = 1, column = 0)
		self.buttonDefaultOriginPath = Button(centre_frame, text = "...", command = self.defaultOriginFileChooser)
		self.buttonDefaultOriginPath.grid(row = 1, column = 1, padx = 10)
		
		#Buttons
		self.buttonAccept = Button(bottom_frame, text = "Accept", command = self.accept)
		self.buttonAccept.grid(row = 2, column = 0, padx = 25, pady = 20)
		self.buttonCancel = Button(bottom_frame, text = "Cancel", command = self.cancel)
		self.buttonCancel.grid(row = 2, column = 1, padx = 25, pady = 20)
	#Finished __init__

	def defaultOriginFileChooser(self):
		resultPath = tkFileDialog.askdirectory(initialdir = globals.selectedDefaultOrigin) + "/"
		if resultPath != "/" and resultPath != "":
			globals.selectedDefaultOrigin = resultPath.encode("utf-8")
			globals.windowDefaultOrigin.set(globals.selectedDefaultOrigin)
	#Finished originFileChooser
	
	def accept(self):
		globals.extension = self.textExtension.get("1.0", "end-1c")
		writeConfiguration()
		print("accept: globals.selectedDefaultOrigin '%s'" % globals.selectedDefaultOrigin)
		print("accept: globals.extension '%s'" % globals.extension)
		self.master.destroy()
	#Finished accept
	
	def cancel(self):
		self.master.destroy()
	#Finished cancel
#Finished configurationGUI
