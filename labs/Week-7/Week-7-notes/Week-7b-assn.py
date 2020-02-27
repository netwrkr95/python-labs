# __author__ = 'crhill'
# 7.2 Write a program that prompts for a file name,
# then opens that file and reads through the file,
# looking for lines of the form:
#
# X-DSPAM-Confidence:    0.8475
#
# Count these lines and extract the floating point values from
# each of the lines and compute the average of those values and
# produce an output as shown below.
#
# You can download the sample
# data at http://www.pythonlearn.com/code/mbox-short.txt when
# you are testing below enter mbox-short.txt as the file name.
#
# for line in inp:
# line = line.strip()
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
# inp = fh.read()
count = 0
tot = 0
totf = float(tot)
for line in fh:
 line = line.strip()
 if not line.startswith("X-DSPAM-Confidence:") :
  continue
# print line
 count = count + 1
 x = line[19:27]
 ix = float(x)
 totf = totf + ix
# print ix
# print line [19:27]
# print count
# print totf
avg = totf / count
print "Average spam confidence: ",avg
print "Done"


#for line in fh:
# line = line.strip()
# if not line.startswith("X-DSPAM-Confidence:"):
#  count = count + 1
#  x = x + line[21:27]
#  continue
# print line
# print line[20:27]
# print count
# print x / count
# print "Done"
# print line
#print "Done"

