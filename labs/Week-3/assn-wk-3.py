#  Week 3 assignment

hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = 10.50

# Basic hours 40 or less
if h <= 40:
 pay = h * rate
 print 'pay',pay
 
# Hours greater than 40
elif h > 40:
 base = 40 * rate
 OThr = (h - 40) * rate
 OT = (OThr * 1.5) + base
 print 'pay',OT