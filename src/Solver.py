from flask import Flask, request
import requests

server = Flask(__name__)

@server.route("/solve", methods=["POST"])
def Verify():	
	stack = []
	result = True
	
	# Get input from Body Request
	# 
	# Body content type: text/plain
	# 
	# Parse data to String
	inputLocal = str(request.data)
	# Remove unused caracters : d'<INPUT>'
	inputLocal = inputLocal[2:len(inputLocal)-1]	
	print('Local input : ' + inputLocal)

	if inputLocal == "":
		# Consume Input From Server API 
		# url:	('http://localhost:5000/input')
		inputServer = requests.get('http://localhost:5000/input')
		inputFinal = inputServer.text
		print('Server input : ' + inputFinal)
	else :	
		# Using Local Input
		inputFinal = inputLocal
	
	for c in inputFinal:
		if c in ['[', '(', '{']:
			# Insert Opening Char in Stack
			stack.append(c)
		elif len(stack)!=0:
			# Comparing the Closing Char with the Waiting Char 
			if ( c == ')' and stack[-1] == '(' ):
				# Remove Char from Stack
				stack.pop()
			elif ( c == '}' and stack[-1] == '{' ):
				# Remove Char from Stack
				stack.pop()
			elif ( c == ']' and stack[-1] == '[' ):
				# Remove Char from Stack
				stack.pop()
			else:
				# Invalid Closing Character
				result = False
				break
		else :
			# The Stack is empty And there are some Closing Character(s)
			result = False
			break
	if len(stack) != 0 :
		# There are some Opening Character(s) :	- at the end of Input
		# 										- not closed 			    
		result = False

	if result:
		print("RESULT : OK!")
		return "INPUT : "+ inputFinal + " -- RESULT : OK!"

	else :
		print("RESULT : BAD INPUT :(")
		return "INPUT : "+ inputFinal + " -- RESULT : BAD INPUT :("

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5001)

