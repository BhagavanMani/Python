# F:\Studies\Resume\CoverLetter.docx
#Files
#-------------------------------------***********************--------------------------------------------
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
import os
print(os.getcwd())
fstr = open('out.py','r')
# print(dir(fstr))
contents = fstr.read()
print(type(contents))
print("Contents in {} are {} and type {}".format(fstr.name, contents,type(contents)))

# fstr.close()
# print(fstr.name)
# fstr = open('out.txt', 'r')
# fstr.read()
# with open('out.txt', 'r') as fstream:
   # print("type of fstrem is {}".format(type(fstream)))
   # print(fstream.readline(), end ='')
   # print(fstream.readline(), end = '')
   # contents = fstream.readline()
   # print("Count {} and contents are {}".format(len(contents), contents))


   # Read lines one after the other
   # for line in fstream:
   #    print(line, end = " ")

   # Read everything at one shot
   # fstream.tell()
   # contents = fstream.read()
   # print("Read() {}".format(contents))
   # print("Current offset is {}".format(fstream.tell()))
   # fstream.seek(0)
   # print("Current offset after resetting is {}".format(fstream.tell()))

   # # print("Current offset is {}".fstream.tell)
   # cont_lines = fstream.readlines()
   # print("Readlines() {}".format(cont_lines))
 # read, readline, readlines
   # contents = fstream.read(10)
   # print(contents)
   # fstream.seek(0)
   # contents = fstream.read()
   # print("My contents are {}" .format(contents))
   # if 'Error' in contents:
   #    print("Yes")
   # else:
   #    print("No")
# 1. Read the entire text file
# 2. Read the file one line at a time using readline, for using fd
# 3. Read first n lines.
# 4. Read file line by line and append to list.
# 5. Print line count, word count, character count
# 6. Print longest words in a file, if there are multiple largest words print
# all of them
# 7. Create odd and even list, odd list should have contents of odd lines
# and even line should have content of even lines.

# Read from one file and write to another file
# Read from one file and write to two files
# Read odd lines file1, even lines to file 2
# concatenate lines from two files line by line add to 3rd file.
# -------------------------------------***********************--------------------------------------------






# import os
# print(dir(os))
# for i in dir(os):
#     print(i)

# currentdir=os.getcwd()
# print(os.getcwd())
#
# os.chdir('F:\Studies\Resume')
# print(os.getcwd())
#
# print(os.listdir())

# os.makedirs('F:\Studies\Resume\As_Demo1\os_Demo2\os_Demo3')
# print(os.listdir('F:\Studies\Resume'))
# os.removedirs('F:\Studies\Resume\os_Demo1\os_Demo2\os_Demo3')
# print(os.listdir('F:\Studies\Resume'))

# os.rename('F:\Studies\Resume\CoverLetter.docx','F:\Studies\Resume\CoverLetterOld.docx')
# print(os.listdir('F:\Studies\Resume'))

# print(os.stat('F:\Studies\Resume\CoverLetterOld.docx'))
# print(type(os.stat('F:\Studies\Resume\CoverLetterOld.docx')))
# print(os.stat('F:\Studies\Resume\CoverLetterOld.docx').st_size)
# print(os.stat('F:\Studies\Resume\CoverLetterOld.docx').st_mtime)

# from datetime import datetime
# ModTime=os.stat('F:\Studies\Resume\CoverLetterOld.docx').st_mtime
# print(datetime.fromtimestamp(ModTime))
#
# from datetime import date
# ModTime=os.stat('F:\Studies\Resume\CoverLetterOld.docx').st_mtime
# print(date.fromtimestamp(ModTime))

#
# for dirpath,dirname,filename in os.walk('F:\Studies\Resume'):
#     print('DirPath :',dirpath)
#     print('DirName:',dirname)
#     print('FilenName:',filename)

# print(os.environ.get


# file_path=os.path.join('F:\Studies\Resume','test.txt')
# # print(file_path)
# with open(file_path,'w') as fd:
#     fd.write('This is test file \n')
#     fd.write('This is second line \n')
#     fd.write('This is 3rd line')
# with open(file_path,'r') as f:
#     print(f.readlines(),end='  ')
