import subprocess
import sys
import re
import os
# import the search.py script
import search

command = ''

for cmd in sys.argv[1:]:
	command=command+' '+cmd

p = subprocess.Popen(command,shell=True, stderr=subprocess.PIPE)
out, err = p.communicate()
# write to the text file
file = open('errors.txt', 'w')
file.write(err)
file.close()

# open the file and read it
file = open('errors.txt', 'r')
inputList = file.readlines()
file.close()
#Add a bunch of 'junk patterns' here in which we will need to remove
pattern1  = re.compile ("\"\w+\.\w+\"") #This pattern should match file names
pattern2 = re.compile ("\w+\.\w+")
pattern3 = re.compile ("\w+Error: \w+")

print "After Parsing"
#for i in range(len(inputList)):
#	if re.match(pattern1,inputList[i]):
#		inputList[i] = ""
#	elif re.match(pattern2,inputList[i]):b
#		inputList[i] = ""
for i in range(len(inputList)):
	
	if re.match(pattern3,inputList[i]):

	else:
		inputList[i]=""
os.remove("errors.txt")
file = open('errors.txt', 'w')
for j in inputList:
	file.write(j)
file.close()



# main function
if __name__ == '__main__':

	# creat a list with each line as an element of the list
	file = open("errors.txt","r")
	argList = file.readlines()
	file.close()


	# print the list


	# iterate through the list
	# read each element and find all the apostrophes
	# replace all (') to a (\') to escape the character
	for i in argList:
		i.replace("'","\\'")
	# Pass each element in the list to the function search
	search.search(argList)

# delete the error txt file
os.remove("errors.txt")


