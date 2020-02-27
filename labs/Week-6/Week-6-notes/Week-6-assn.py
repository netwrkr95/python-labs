#__author__ = 'crhill'
# text = "X-DSPAM-Confidence:    0.8475";

# Week 6 assignment
# 6.5 Write code using find() and string slicing (see section 6.10)
# to extract the number at the end of the line below.
# Convert the extracted value to a floating point number
#  and print it out.

text = "X-DSPAM-Confidence:    0.8475"
# leverage text.find to find the "starting" point of target
startpos = text.find('0')
# print startpos
#
# define the end point of the search, which is "5"
endpos = text.find('5')
# print endpos
#
# starting point is easy, but end position is:  end "NOT including the "5"
# so I added the "endpos + 1" to include the "5"
output = text[startpos:endpos+1]
outfloat = float(output)
# print output
# x = outfloat * 10.0:    I used this to test the "floating" conversion was working
# print x
# outfloat = float(output)
print outfloat
