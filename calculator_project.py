def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
print("CHOOSE AN OPERATION: ")
print("1.Addition")
print("2.subtraction")
print("3.Multiplication")
print("4.Division")
choice=input("Enter an operations 1,2,3,4\n")
if choice in('1','2','3','4'):
    num1=float(input("Enter a first Number : "))
    num2=float(input("Enter the second number: "))
    if choice == '1' :
        print("Result: ",addition(num1,num2))
    elif choice == '2' :
       print("Result: ",subtraction(num1,num2))
    elif choice == '3':
        print("Result:",multiplication(num1,num2))
    elif choice == '4':
        print("Result: ",division(num1,num2))
else :
    print("Invalid choice ! please enter an valid operation")
          