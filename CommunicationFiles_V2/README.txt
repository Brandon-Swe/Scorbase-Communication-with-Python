Long Term Goal: Using the lab code as a skeleton, an adaptation code will be written to accept commands for the robot from the analytics engine, or through the Scorbase code manually. 
Short Term Goal: The analytics engine will send commands to Scorbase to make position adjustments before moving into pick up (GET) or place (PUT) a template in any given circumstance.

Long term Objectives: 
- Integrate command receiver using device ids for command type - done 
- Setup a General Routine to be used separate from the command receiver - done
- Integrate the RFID output into sent data to the analytics engine - (ryan is working on this) 

Short term Objectives:
- formulate a subroutine to send coordinates to analytics engine for checking point and/or animation - done
- Implement a Scorbase adjustment sent in from the analytics engine after the coordinate check - done
- Lab check the position adjustment to ensure it is done safely and properly - (programmatic adjustment need be setup by Ryan, but more needs to be done to make sure all positions work ok)

Project Notes (for building):

- The skeleton code this is built off of is very picky on how you do things. 
Notes:	- only use subroutine (labels outside a subroutine break everything else)
	- will have to call the subroutine after the "automatically generated code" because any lines of code placed before the '$' are placed below them after saving and re-opening the program. This is for calls that are needed outside of the subroutines already given.

Project Notes (for User):

File Breakdown:

- ASRSx2-ScorbaseToPythonV2.PNT : This holds the defined position information
- ASRSx2-ScorbaseToPythonV2.SBP : This holds the code itself
- ASRSx2-ScorbaseToPythonV2.WS	: This holds the glue that brings it all together (You open this one when loading Scorbase)
- ExCommand.txt			: An example command to be copied and pasted into the vbs file for testing (does not interact with the code)
- General_routines.jpg		: A sketch of how the interchanges in the general routine operate
- points.txt			: A gathering place for all the points sent from scorbase (from both send and check subroutines)
- Project Notes and Objectives  : A bunch of scattered notes I made for myself when programing this system. View at your own risk.
- README.txt			: Documentation for how this communication is meant to work (i.e. what you're reading now)
- SendCommand_python.py		: For sending commands from python to scorbase (see documentation below for how to use it)
- SendCommand_Scor.vbs		: Scorbase uses this code to write to the SendCommand_varTxt.vbs file in order to tell python it is done running a command
- SendCommand_varTxt.vbs	: This holds the command information from python and an interaction variable for both sides to see
- SendPoint_Scor.vbs		: For sending a point from Scorbase to VBS (that will then get picked up by the pointChecker.py file)
- SendPoint_python.py		: In charge of taking points from Scorbase and sending back adjusted ones to Scorbase (currently only sends a random position back)
- SendPoint_varTxt.vbs		: Points taken from Scorbase to go to python and also the other way around too

Quick Definitions:

Template - they hold the product and are stored within the ASRS. The robot moves these around to be placed on the conveyor
Pallet - These are the placed on the conveyor belt to transport templates between workstations.
Work Station - Each robot in the factory is a work station. The ASRS is work station 1 as an example.
Interchange - The way I use it here is to say that the template is exchanging cells between other cells, including the conveyer's pallet, and each interchange is an iteration of this exchange (like someone moving from the front of the queue to the back of the queue and moving everyone forward)

Program User Guide:

- Digital Inputs: To utilize these, first show them through View>Dialog Bars>Digital Inputs. This will show a set of darkened green boxes, numbering 1-8. Clicking them now does not do anything, so for the ones you want to change, right click them and press "Force". The text should turn red, and you will be able to click it to toggle it on or off. As of now 3 are used: 1 - Command Receiver, 2 - General Routine, 3 - End the program

- General Routine utilizes a rotation of templates between places in the ASRS and the conveyor belt. They are set up so that when it finishes, no template should be out of order. The routine uses three levels each with an increasing number of template spot interactions (1st Interchange: 1 template spot and conveyer, 2nd Interchange: 2 template spots and the conveyor, 3rd Interchange: 3 template spots and conveyor). Note that these are just examples to show off the capabilities of the ASRSx2 and are in no way practical in actual future factory logic.

	- To utilize General Routine, enable digital input 2 while in the initialization loop (see above for how to use digital inputs)
		- Initialization loop occurs with the auto-generated code that comes with the INIT code on startup of the code
		- If it has pick and place command instead, re-open the code to use the initialization loop (it is ok to save if needed)
	- At the end of the routine, it will wait for the digital input 2 to be turned off, so make sure you do so. 
		- This is to prevent the robot from running this subroutine more than you want it to
	- This routine assumes the conveyor I/O port is empty with pallet ready (so keep it that way)
	- Also, I attached a picture describing the order of the 3 routines

- If you want to test with single command sets (i.e. using the pick and place command): make sure you have the Open CIM Device Driver open (if not then window>OpenCIM Screen), then click the small folded landscape paper icon to open the UI (for ASRS partID is irrelevant, SourceID is device you start at (ASRS - 210, RFID - 12, or Conveyor - 1), source index is the cell number you start at (1-72 for ASRS, 1 for conveyor/RFID), Target Id and Target index are the end point devices and cell numbers respectively. Note does not matter. (also, unless you are on the lab computer, the drop-down menus likely don't provide the correct ids, so don't use them unless you are sure)
	- If you are getting "Illegal Sequence of operations" error, comment out any subroutine calls after the pick and place code, outside of an existing subroutine. 	(right click the line and press command/remark)
	- If you want to go back to normal operations reopen the file and it should work as normal 

- The Command Receiver is available through the use of digital input 1 and the python file "Scorbase Command Sender" (see above for how to use digital inputs). To use it, start the Scorbase code and have it loop within the Command Receiver Subroutine (after digital input 1). Then edit the example command dictionary to whatever command you want it to do (see SendCommand_python.py for the key to set a command), and run the python code. Scorbase will then run the command and then return to the subroutine's loop. If you want to return to the initial subroutine, disable the digital input and it will return if it is looping.

- The position adjustment algorithm (SendPos and CheckPos subroutines) uses vbs to collect the current positions of the robot at those times and python stores them for animation use later. If the subroutine used was SendPoint, then this is all it will do, but if CheckPos was used, after sending the current position, the subroutine will loop waiting for a renewed set of coordinates from python to occur. After the new position is sent back to scorbase, scorbase will enact that position and move on through the rest of the get/put motion until another check is needed. 
	- make sure their labels "SKIPSEND" and "SKIPCHECK" are commented along with the jump to inside their subroutines (there is 1 in SendPos and 2 in CheckPos)
		- to comment/uncomment code, simply right click and click Command/Remark and an astrick will appear/disappear before the line of code signifying it being run
	- To use the check, go to the python file SendPoint_python.py and input a position into the point set at the end of the code (currently has position 499) and run the code while its is doing its check loop.
		- beware that not all positions work (this will require further research onto why)

- digital input 3 will end the code. Not sure if I will keep that one there or not in later versions

- Keep everything in the same folder and place this CommunicationFiles_V2 folder into Intelitek>Projects>ASRS_36u since that is how they are based. They will be adapted later as understanding improves with how the lab file paths are set up.

- Auto generated code from pick-place command will not save with the rest of the document and will revert to calling initialization when reopened (whether you save or not), so keep anything permanent out of the $ Remarks

- Otherwise GLHF, I will update this folder as needed and try to keep this file up to date with new info. Let me know if you have come across any errors I may have missed.