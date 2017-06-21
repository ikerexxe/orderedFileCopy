'''
 ' main.py
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
from mainGui import *
from fileManager import *
from usbDetection import *
import globals
import threading

def main():
	checkPaths()
	copyThread = threading.Thread(target = copyManager)
	copyThread.start()
	usbThread = threading.Thread(target = usbDetector)
	usbThread.start()
	root = Tk()
	mainWindow = mainGUI(root)
	root.mainloop()
	globals.stopThread = True
	globals.copyThreadSemaphore.release()
#Finished main

if __name__ == "__main__":
    main()