#__author__ = 'crhill'
# 7.1 Write a program that prompts for a file name,
# then opens that file and reads through the file,
# and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.
#
# You can download the sample data at http://www.pythonlearn.com/code/words.txt
#
# Use words.txt as the file name
fname = raw_input("Enter file name: ")
# fname = open('words.txt')
fh = open(fname)
# "read" is needed, as "fname" is only a pointer
# so "read" inputs the text file into memory
inp = fh.read()
# "strip" is removing the line characters and
# white space found in the document
for line in inp:
# remove the "white space" from the lines
 line = line.strip()
# print the output in all UPPER CASE
inpcap = inp.upper()
# print len(inp)
print inpcap[0:]
