# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

def sum():
    num = int(input("Enter the number : "))
    add = lambda i: i + 25
    print('25 +',num,' = ' , add(num))
    
    return add

if __name__ == "__main__":
    num = sum()
