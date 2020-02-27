#__author__ = 'crhill'
#
# 10.2 Write a program to read through the mbox-short.txt and
# figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and
# then splitting the string a second time using a colon.
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below. Note that the autograder does not have support
# for the sorted() function.
#
# name = raw_input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)
#
name = raw_input("Enter file: ")
#if len(name) < 1 :
# name = "mbox.txt"
handle = open(name)

# The program looks for 'From ' lines
#  and takes the second word of those lines as the person who sent the mail.
counts = dict()
for line in handle:
# line = line.rstrip()
 if not line.startswith('From '):
  continue
# split file into single words, this this email#domain.com
 words = line.split()
 #print words[5]

# Do a double split
 timespl = words[5]
 pieces = timespl.split(':')
 x = pieces[0:1]
 #print x

# for word in words:
 for word in x:
  # This is the same as an IF ELSE statement.
  # this line takes a word, or a list in this case.   If it a NEW word,
  # it applies 0 to it, than
  # it increment 1 (cause of the + 1). If it already exists, it just
  # increments the counter.
  counts[word] = counts.get(word,0) + 1
  #print counts

# Create an empty List with list()
lst = list()
# leverage this sorted command for k, v in the dictionary "counts
# sort via "k" in the dictionary.  You need an additional command
# of "lst.sort(reverse = True) to sort on "k" value
for k, v in sorted(counts.items()):
 print k, v


