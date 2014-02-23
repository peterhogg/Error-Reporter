#
# This is a helper script for our program
# - it takes in a list of compiler errors
# - passes these errors through the search function
# - opens the browser displaying possible solutions to those compiler errors
#
import urllib
import json
import sys
import webbrowser

# 
# This function takes in the list as an arguement and runs a search query 
# The top 5 results from the search query are displayed in new windows
#
def search(search):

	for i in search:

		#encode each element in the list
		encoded = urllib.quote(i)

		# append the encoded string into the ajax api quer link
		rawData = urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q='+encoded).read()

		# load the raw json data
		jsonData = json.loads(rawData)
		
		# pull information from the responseData and results array
		results = jsonData['responseData']['results']

		# open the links in the browser
		for er in results:		
			link = er['url']
			webbrowser.open(link)

# this list will contain the compiler errors 
argList = [
			"AttributeError: \'tuple\' object has no attribute \'rstrip\'",  
		    "SyntaxError: invalid syntax" 
		  ]

# iterate through the list
# read each element and find all the apostrophes 
# replace all (') to a (\') to escape the character
for i in argList:
	i.replace("'","\\'")

# Pass each element in the list to the function search
search(argList)
