'''
 ' mainGui.py
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
from configurationGui import *
from fileManager import *
import tkFileDialog

#Global variables
windowOrigin = ""
windowDestination = ""

class mainGUI:
	def __init__(self, master):
		global windowOrigin
		global windowDestination
		
		print("mainGUI selectedOrigin %s" % globals.selectedOrigin)
		
		windowOrigin = globals.selectedOrigin
		windowDestination = globals.selectedDestination
		
		#Window title
		self.master = master
		master.title("Ordered file copy")
		
		#Window menu
		mainMenu = Menu(master)
		master.config(menu = mainMenu)
		fileMenu = Menu(mainMenu)
		mainMenu.add_command(label = "Configuration", command = self.openConfiguration)
		
		#Window position and size
		windowWidth = 600
		windowHeight = 150
		screenWidth = self.master.winfo_screenwidth()
		screenHeight = self.master.winfo_screenheight()
		print("screenWidth %d" % screenWidth)
		print("screenHeight %d" % screenHeight)
		windowWidthPosition = (screenWidth - windowWidth) / 2
		windowHeightPosition = ((screenHeight - windowHeight) / 2) - windowHeight
		print("windowWidthPosition %d" % windowWidthPosition)
		print("windowHeightPosition %d" % windowHeightPosition)
		self.master.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, windowWidthPosition, windowHeightPosition))
		
		#Origin information
		self.textOriginPath = Text(master, height = 1, width = 57, font = ("Helvetica", 11))
		self.textOriginPath.grid(row = 0, column = 0)
		self.textOriginPath.insert(END, windowOrigin)
		self.buttonOriginPath = Button(master, text = "...", command = self.originFileChooser)
		self.buttonOriginPath.grid(row = 0, column = 1)
		
		#Destination information
		self.textDestinationPath = Text(master, height = 1, width = 57, font = ("Helvetica", 11))
		self.textDestinationPath.grid(row = 1, column = 0)
		self.textDestinationPath.insert(END, windowDestination)
		self.buttonDestinationPath = Button(master, text = "...", command = self.destinationFileChooser)
		self.buttonDestinationPath.grid(row = 1, column = 1)
		
		#Copies left information
		self.labelFilesLeft = Label(master, text = "0 files left to copy")
		self.labelFilesLeft.grid(row = 2)
		
		#Copy button
		self.buttonCopy = Button(master, text = "Copy", command = self.copyFiles)
		self.buttonCopy.grid(row = 3)
	#Finished __init__

	def openConfiguration(self):
		print("Opening configuration window")
		self.configuration = Toplevel(self.master)
		self.app = configurationGUI(self.configuration)
	#Finished openConfiguration

	def originFileChooser(self):
		global windowOrigin
		
		windowOrigin = tkFileDialog.askdirectory() + "/"
		if windowOrigin != "":
			self.textOriginPath.delete('1.0', END)
			self.textOriginPath.insert(END, windowOrigin)
			globals.selectedOrigin = windowOrigin
			print("selectedOrigin '%s'" % globals.selectedOrigin)
	#Finished originFileChooser
	
	def destinationFileChooser(self):
		global windowDestination
		
		windowDestination = tkFileDialog.askdirectory() + "/"
		if windowDestination != "":
			self.textDestinationPath.delete('1.0', END)
			self.textDestinationPath.insert(END, windowDestination)
			globals.selectedDestination = windowDestination
			print("selectedDestination '%s'" % globals.selectedDestination)
	#Finished originFileChooser
	
	def copyFiles(self):	
		findFilesInPath(globals.selectedOrigin, globals.selectedDestination)
		globals.copyThreadSemaphore.release()
	#Finished something
#Finished mainGUI