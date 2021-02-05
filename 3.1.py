hrs = float(input("Enter Hours:"))
rate = float(input("Enter the Rate:"))
r = float(rate)
if hrs <= 40:
 	print( hrs  * r)
elif hrs > 40:
	print(40* r + (hrs-40)*1.5*r)
