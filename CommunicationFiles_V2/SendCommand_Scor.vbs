' This changes the Command_Check variable that is observed by both Scorbase and Python to determine if a command is new or not
Function SendCommand_Scor(varCheck)
    Const ForReading = 1, ForWriting = 2
    dim fso, f
    set fso = CreateObject("Scripting.FileSystemObject")
    
    ' the file path is from \Intelitek\OpenCIM\MICROCIM-DEMO\WS1 to the ASRS project path seen below
    set f = fso.OpenTextFile("..\..\..\Projects\Asrs2_36u\CommunicationFiles_V2\SendCommand_varTxt.vbs", ForWriting, true)
    ' set f = fso.OpenTextFile("O:\CPP\WS1\ASRS-36x2\SendCommand_varTxt.vbs", ForWriting, true) ' Direct lab file path

    'for checking if the position is from scorbase or python (1 - from scorbase, 0 - from python, -1 - not applicable)
    f.Write "fromScor = " & varCheck
    
end Function