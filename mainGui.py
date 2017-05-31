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

class mainGUI:
	labelFilesLeft = ""
	
	def __init__(self, master):
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
		print("mainGui init: screenWidth %d" % screenWidth)
		print("mainGui init: screenHeight %d" % screenHeight)
		windowWidthPosition = (screenWidth - windowWidth) / 2
		windowHeightPosition = ((screenHeight - windowHeight) / 2) - windowHeight
		print("mainGui init: windowWidthPosition %d" % windowWidthPosition)
		print("mainGui init: windowHeightPosition %d" % windowHeightPosition)
		self.master.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, windowWidthPosition, windowHeightPosition))
		
		#Origin information
		globals.windowOrigin = StringVar()
		globals.windowOrigin.set(globals.selectedOrigin)
		self.textOriginPath = Entry(master, width = 57, font = ("Helvetica", 11), textvariable = globals.windowOrigin)
		self.textOriginPath.grid(row = 0, column = 0)
		self.buttonOriginPath = Button(master, text = "...", command = self.originFileChooser)
		self.buttonOriginPath.grid(row = 0, column = 1)
		
		#Destination information
		globals.windowDestination = StringVar()
		globals.windowDestination.set(globals.selectedDestination)
		self.textDestinationPath = Entry(master, width = 57, font = ("Helvetica", 11), textvariable = globals.windowDestination)
		self.textDestinationPath.grid(row = 1, column = 0)
		self.buttonDestinationPath = Button(master, text = "...", command = self.destinationFileChooser)
		self.buttonDestinationPath.grid(row = 1, column = 1)
		
		#Copies left information
		globals.windowFilesLeft = StringVar()
		globals.windowFilesLeft.set("%d files left to copy" % globals.filesLeft)
		self.labelFilesLeft = Label(master, textvariable = globals.windowFilesLeft)
		self.labelFilesLeft.grid(row = 2)
		
		#Copy button
		self.buttonCopy = Button(master, text = "Copy", command = self.copyFiles)
		self.buttonCopy.grid(row = 3)
	#Finished __init__

	def openConfiguration(self):
		self.configuration = Toplevel(self.master)
		self.app = configurationGUI(self.configuration)
	#Finished openConfiguration

	def originFileChooser(self):
		resultPath = tkFileDialog.askdirectory(initialdir = globals.selectedOrigin) + "/"
		if resultPath != "/" and resultPath != "":
			globals.selectedOrigin = resultPath.encode("utf-8")
			globals.windowOrigin.set(globals.selectedOrigin)
	#Finished originFileChooser
	
	def destinationFileChooser(self):
		resultPath = tkFileDialog.askdirectory(initialdir = globals.selectedDestination) + "/"
		if resultPath != "/" and resultPath != "":
			globals.selectedDestination = resultPath.encode("utf-8")
			globals.windowDestination.set(globals.selectedDestination)
	#Finished destinationFileChooser
	
	def copyFiles(self):
		writeConfiguration()
		findFilesInPath(globals.selectedOrigin, globals.selectedDestination)
		globals.copyThreadSemaphore.release()
	#Finished copyFiles
#Finished mainGUI
