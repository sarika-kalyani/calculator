print("Please select operation -\n" \
		"1. Add\n" \
		"2. Subtract\n" \
		"3. Multiply\n" \
		"4. Divide\n")
      
select = int(input("Select operations form 1, 2, 3, 4 :"))
      
n1 = int(input("Enter first number: "))
      
n2 = int(input("Enter second number: "))
      
if select == 1:
	print(n1+n2)

elif select == 2:
	print(n1-n2)

elif select == 3:
	print(n1*n2)

elif select == 4:
	print(n1/n2)
	
else:
	print("Invalid input")
