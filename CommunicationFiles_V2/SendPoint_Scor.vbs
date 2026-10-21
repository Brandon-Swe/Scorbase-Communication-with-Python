' This changes the Command_Check variable that is observed by both Scorbase and Python to determine if a command is new or not
Function  SendPoint_Scor(fromScor, varX, varY, varZ, varRoll)
    Const ForReading = 1, ForWriting = 2, ForAppending = 8 ' use ForAppending to skip use of python program
    dim fso, f
    set fso = CreateObject("Scripting.FileSystemObject")
    ' the file path is from \Intelitek\OpenCIM\MICROCIM-DEMO\WS1 to the ASRS project path seen below
    set f = fso.OpenTextFile("..\..\..\Projects\Asrs2_36u\CommunicationFiles_V2\SendPoint_varTxt.vbs", ForWriting, true) 
    ' set f = fso.OpenTextFile("O:\CPP\WS1\ASRS-36x2\SendPoint_varTxt.vbs", ForAppending, true)     ' Direct lab file path

    f.Write "' This file will be used to send points back and forth between the simulation and Scorbase"
    f.WriteBlankLines 1
    f.Write "fromScor = " & fromScor    'for checking if the position is from scorbase or python (1 - from scorbase, 0 - from python, -1 - not applicable)
    f.WriteBlankLines 1
    f.Write "x = " & varX
    f.WriteBlankLines 1
    f.Write "y = " & varY
    f.WriteBlankLines 1
    f.Write "z = " & varZ
    f.WriteBlankLines 1
    f.Write "roll = " & varRoll
    
end Function