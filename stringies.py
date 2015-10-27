str = "This is a string example....wow!!!"

print str.capitalize() 		#simply capitalizes the first letter

sub = "i"

print str.count(sub, 4, 40)	#this should print out 2 as i appears twice( between 4 and 40)

sub = "wow"

print str.count(sub)		#this should only output 1 as wow appears once


print len(str) #prints out the length of the string

print str.upper() #converts to uppercase
print str.lower() #converts to lowercase

str2 = "exam"

print str.find(str2)
print str.find(str2, 10)
print str.find(str2, 40)