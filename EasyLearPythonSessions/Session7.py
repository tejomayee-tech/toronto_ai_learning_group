
class my_math:

    def add(self,first_number: int, second_number: int):
        """Adds two numbers."""
        return first_number + second_number

    def sub(self,first_number: int, second_number: int):
        """Adds two numbers."""
        return first_number - second_number

    def mul(self,first_number: int, second_number: int):
        """Adds two numbers."""
        return first_number * second_number

    def div(self,first_number: int, second_number: int):
        """Adds two numbers."""
        return first_number / second_number

    def print_some_numer(self):
        print(100)

# sum = add(5,10)
# print(sum)

# product = mul(5,10)
# print(product)

math_class = my_math()

sum = math_class.add(5,10)
print(sum)

math_class.print_some_numer()