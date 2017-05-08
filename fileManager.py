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
from shutil import copyfile

#Global variables
originPaths = []
destinationPaths = []
files = []
extension = ".txt"

def findFilesInPath(originPath, destinationPath):
	global originPaths
	global files
	global extension
	
	for tmpFile in os.listdir(originPath):
		if tmpFile.endswith(extension):
			originPaths.append(originPath)
			destinationPaths.append(destinationPath)
			files.append(tmpFile)
			print("Added file %s" % tmpFile)
#Finished findFilesInPath

def copyFile(originPath, destinationPath, file):
	copyfile(originPath+file, destinationPath+file)
	print("Copied '%s' from '%s' to '%s'" %(file, originPath, destinationPath))
#Finished copyFile

def main():
	global originPaths
	global destinationPaths
	global files
	cont = 0
	originPath = ""
	destinationPath = ""
	
	findFilesInPath(originPath, destinationPath)
	while(cont < len(originPaths)):
		copyFile(originPaths[cont], destinationPaths[cont], files[cont])
		cont += 1
	
	originPaths.pop(0)
	destinationPaths.pop(0)
	files.pop(0)
#Finished main

if __name__ == "__main__":
    main()