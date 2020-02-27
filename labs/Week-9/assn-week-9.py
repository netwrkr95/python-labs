#__author__ = 'crhill'
#
#9.4 Write a program to read through the mbox-short.txt and figure out who has the
#  sent the greatest number of mail messages. The program looks for 'From ' lines
#  and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address
# to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary
# using a maximum loop to find the most prolific committer.
#
# Week 9 starter code
# name = raw_input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)
#
# figure out who sent the greatest number of emails.
name = raw_input("Enter file: ")
# if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)


#
# The program looks for 'From ' lines
#  and takes the second word of those lines as the person who sent the mail.
counts = dict()
for line in handle:
# line = line.rstrip()
 if not line.startswith('From '):
  continue
# split file into single words, this this email#domain.com
 words = line.split()
 print words[1]
# Now I need to Put the email back into a "list"
# so it looks like 'email@domain.com'
 email = words[1]
 pieces = email.split()
 print pieces

 #wordlist = list(networds)
 #print wordlis

# for word in words:
 for word in pieces:
  # This is the same as an IF ELSE statement.
  # this line takes a word, or a list in this case.   If it a NEW word,
  # it applies 0 to it, than
  # it increment 1 (cause of the + 1). If it already exists, it just
  # increments the counter.
  counts[word] = counts.get(word,0) + 1
# print counts

# The program creates a Python dictionary that maps the sender's mail address
# to a count of the number of times they appear in the file.

lgcount = None
lgword = None
# Note in the line below word and count are separated by a comma ( , )
# this takes into account the "key.value" pair in the dictionary
for word,count in counts.items():
# print word.count
 if lgcount is None or count  > lgcount:
  lgword = word
  lgcount = count
#
print lgword, lgcount




# print counts.keys(), counts.values()


# After the dictionary is produced, the program reads through the dictionary
# using a maximum loop to find the most prolific committer.



