# Scorbase Command Sender

# General goal: write to a vbs script the command details to be read by Scorbase. Will be similar ot the test code version, but sending different things. 

# Writing the following to vbs:
#   TASK_ID - for command tracking
#   PART_ID - not important here
#   SOURCE_DEVICE_ID - starting device (210 - ASRS, 12 - RFID scanner, 1 - Conveyor)
#   SOURCE_DEVICE_INDEX - starting cell (for conveyor and RFID, always 1; for ASRS, 1-72)
#   TARGET_DEVICE_ID - ending device (210 - ASRS, 12 - RFID scanner, 1 - Conveyor)
#   TARGET_DEVICE_INDEX - ending cell (for conveyor and RFID, always 1; for ASRS, 1-72)
#   PICK_AND_PLACE_NOTE - not important here


# Command dictionary (This defintion is for testing purpose; the actual dictionary will come from the analytics engine)
command = {
    "TASK_ID": 10000,
    "PART_ID": 0,
    "SOURCE_DEVICE_ID": 210,
    "SOURCE_DEVICE_INDEX": 20,
    "TARGET_DEVICE_ID": 210,
    "TARGET_DEVICE_INDEX": 30,
    "PICK_AND_PLACE_NOTE": 0
}

# Checking if the previous command has been run by Scorbase yet (fromScor = 1: means from scorbase, fromScor = 0: means not from scorbase)
with open("commandSend.vbs", "r") as cmdFin:

    fromScorSTR = "fromScor = "
    cmdFinRead = cmdFin.read()
    newCmdITR = cmdFinRead.find(fromScorSTR) + len(fromScorSTR)
    newCmd = int(cmdFinRead[newCmdITR])

overwrite = False       # For testing purporses, can overrite the command by switching this to true

if newCmd == 1 or overwrite:
    
    # The command dictionary is written to a VBS file that Scorbase can read
    with open("commandSend.vbs","w") as cmdSend:
        cmdSend.write("fromScor = " + str(0))
        cmdSend.write("\nTASK_ID = " + str(command["TASK_ID"]))
        cmdSend.write("\nPART_ID = " + str(command["PART_ID"]))
        cmdSend.write("\nSOURCE_DEVICE_ID = " + str(command["SOURCE_DEVICE_ID"]))
        cmdSend.write("\nSOURCE_DEVICE_INDEX = " + str(command["SOURCE_DEVICE_INDEX"]))
        cmdSend.write("\nTARGET_DEVICE_ID = " + str(command["TARGET_DEVICE_ID"]))
        cmdSend.write("\nTARGET_DEVICE_INDEX = " + str(command["TARGET_DEVICE_INDEX"]))
        cmdSend.write("\nPICK_AND_PLACE_NOTE = " + str(command["PICK_AND_PLACE_NOTE"]))
else:
    print("The previous command has not yet completed")