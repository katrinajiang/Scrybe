'''
	OOB.py v0.01
	"Overarching Organizational Backend"
	by Andy Wong
	1. Uses string input, sorts into individual characters (TODO: GUI Input)
	2. Determines which characters from the library to use.
	3. Strings characters together to form one G-Code file (TODO: G-CODE CONCATENATOR)
	4. Sends this G-Code file to correct location for G-Code sender
	5. G-Code sender streams to grbl.
'''
from shutil import copyfile
from stream_input import simple_streaming
import gcode_concatenator

directory0 = "C:\users\medecinqui\desktop\scryb\streaming"
directory1 = directory0 + "\stream_input"

write_string = "Go Bears! \n University of California, Berkeley"
gcode_concatenator.concatenate(write_string) #create entire g-code file
copyfile(directory0 + "grbl.gcode", directory1 + "grbl.gcode")
simple_streaming.run_stream() #have to turn python .main into .run_stream() effectively
