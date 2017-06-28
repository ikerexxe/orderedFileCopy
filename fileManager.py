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
import mainGui
from shutil import copyfile

#Global variables
originPaths = []
destinationPaths = []
files = []

def findFilesInPath(originPath, destinationPath):
	global originPaths
	global files
	filesToOrder = []
	
	for tmpFile in os.listdir(originPath):
		if tmpFile.endswith(globals.extension):
			filesToOrder.append(tmpFile)

	orderedFiles = orderFiles(filesToOrder)
	
	for tmpFile in orderedFiles:
		if tmpFile.endswith(globals.extension):
			originPaths.append(originPath)
			path = originPath.split(globals.selectedDefaultOrigin)[1]
			destinationPaths.append(destinationPath+path)
			files.append(tmpFile)
			globals.filesLeft += 1
			if globals.filesLeft > 0:
				globals.mainWindow.labelFilesLeft.configure(background="red")
			print("findFilesInPath: added file %s" % tmpFile)
	
	globals.windowFilesLeft.set("%d files left to copy" % globals.filesLeft)
#Finished findFilesInPath

def orderFiles(files):
	filters = [" ", "-", "_", "."]
	fileList = []
	
	print("orderFiles: files %s" % files)
	print("orderFiles: filters %s" % filters)
	
	for file in files:
		bestFilterPosition = 4
		
		for filter in filters:
			newFilterPosition = file.find(filter)
			
			if newFilterPosition > 0 and newFilterPosition < bestFilterPosition:
				bestFilterPosition = newFilterPosition
				
		if bestFilterPosition > 0 and bestFilterPosition < 4:
			fileList.append(int(file[:bestFilterPosition]))
				
	print("orderFiles: fileList %s" % fileList)
	orderedFiles = ordering(files, fileList)
	print("orderFiles: orderedFileList %s" % fileList)
	print("orderFiles: orderedFiles %s" % orderedFiles)
	
	return orderedFiles
#Finished orderFiles

def ordering(files, fileList):
	cont1 = 0
	cont2 = 0
	
	while(cont1 < (len(fileList) - 1)):
		cont2 = cont1 + 1
		while(cont2 < len(fileList)):
			if fileList[cont1] > fileList[cont2]:
				#Ordering file names
				tmpFileList = fileList[cont1]
				fileList[cont1] = fileList[cont2]
				fileList[cont2] = tmpFileList
				
				#Ordering files
				tmpFiles = files[cont1]
				files[cont1] = files[cont2]
				files[cont2] = tmpFiles
			cont2 += 1
		cont1 += 1
		
	return files
#Finished ordering

def copyFile(originPath, destinationPath, file):
	copyfile(originPath+file, destinationPath+file)
	print("copyFile: Copied '%s' from '%s' to '%s'" %(file, originPath, destinationPath))
#Finished copyFile

def createPath(destinationPath):
	folderExist = os.path.isdir(destinationPath)
	
	if folderExist == False:
		os.makedirs(destinationPath)
		print("createPath: path '%s' created" % destinationPath)
	else:
		print("createPath: path not created")
#Finished createPath

def copyManager():
	global originPaths
	global destinationPaths
	global files
	cont = 0
	
	while globals.stopThread == False:
		globals.copyThreadSemaphore.acquire()
		print("copyManager: number of files to copy %d" % len(originPaths))
		
		while(len(originPaths) > 0):
			createPath(destinationPaths[cont])
			copyFile(originPaths[cont], destinationPaths[cont], files[cont])
			originPaths.pop(cont)
			destinationPaths.pop(cont)
			files.pop(cont)
			globals.filesLeft -= 1
			if globals.filesLeft == 0:
				globals.mainWindow.labelFilesLeft.configure(background="green")
			globals.windowFilesLeft.set("%d files left to copy" % globals.filesLeft)
	
	print("copyManager finished copying files")
#Finished copyManager

def checkPaths():	
	fileExist = readConfiguration()
	
	if fileExist == False:
		setDefaultPaths()
	
	print("checkPaths: globals.selectedOrigin '%s'" % globals.selectedOrigin)
	print("checkPaths: globals.selectedDestination '%s'" % globals.selectedDestination)
	print("checkPaths: globals.selectedDefaultOrigin '%s'" % globals.selectedDefaultOrigin)
	print("checkPaths: globals.extension '%s'" % globals.extension)
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
		print("detectOS: unknown os")
	
	return osType
#Finished detectOS

def detectUsername():
	username = getpass.getuser()
	
	return username
#Finished detectUsername

def writeConfiguration():
	configurationFile = open(globals.configurationFileName, "w")
	
	configurationFile.write(globals.tokenOrigin+globals.tokenEqual+globals.selectedOrigin+"\n")
	configurationFile.write(globals.tokenDestination+globals.tokenEqual+globals.selectedDestination+"\n")
	configurationFile.write(globals.tokenDefaultOrigin+globals.tokenEqual+globals.selectedDefaultOrigin+"\n")
	configurationFile.write(globals.tokenExtension+globals.tokenEqual+globals.extension+"\n")
	configurationFile.write(globals.tokenUsbState+globals.tokenEqual+str(globals.selectedUsbState)+"\n")
	configurationFile.write(globals.tokenUsbName+globals.tokenEqual+globals.selectedUsbName+"\n")
	
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
			
			searchText = re.compile(globals.tokenUsbState)
			textFound = searchText.search(line)
			if textFound != None:
				globals.selectedUsbState = int(line[len(globals.tokenUsbState)+3:-1])
			
			searchText = re.compile(globals.tokenUsbName)
			textFound = searchText.search(line)
			if textFound != None:
				globals.selectedUsbName = line[len(globals.tokenUsbName)+3:-1]
				print("readConfiguration: selectedUsbName %s" % globals.selectedUsbName)
	
		configurationFile.close()
	
	return fileExist
#Finished readConfiguration
