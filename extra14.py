#14. Write a function to multiply all the numbers in a list. (Numbers can be negative, 
#positive or zero).

def multilist():
    lst=[2,3,2,-2,3]
    p=1
    for i in lst:
        p=p*i
    return p
a=multilist()
print("multiplication is :",a)

#15. Write a function to calculate the factorial of a number. The function accepts the 
#number as an argument.

def factorial(a):
    if a==0 :
        return 1
    else:
        return a * factorial(a-1)

b=factorial(4)
print("factoral of given number is "b)

#16. Write a function that takes a list and returns a new list with distinct elements from 
#the first list.
def largest(lst):
    


lst=[1,22,44,2,-55]
a=largest(lst)
print(a)










