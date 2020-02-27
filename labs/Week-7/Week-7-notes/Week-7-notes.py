# __author__ = 'crhill'
# xfile = open('cpol.txt')
xfile = raw_input("Enter file name: ")
fh = open(xfile)
# add counter
count = 0
# inp = fh.read()
# the "for" "in" statement will print each line in the file = 'cpol.rtf'
for line in fh:
# count = count + 1
# remove white space with "rstrip()"
# print line[:20]
 line = line.rstrip()
 if not 'ACI' in line:
  continue
# if line.startswith('ACI') :
 count = count + 1
 print line
print count
# print "Line Count Total:",count
