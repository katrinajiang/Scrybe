Given that I'm up this late, I sincerely doubt I'll wake up early tomorrow and go to the meeting in Soda at a reasonable time or at all. I'm sincerely sorry about that and also not making the friday meeting.

I'm writing this to discuss the software backend of our project, as it seems that's what I'm working on.

First of all, I've made a github repo for this project on https://github.com/medecinqui/Scryb. All the work I've done is in /streaming, as I am nominally working on the part of the project that streams g-code to grbl.

Second of all, it's time to discuss how we're actually going to send gcode files to grbl.

Originally, our idea was this: have a library of characters, in gcode. Using this library, we choose an arbitrary string and we write each character out by having a backend select the appropriate characters and sending it to grbl. This is simple enough that I could honestly do it right now (as long as the library was created and grbl was setup). HOWEVER, there's an issue.

We did not consider the necessary offset required to write one character after another one, like the "A" in "CAL" following "C". In order to do this in g-code, we have to have actual offsets included in the g-code - that is, we need to modify the g-code itself.

What we originally planned was:

Coordinates for characters --software-->> g-code for characters
g-code for characters + input string --backend-->> grbl

but now to do this we'd need to do:

Coordinates for characters --software-->> g-code for characters
g-code for characters + input string --software-->> WEIRD STEP
WEIRD STEP --backend-->> grbl

where WEIRD STEP means either a. take the first character's g-code, offset it by 0, take the second character's g-code, offset it by 1, take second one, offset it by 2, and so on OR b. put all characters together in one g-code file, each portion having appropriate offsets.

WEIRD STEP implies a requirement for a g-code parser. That is, we already turn coordinates into g-code via our own written software. WEIRD STEP requires something to turn g-code into something readable so that we can modify it and then return it to g-code again.

NOW, THIS SOUNDS TEDIOUS? IS THERE AN ALTERNATIVE?

Instead of having a g-code library, we can have a coordinates library (a lot of .csv files, maybe - it's easy to export those in matlab). Then, the backend takes in the string we want to write (e.g. "GO BEARS!") and it then chooses which coordinate files we want. It chooses these coordinates, adding an offset in x or y for later characters. Then, on the fly it transforms these coordinates to g-code (which shouldn't be very long - it's O(n) time, where n is the amount of coordinates there are total) [NOT REAL TIME - no time constraint]. Then, once the g-code is done, it sends this g-code to grbl.

Does this sound clear? Jose knows a bit of what I mean as I talked to him a little bit.

Conclusion:

I've handled the python streaming thing. It's easy peasy. We have to introduce an offset somewhere, and we might as well do it before we turn anything into g-code first, instead of having to edit g-code afterward.

Things still left to do in software:
A. configuring grbl so that it works with our 4 axis machine
B. complete library?
C. coordinates -> g-code
D. seperate coordinates/g-code to complete g-code for entire string
things if we have time, not that hard tbh
E. console window GUI -> slightly better GUI (python ezpz)
F. More than one line string? e.g. "Go Bears \n Yee boi"
