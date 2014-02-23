import subprocess
import sys
import re

command = ''

for cmd in sys.argv[1:]:
	command=command+' '+cmd

p = subprocess.Popen(command,shell=True, stderr=subprocess.PIPE)
out, err = p.communicate()
# write to the text file
file = open('errors.txt', 'w')
file.write(err)

# open the file and read it
file = open('errors.txt', 'r')
inputList = file.read().split()
#Add a bunch of 'junk patterns' here in which we will need to remove
pattern1  = re.compile ("\"\w+\.\w+\"") #This pattern should match file names
pattern2 = re.compile ("\w+\.\w+")

print "After Parsing"
for i in range(len(inputList)):
	if re.match(pattern1,inputList[i]):
		inputList[i] = ""
	elif re.match(pattern2,inputList[i]):
		inputList[i] = ""

for j in inputList:
	print j