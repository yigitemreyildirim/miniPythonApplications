def calculationSec(first,second,opS):
	opList = ["+","-","*","/"]
	
	if opS not in opList:
		return "please select operation (+)(-)(*)(/)"

	if opS == "+":
		return f"{first} {opS} {second} = {first+second}"

	if opS == "-":
		return f"{first} {opS} {second} = {first-second}"

	if opS == "*":
		return f"{first} {opS} {second} = {first*second}"

	if opS == "/":
		if second == 0:
			return "can not divide by zero"
		return f"{first} {opS} {second} = {first/second}"



while True:
    try:
        firstNumber = int(input("Please type the first number: "))
        secondNumber = int(input("Please type the second number: "))
    except ValueError:
        print("Please enter valid numbers")
        continue

    opSelection = input("Please select operation (+)(-)(*)(/): ")

    print(calculationSec(firstNumber, secondNumber, opSelection))
