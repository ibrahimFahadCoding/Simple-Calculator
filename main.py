# main.py


print("Python Calculator")
print("Addition: +")
print("Subtraction: -")
print("Multiplication: *")
print("Division: /")
print("Modulus: %")
print("Factorial: !")
print("Exponent: ^")

yorn = "Y"

while yorn != "N":
  if yorn == "Y":
    add = 0
    subtract = 0
    multiply = 0
    divide = 0
    mod = 0
    fact = 1
    exp = 1
    
    def func():
      choice = input("Enter the Operation you want: ")
      if choice == "+":
          n1 = int(input("Number 1: "))
          n2 = int(input("Number 2: "))
          add = n1 + n2
          print("Result: " + str(add))
    
      if choice == "-":
          n1 = int(input("Number 1: "))
          n2 = int(input("Number 2: "))
          subtract = n1 - n2
          print("Result: " + str(subtract))
      if choice == "*":
          n1 = int(input("Number 1: "))
          n2 = int(input("Number 2: "))
          multiply = n1 * n2
          print("Result: " + str(multiply))
      if choice == "/":
          n1 = int(input("Number 1: "))
          n2 = int(input("Number 2: "))
          divide = n1//n2 
          print("Result: " + str(divide))
      if choice == "%":
          n1 = int(input("Number 1: "))
          n2 = int(input("Number 2: "))
          mod = n1 % n2
          print("Result: " + str(mod))
          
      if choice == "!":
          num = int(input("Enter a number: "))
          fact = 1
          for i in range(1,num + 1):
            fact *= i
          print("Result: " + str(fact))
        
      if choice == "^": 
          exp = 1
          num1 = int(input("Number 1: "))
          num2 = int(input("Number 2: "))
          for i in range(num2):
            exp *= num1
          print("Result: " + str(exp))
      yorn = input("Y/N to continue: ")
  if yorn == "Y":
    func()
  if yorn == "N":
    print()
    
      
      
      
