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
import time
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
	
	while globals.stopThread == False:
		globals.copyThreadSemaphore.acquire()
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
	fileExist = readConfiguration()
	
	if fileExist == False:
		setDefaultPaths()
#Finished checkPaths

def setDefaultPaths():
	osType = detectOS()
	username = detectUsername()
	
	if osType == "Windows":
		globals.selectedOrigin = "C:/Users/"
		globals.selectedOrigin += username+"/"
		globals.selectedDestination = "C:/Users/"
		globals.selectedDestination += username+"/"
		globals.selectedDefaultOrigin = "C:/Users/"
		globals.selectedDefaultOrigin += username+"/"
	elif osType == "Linux":
		globals.selectedOrigin = "/home/"
		globals.selectedOrigin += username+"/"
		globals.selectedDestination = "/home/"
		globals.selectedDestination += username+"/"
		globals.selectedDefaultOrigin = "/home/"
		globals.selectedDefaultOrigin += username+"/"
	else:
		print("Error: unknown os")
#Finished setDefaultPaths

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

def writeConfiguration():
	configurationFile = open(globals.configurationFileName, "w")
	
	configurationFile.write(globals.tokenOrigin+globals.tokenEqual+globals.selectedOrigin+"\n")
	configurationFile.write(globals.tokenDestination+globals.tokenEqual+globals.selectedDestination+"\n")
	configurationFile.write(globals.tokenDefaultOrigin+globals.tokenEqual+globals.selectedDefaultOrigin+"\n")
	configurationFile.write(globals.tokenExtension+globals.tokenEqual+globals.extension+"\n")
	
	configurationFile.close()
#Finished writeConfiguration

def readConfiguration():
	fileExist = os.path.isfile(globals.configurationFileName)
	
	if fileExist == True:
		configurationFile = open(globals.configurationFileName, "r")
		
		for line in configurationFile:
			searchText = re.compile(globals.tokenOrigin)
			textFound = searchText.search(line)
			if textFound != None:
				globals.selectedOrigin = line[len(globals.tokenOrigin)+3:-1]
			
			searchText = re.compile(globals.tokenDestination)
			textFound = searchText.search(line)
			if textFound != None:
				globals.selectedDestination = line[len(globals.tokenDestination)+3:-1]
			
			searchText = re.compile(globals.tokenDefaultOrigin)
			textFound = searchText.search(line)
			if textFound != None:
				globals.selectedDefaultOrigin = line[len(globals.tokenDefaultOrigin)+3:-1]
			
			searchText = re.compile(globals.tokenExtension)
			textFound = searchText.search(line)
			if textFound != None:
				globals.extension = line[len(globals.tokenExtension)+3:-1]
	
		configurationFile.close()
		print("readConfiguration selectedDefaultOrigin %s" % globals.selectedDefaultOrigin)
		print("readConfiguration extension %s" % globals.extension)
	
	return fileExist
#Finished readConfiguration
