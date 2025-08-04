def greet():
    print("Hello, Deepak!")
greet()
# Output: Hello, Deepak!


# Function with Return Value
def square(x):
    return x * x
result = square(4)
print(result)
# Output: 16

# Default Parameters
def welcome(name="Guest"):
    print("Welcome,", name)

welcome()
welcome("Deepak")
# Output:
# Welcome, Guest
# Welcome, Deepak
