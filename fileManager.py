'''
 ' fileManager.py
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
import os
import platform
import re
import getpass
import globals
from shutil import copyfile

#Global variables
originPaths = []
destinationPaths = []
files = []

def findFilesInPath(originPath, destinationPath):
	global originPaths
	global files
	
	for tmpFile in os.listdir(originPath):
		if tmpFile.endswith(globals.extension):
			originPaths.append(originPath)
			path = originPath.split(globals.selectedDefaultOrigin)[1]
			destinationPaths.append(destinationPath+path)
			files.append(tmpFile)
			print("Added file %s" % tmpFile)
#Finished findFilesInPath

def copyFile(originPath, destinationPath, file):
	copyfile(originPath+file, destinationPath+file)
	print("Copied '%s' from '%s' to '%s'" %(file, originPath, destinationPath))
#Finished copyFile

def createPath(destinationPath):
	folderExist = os.path.isdir(destinationPath)
	
	if folderExist == False:
		os.makedirs(destinationPath)
		print("Path '%s' created" % destinationPath)
	else:
		print("Path '%s' not created" % destinationPath)
#Finished createPath

def copyManager():
	global originPaths
	global destinationPaths
	global files
	cont = 0
	
	print("copyManager, number of files to copy %d" % len(originPaths))
	
	while(len(originPaths) > 0):
		createPath(destinationPaths[cont])
		copyFile(originPaths[cont], destinationPaths[cont], files[cont])
		originPaths.pop(cont)
		destinationPaths.pop(cont)
		files.pop(cont)
	
	print("copyManager finished copying files")
#Finished copyManager

def checkPaths():
	osType = detectOS()
	username = detectUsername()
	
	if osType == "Windows":
		globals.selectedOrigin = "C:/Users/"
		globals.selectedOrigin += username
		globals.selectedOrigin += "/Desktop/interesante/Scripts/zzzzOrigin/"
		globals.selectedDestination = "C:/Users/"
		globals.selectedDestination += username
		globals.selectedDestination += "/Desktop/interesante/Scripts/zzzzzDestination/"
		globals.selectedDefaultOrigin = "C:/Users/"
		globals.selectedDefaultOrigin += username
		globals.selectedDefaultOrigin += "/Desktop/interesante/Scripts/"
	elif osType == "Linux":
		globals.selectedOrigin = "/home/"
		globals.selectedOrigin += username
		globals.selectedOrigin += "/Escritorio/orderedFileCopy/zzzzOrigin/"
		globals.selectedDestination = "/home/"
		globals.selectedDestination += username
		globals.selectedDestination += "/Escritorio/orderedFileCopy/zzzzzDestination/"
		globals.selectedDefaultOrigin = "/home/"
		globals.selectedDefaultOrigin += username
		globals.selectedDefaultOrigin += "/Escritorio/orderedFileCopy/"
	else:
		print("Error: unknown os")
#Finished checkPaths

def detectOS():
	osraw = platform.platform()
	print("Raw OS type: %s" % osraw)
	
	searchText = re.compile("Windows")
	osIsWindow = searchText.search(osraw)
	searchText = re.compile("Linux")
	osIsLinux = searchText.search(osraw)
	
	if osIsWindow != None:
		osType = "Windows"
	elif osIsLinux != None:
		osType = "Linux"
	else:
		osType = "Unknown"
		print("Unknown os")
	
	print("OS type %s" %osType)
	return osType
#Finished detectOS

def detectUsername():
	username = getpass.getuser()
	print("Username: %s" % username)
	
	return username
#Finished detectUsername
