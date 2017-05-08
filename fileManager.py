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