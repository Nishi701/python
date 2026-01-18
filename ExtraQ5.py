# 1) Without function
# 2) Using function and return values
# 3) Using function and return result in list


print("----- WITHOUT FUNCTION -----")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)

if b != 0:
    print("Division =", a / b)
else:
    print("Division not possible")


print("\n----- USING FUNCTION WITH RETURN -----")

def calculate(x, y):
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y if y != 0 else "Not possible"
    return add, sub, mul, div

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

r = calculate(x, y)

print("Addition =", r[0])
print("Subtraction =", r[1])
print("Multiplication =", r[2])
print("Division =", r[3])


print("\n----- USING FUNCTION RETURNING LIST -----")

def operations_list(p, q):
    result = []
    result.append(p + q)
    result.append(p - q)
    result.append(p * q)

    if q != 0:
        result.append(p / q)
    else:
        result.append("Not possible")

    return result

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

res = operations_list(n1, n2)

print("Addition =", res[0])
print("Subtraction =", res[1])
print("Multiplication =", res[2])
print("Division =", res[3])

"""----- WITHOUT FUNCTION -----
Enter first number: 11
Enter second number: 22
Addition = 33
Subtraction = -11
Multiplication = 242
Division = 0.5

----- USING FUNCTION WITH RETURN -----
Enter first number: 11
Enter second number: 5
Addition = 16
Subtraction = 6
Multiplication = 55
Division = 2.2

----- USING FUNCTION RETURNING LIST -----
Enter first number: 44
Enter second number: 10
Addition = 54
Subtraction = 34
Multiplication = 440
Division = 4.4 """
