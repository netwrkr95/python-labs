#  Week 3 assignment B

score = raw_input("Enter score between 0.0 and 1.0:")
s = float(score)

# Score Grade
# Number out of range
if s >= 1.1:
 print 'Number Entered out of range.'

# = 1.0 A
elif s == 1.0:
 print 'A'
 
# >= 0.9 A
elif s > 0.9:
 print 'A'

# >= 0.8 B
elif s >= 0.8:
 print 'B'

# >= 0.7 C
elif s >= 0.7:
 print 'C'

# >= 0.6 D
elif s >= 0.6:
 print 'D'

# < 0.6 F
else:
 print 'F'
