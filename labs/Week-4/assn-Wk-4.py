#  From Class assignment
#
# def computepay(h,r):
#     return 42.37
#
# hrs = raw_input("Enter Hours:")
# p = computepay(10,20)
# print "Pay",p


# def computepay(h,r):
#    return 42.37
#
#hrs = raw_input("Enter Hours:")
#p = computepay(10,20)
#print "Pay",p

# Week 4 assignment

# function for base pay under 40 hrs
def computepay(h,r):
 pay = h * r
 return pay

# function for over 40 hours
def OT_computepay(h,r):
 pay = 40 * r
 OThr = (h - 40) * r
 OT = (OThr * 1.5) + pay
 return OT

hrs = raw_input("Enter Hours: ")
h = float(hrs)

rate = raw_input("Enter Pay Rate: ")
r = float(rate)
# rate = 10.50

# Basic hours 40 or less
if h <= 40:
 p = computepay(h,r)
 print 'pay',p
 
# Hours greater than 40
elif h > 40:
 OTime = OT_computepay(h,r)
 print OTime