try: 
  a=float(input("enter first number:"))
  b=float(input("enter second number:"))

  print(f"Addition:{a+b}")
  print(f"Substraction:{a-b}")
except ValueError:
  print("please enter valid numbers.")
