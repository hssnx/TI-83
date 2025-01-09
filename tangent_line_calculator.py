def main():
    def tangent_line():
        # Use try-except for basic error handling
        try:
            # Prompt user for inputs
            f_prime = float(input("f'(x): "))  # Derivative at x
            f_a = float(input("f(a): "))       # Function value at a
            a = float(input("a: "))            # Point of tangency
        except ValueError:
            return "Invalid input! Please enter numeric values."

        # Compute slope and y-intercept
        m = f_prime
        c = f_a - m * a

        # Construct the equation as a string
        if c >= 0:
            return f"y = {m}x + {c}"
        else:
            return f"y = {m}x - {-c}"

    # Get and print the tangent line equation
    equation = tangent_line()
    print(f"Equation: {equation}")

# Execute the main function
main()