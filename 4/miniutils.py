import ast
version = "a1.0.0-minimod-1"

def miniInput(inputType: type = str, *prompt: str, errorMessage: str = "You must enter a{n} {type}"):
	"""
	An input function that you always wished python had as default
	PARAMETERS:
	inputType: must be a type, determines the required type of the input. Use str to allow all input
	prompt: determines the prompt that is passed to input. Please note that "\\n>>> " will be added onto the end of the prompt
	errorMessage: the error message that will be given if the input is not of the required type. Defaults to "You must enter a{n} {type}". {Type} is replaced with the required type and {n} is replaced with the "n" if the type starts with a vowel (for use in a/an, for example).
	"""
	while True:
		inputToCheck = input(" ".join(prompt)+"\n>>> ")
		try:
			if inputToCheck:
				inputToCheck = ast.literal_eval(inputToCheck)
				return inputType(inputToCheck)
			else:
				print("You need to enter something")
		except ValueError:
			n = ""
			if inputType.__name__[0] in ["a", "e", "i", "o", "u"]:
				n = "n"
			print(errorMessage.replace("{type}", inputType.__name__).replace("{n}", n))

print("Using MiniUtils version "+version+" by Minion3665")
print("Please don't remove these credits")
print("Writing your own name doesn't make you a coder")
