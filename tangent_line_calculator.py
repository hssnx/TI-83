def tangent_line():
    # Basic attempt to parse user inputs as floats
    try:
        f_prime = float(input("f'(x): "))
        f_a = float(input("f(a): "))
        a = float(input("a: "))
    except:
        return "Invalid input! Please enter numeric values."

    # Compute slope (m) and intercept (c)
    m = f_prime
    c = f_a - (m * a)

    # Construct the equation string using basic concatenation
    if c >= 0:
        return "y = " + str(m) + "x + " + str(c)
    else:
        return "y = " + str(m) + "x - " + str(-c)

# Print the result directly
print("Equation: " + tangent_line())