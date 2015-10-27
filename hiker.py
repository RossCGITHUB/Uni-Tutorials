str = "This planet has - or rather had - a problem which was this: most of the people on it were unhappy for pretty much of the time. Many solutions were suggested for this problem, but most of these were largely concerned with the movements of small green pieces of paper, which is odd because on a whole it wasn't the SMALL green pieces of paper that were unhappy. The server login is username:server password:drowssap"

sub = "problem"
print str.count(sub)

str2 = str.lower()

sub = "small"
print str2.count(sub)

sub = "."
print str.count(sub) 


str3 = "."

int = str.find(str3, 30)

print "The first sentance is,"
print str[0:int]

str4 = "username"

str5 = str.find(str4)

print str5

print str[str5:str5+16]



str6 = "password"

str7 = str.find(str6)

print str[str7:str7+18]


