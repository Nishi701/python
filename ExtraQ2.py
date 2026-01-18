print("Without Function")
n1=int(input("Enter num1:"))
n2=int(input("Enter num2:"))
res=n1+n2
print(f"Result addition is {res}")


print("With function and print value:")
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
def add():
    result=num1+num2
    print(f"Result addition is {result}")

if __name__ == "__main__":
    add()

add()


print("With function and return value:")
no1=int(input("Enter num1:"))
no2=int(input("Enter num2:"))
def funcReturn():
    return no1+no2


if __name__ == "__main__":
    print(funcReturn())


"""Without Function
Enter num1:11
Enter num2:22
Result addition is 33
With function and print value:
Enter num1:22
Enter num2:33
Result addition is 55
Result addition is 55
With function and return value:
Enter num1:44
Enter num2:55
99"""
