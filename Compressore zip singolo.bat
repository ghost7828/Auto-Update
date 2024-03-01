@echo off
SET "sourcedir=C:\Users\name\Desktop\YOUR FOLDER INPUT" 
SET "destdir=C:\Users\NAME\Desktop\YOUR FOLDE OUTPUT" 

FOR %%G IN ("%sourcedir%\*.*") DO (
    IF NOT "%%~xG"=="" (
        "C:\Program Files\7-Zip\7z.exe" a -tzip "%destdir%\%%~nG.zip" "%%G"
    )
)

FOR /D %%D IN ("%sourcedir%\*") DO (
    "C:\Program Files\7-Zip\7z.exe" a -tzip "%destdir%\%%~nD.zip" "%%D\"
)

echo Compression complete.

