Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c mim_start.bat"
oShell.Run strArgs, 0, false