import time
import re

print "Enter your credentials..."
usrid = raw_input("\nEnter userid ::  ")
if usrid == "":
	print "Sorry !! user id can not be blank\n"
	exit()

if re.match(r'\s',usrid):
	print "Alphabets only!! \nno white space character please !!\n"
	exit()
if re.match(r'\W',usrid):
	print " Alphabets only!! \nno special character please !!\n"
	exit()	
if re.match(r'\d',usrid):
	print "Sorry !! user id must contain alphabets only\n"
	exit()
upwd = raw_input("\nEnter password :: ")
if upwd == "":
	print "Sorry !! password can not be blank\n"
	exit()
if re.match(r'\s',upwd):
	print " numbers only !!\nno white space charater please !!\n"
	exit()
if re.match(r'\W',upwd):
	print " numbers only !!\nno special character please !!\n"
	exit()	
if re.match(r'\D',upwd):
	print "Sorry !! password must be numeric"
	exit()
#pattern = "^[0-9]+$"
pwd = 0
pwd = int(upwd)
print "\n\nPlease wait for while we verify the details....."
time.sleep(2)
if usrid == "abcde" and pwd == 1234:
	print "Valid user!! \nAccess granted!!"
else:
	print "Not a valid user"
	exit()