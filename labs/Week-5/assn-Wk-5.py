# 5.2 Write a program that repeatedly prompts a user for integer numbers
#  until the user enters 'done'. Once 'done' is entered,
# print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except
# and put out an appropriate message and ignore the number. Enter the numbers from
# the book for problem 5.1 and Match the desired output as shown.
#
# largest = None
# smallest = None
# while True:
#    num = raw_input("Enter a number: ")
#    if num == "done" : break
#    print num
#
# Week 5
largest = None
smallest = None
while True:
 num = raw_input("Enter a number:")
 if num == 'done':
  break

# For smaller value
 for value in [num]:
  if smallest is None:
   smallest = value
  elif value < smallest:
   smallest = value
# print smallest, value

# For largest value
# My "try/except" statement is as follows:
# If not all matches under "try", then JUMP to "except"
 try:
  num = int(num)
  for value in [num]:
   if largest is None:
    largest = value
   elif value > largest:
    largest = value
 except:
  print 'Invalid input'

print "Maximum is",largest
print "Minimum is",smallest
