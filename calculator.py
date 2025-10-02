while True:
  num1 = input("Please enter the first number (or 'quit' to exit): ")

  if num1 == "quit":
    break

  num2 = input("Please enter the second number: ")
  operator = input("Please enter an operator (+, -, *, /): ")

  # Converting inputs to numbers
  num1 = int(num1)
  num2 = int(num2)

  try:
    if operator == "+":
      print("Result: ", num1 + num2)
    elif operator == "-":
      print("Result: ", num1 - num2)
    elif operator == "*":
      print("Result: ", num1 * num2)
    elif operator == "/":
      print("Result: ", num1 / num2)
    else:
      print("Unknown operator. Try again.")
  except ZeroDivisionError:
    print("You can't divide by zero")
