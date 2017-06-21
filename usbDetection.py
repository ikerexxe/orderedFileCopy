'''
 ' usbDetection.py
 ' Author: m.wasowski and Iker Pedrosa
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
import re
import time
import globals
from glob import glob
from subprocess import check_output, CalledProcessError

#Global variables
sleepTime = 3

def get_usb_devices():
	sdb_devices = map(os.path.realpath, glob('/sys/block/sd*'))
	usb_devices = (dev for dev in sdb_devices if 'usb' in dev.split('/')[5])
	return dict((os.path.basename(dev), dev) for dev in usb_devices)
#Finished get_usb_devices

def get_mount_points(devices = None):
	devices = devices or get_usb_devices()
	output = check_output(['mount']).splitlines()
	is_usb = lambda path: any(dev in path for dev in devices)
	usb_info = (line for line in output if is_usb(line.split()[0]))
	return [(info.split()[0], info.split()[2]) for info in usb_info]
#Finished get_mount_points

def usbDetector():
	while globals.stopThread == False:
		if globals.selectedUsbState == 1:
			mountPoints = get_mount_points()
			print("usbDetector: mountPoints found %s" % mountPoints)

			for point in mountPoints:
				searchText = re.compile(globals.selectedUsbName)
				usbFound = searchText.search(point[1])

				if usbFound != None and globals.selectedDestination != point[1]:
					print("usbDetector: Found  mount point in %s" % point[1])
					globals.selectedDestination = point[1]
					globals.windowDestination.set(globals.selectedDestination)
		
		time.sleep(sleepTime)
#Finished usbDetector