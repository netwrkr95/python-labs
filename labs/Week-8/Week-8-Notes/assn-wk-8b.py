#__author__ = 'crhill'
#
#
#  8.5 Open the file mbox-short.txt and read it line by line. When you find a line that
# starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# You will parse the From line using split() and print out the second
# word in the line (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.
#
# Hint: make sure not to include the lines that start with 'From:'.
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt
#
#
# fname = raw_input("Enter file name: ")
# if len(fname) < 1 : fname = "mbox-short.txt"
#
# fh = open(fname)
# count = 0
#
# print "There were", count, "lines in the file with From as the first word"
#
fname = raw_input("Enter file name: ")
#if len(fname) < 1 : fname = "mbox.txt"

fh = open(fname)
count = 0
# Loop:  strip white noise, and if line does NOT start with "From ", ignore it
for line in fh:
 line = line.rstrip()
 if not line.startswith('From '):
  continue
# split file into single words
 words = line.split()
 count = count + 1
# count each of the words
# print words
# print the word at the **2nd* spot, indicated by "1", as the email address
 print words[1]
# print it
print "There were", count, "lines in the file with From as the first word"