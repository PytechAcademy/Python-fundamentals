def example_function():
    x = 10  # Local variable
    print(x)
example_function()
# print(x)  # This will raise an error as x is not defined outside the function.
c = 10  # Global variable

def example_function():
    print(c)
example_function()
print(c)  # Global variable c can be accessed outside the function.

def outer_function():
    x = 10
    def inner_function():
        nonlocal x  # Use the nonlocal keyword to access the non-local variable.
        x += 5
        print(x)
    inner_function()
outer_function()
