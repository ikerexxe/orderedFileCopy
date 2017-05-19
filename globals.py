'''
 ' globals.py
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
from threading import Semaphore

#Global variables
selectedOrigin = ""
selectedDestination = ""
selectedDefaultOrigin = ""
extension = ".txt"
copyThreadSemaphore = Semaphore(0)
stopThread = False
configurationFileName = ".config"
tokenEqual = " = "
tokenOrigin = "MainOrigin"
tokenDestination = "Destination"
tokenDefaultOrigin = "DefaultOrigin"
tokenExtension = "Extension"