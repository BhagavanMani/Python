Hello world
hello india
Error: There is an error occured
Warning:
Info:
Debug:
"""File Operations.

open
Read the file with open (Explicit close is requried!)
Read the file with context manager
read,read(size) readlines, readline, returns empty string when it
finished reading.
Context Mgr: with open (<file>, <mode>) as fd
Read: read,read(<size>) readlines, readline, Iterate through fd
Current postion: tell(), Manipulate current position;seek()

Write into file
Modes:
``r''   Open text file for reading.  The stream is positioned at the
         beginning of the file.

 ``r+''  Open for reading and writing.  The stream is positioned at the
         beginning of the file.

 ``w''   Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.

 ``w+''  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.

 ``a''   Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.

 ``a+''  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.
"""
