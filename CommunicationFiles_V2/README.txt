Goal: Using the lab code as a skeleton, an adaptation code will be written to accept commands from the analytics engine, or through the code manually. 
The analytics engine will also interact with Scorbase to make position adjustments before moving into pick up or place a pallet in any given circumstance.

Short term Objectives:
- Integrate command receiver using device id's for command type - done
- Setup a General Routine to be used separate from the command receiver - done* (Not yet lab tested)
- formulate a subroutine to send coordinates to analytics engine for checking point and/or animation - done
- Implement a Scorbase adjustment sent in from the analytics engine after the coordinate check - done
- Integrate the RFID output into sent data to the analytics engine - (ryan is working on this)

Project Notes (for building):

- The skeleton code this is built off of is very picky on how you do things. 
Notes:	- only use subroutine (labels outside a subroutine break everything else)
	- will have to call the subroutine after the "automatically generated code" because any lines of code placed before the '$' are placed below them after saving and re-opening the program. This is for calls that are needed outside of the subroutines already given.

Project Notes (for User):

File Breakdown:

- ASRSx2-ScorbaseToPythonV2.PNT : This holds the defined position information
- ASRSx2-ScorbaseToPythonV2.SBP : This holds the code itself
- ASRSx2-ScorbaseToPythonV2.WS	: This holds the glue that brings it all together (You open this one when loading Scorbase)
- commandSend.vbs				: This holds the command information from python and an interaction variable for both sides to see
- General_routines.jpg			: A sketch of how the interchanges in the general routine operate
- New_Command.vbs				: Scorbase uses this code to write to the commandSend.vbs file in order to tell python it is done running a command
- NewPoint.vbs					: Points taken from Scorbase to go to python and also the other way around too
- pointChecker.py				: In charge of taking points from Scorbase and sending back adjusted ones to Scorbase (currently only sends a random position back)
- Project Notes and Objectives  : A bunch of scattered notes I made for myself when programing this system. View at your own risk.
- README.txt					: Documentaion for how this communication is meant to work (i.e. what your reading now)
- Scorbase Command Sender.py	: For sending commands from python to scorbase (see documentation below for how to use it)
- SendPoint.vbs					: For sending a point from Scorbase to vbs (that will then get picked up by the pointChecker.py file)


- Digital Inputs: To utilize these, first show them through View>Dialog Bars>Digital Inputs. This will show a set of darkened green boxes numbering 1-8. Clicking them now does not do anything (may do something if in lab), so for the ones you want to change, right click them and press "Force". The text should turn red and you will be able to click it to toggle it on or off. As of now 3 are used: 1 - Command Receiver, 2 - General Routine, 3 - End the program

- General Routine utilizes a rotation of templates between places in the ASRS and the conveyor belt. They are set up so that when it finishes, no template should be out of order. The routine uses three levels each with an increasing number of template spot interactions (1st Interchange: 1 template spot and conveyer, 2nd Interchange: 2 template spots and the conveyor, 3rd Interchange: 3 template spots and conveyor). Note that these are just examples to show off the capabilities of the ASRSx2 and are in no way practical in actual future factory logic.

	- To utilize General Routine, enable digital input 2 (see above for how to use digital inputs) 
	- At the end of the routine, it will wait for the digital input 2 to be turned off, so make sure you do so. 
		- This is to prevent the robot from running this subroutine more than you want it to
	- This routine assumes the conveyor I/O port is empty with pallet ready (so keep it that way)
	- If the autogen code still has the Initialization code, start after it, if it has movement code, delete the autogen code and run it (won't work otherwise)
		- The autogen code will appear again when re-loaded regardless of saving
	- Also I attached a picture describing the order of the 3 routines

- If you want to test with single command sets (i.e. using the autogen code): make sure you have the Open CIM Device Driver open (if not then window>OpenCIM Screen), then click the small folded landscape paper icon to open the UI (for ASRS partID is irrelevant, SourceID is device you start at (ASRS - 210, RFID - 12, or Conveyor - 1), source index is the cell number you start at (1-72 for ASRS, 1 for conveyor/RFID), Target Id and Target index are the end point devices and cell numbers respectively. Note does not matter. (also unless you are on the lab computer, the drop down menus likely don't provide the correct ids, so don't use them unless you are sure)
	- If you are getting "Illegal Sequence of operations" error, comment out any subroutine calls after the autogen code (right click the line and press command/remark)
	- If you want to go back to normal operations reopen the file and it should work as normal 

- The Command Receiver is available through the use of digital input 1 and the python file "Scorbase Command Sender" (see above for how to use digital inputs). To use it, start the Scorbase code and have it loop within the Command Receiver Subroutine. Then edit the stand in command dictionary to whatever command you want it to do (see the relevant python code for the key to set a command), and run the python code. Scorbase will then run the command and then return to the subroutine's loop. If you want to return to the initial subroutine, disable the digital input and it will return if it is looping.

- digital input 3 will end the code. Not sure if I will keep that one there or not in later versions

- Regarding the SendPoint and CheckPos subroutines, they are currently skipped (for testing other stuff) and can be utilized by commenting/deleting the labels at the end of each routine (along with the jump to them at the beginning)

- Keep everything in the same folder and place this CommunicationFiles_V2 folder into Intelitek>Projects>ASRS_36u since that is how they are based. They will be adapted later as understanding improves on how the lab file paths are set up.

- Auto generated code from pick-place command will not save with the rest of the document and will revert back to calling initialization when reopened (whether you save or not), so keep anything permanent out of the $ Remarks

- Otherwise GLHF, I will update this folder as needed and try to keep this file up to date with new info. Let me know if you come across any errors I may have missed.
