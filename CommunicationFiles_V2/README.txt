Goal: Using the lab code as a skeleton, an adaptation code will be written to accept commands from the analytics engine, or through the code manually. 
The analytics engine will also interact with Scorbase to make position adjustments before moving into pick up or place a pallet in any given circumstance.

Objectives:
- Integrate command receiver using device id's for command type - low priority
- Setup a General Routine to be used separate from the command receiver - done* (Not yet lab tested)
- formulate a subroutine to send coordinates to analytics engine for checking point and/or animation - done
- Implement a Scorbase adjustment sent in from the analytics engine after the coordinate check - done
- Integrate the RFID output into sent data to the analytics engine - (ryan is working on this)

Project Notes (for building):

- The skeleton code this is built off of is very picky on how you do things. 
Notes:	- only use subroutine (labels outside a subroutine break everything else)
	- will have to call the subroutine after the "automatically generated code" because any lines of code placed before the '$' are placed below them after saving and re-opening the program. This is for calls that are needed outside of the subroutines already given.

Project Notes (for User)

- General Routine utilizes a rotation of templates between places in the ASRS and the conveyor belt. They are set up so that when it finishes, no template should be out of order. The routine uses three levels each with an increasing number of template spot interactions (1st Interchange: 1 template spot and conveyer, 2nd Interchange: 2 template spots and the conveyor, 3rd Interchange: 3 template spots and conveyor). Note that these are just examples to show off the capabilities of the ASRSx2 and are in no way practical in actual future factory logic.

	- To utilize General Routine, don't forget to uncomment it 
	- If the autogen code still has the Initialization code, start after it, if it has movement code, delete the autogen code and run it (won't work otherwise)
		- The autogen code will appear again when re-loaded regardless of saving
	- Also I attached a picture describing the order of the 3 routines

- If you want to test with single command sets (i.e. using the autogen code): make sure you have the Open CIM Device Driver open (if not then window>OpenCIM Screen), then click the small folded landscape paper icon to open the UI (for ASRS partID is irrelevant, SourceID is device you start at (ASRS - 210, RFID - 12, or Conveyor - 1), source index is the cell number you start at (1-72 for ASRS, 1 for conveyor/RFID), Target Id and Target index are the end point devices and cell numbers respectively. Note does not matter. (also unless you are on the lab computer, the drop down menus likely don't provide the correct ids, so don't use them unless you are sure)
	- If you are getting "Illegal Sequence of operations" error, comment out any subroutine calls after the autogen code (right click the line and press command/remark) 

- Regarding the SendPoint and CheckPos subroutines, they are currently skipped (for testing other stuff) and can be utilized by commenting/deleting the labels at the end of each routine (along with the jump to them at the beginning)

- Keep everything in the same folder and place this CommunicationFiles_V2 folder into Intelitek>Projects>ASRS_36u since that is how they are based. They will be adapted later as understanding improves on how the lab file paths are set up.

- Auto generated code from pick-place command will not save with the rest of the document and will revert back to calling initalization when reopened (whether you save or not), so keep anything permanent out of the $ Remarks

- Command Receiver is still a work in progress and so you cannot currently send commands from the analytics engine

- Otherwise GLHF, I will update this folder as needed and try to keep this file up to date with new info.