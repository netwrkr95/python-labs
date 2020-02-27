#__author__ = 'crhill'
#
#8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words
# using the split() function. The program should build a list
# of words. For each word on each line check to see if the word
# is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words
# in alphabetical order.
#
# Week 8a
#
#fname = raw_input("Enter file name: ")
#fh = open(fname)
#lst = list()
#for line in fh:
#print line.rstrip()
#
fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list(fh)
#print lst
#print lst
for line in lst:
 linestrip = line.rstrip()
 print linestrip.split()

# line = line.rstrip()
# spline = line.split()
# print spline
# if line.startswith():
#  print len(spline)
#  print spline

 #spline = lst.split()
#spline = fh.split()
# print spline

#for line in fh:
# print line.rstrip()
