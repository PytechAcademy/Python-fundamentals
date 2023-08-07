class MathOperations:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z

math_obj = MathOperations()
print(math_obj.add(2, 3))       # This will not work as expected (latest definition will override)
print(math_obj.add(2, 3, 4))    # Output: 9