mystr ="Harry is a good boy"
# print(mystr[5]) this will print the 'k'
print(len(mystr))
print(mystr[0:19]) # it will start from 0 and 5 will be excluded here and will print the elements from 0 to 4 but note we have to write [0:5].

print(mystr[0:5:2]) # esme mera 1 char skip ho kr ayega

print(mystr[0:]) # pura hi print hoga 
print(mystr[:5]) 
# agr hum start ka kahli chode to vo 0 lelega and agr hum last ka empty chode to vo full length ko lega !!! 

print(mystr[::]) # same as : mystr[0:19:1]
 # agr 3rd parameter  ko bhi empty rakhe to vo usko 1 manta hai by default !! 

print(mystr[::3]) 

""" negative indexes """
