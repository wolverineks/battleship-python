userInput = raw_input("input: ")

try:
   val = int(userInput)
except ValueError:
   print("That's not an int!")