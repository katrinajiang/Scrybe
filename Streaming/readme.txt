This section of the repo covers the part of software that pulls characters to draw from the library and sends it to grbl. It covers how we're streaming individual character's G-Code to the G-Code sender. This G-Code sender streams the G-Code to grbl.

**Files:

stream_input/simple_stream.py
  G-Code sender officially supported by grbl. Sends file named "grbl.gcode" in local directory to grbl via serial.
  requires pyserial (https://github.com/pyserial/pyserial/tree/master/serial)
OOB.py
  The backend that is coordinating simple_stream with individual characters from the library.
gcode_concatenator.py
  Combines g-code for characters into g-code for a string.
