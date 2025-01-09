# Tangent Line Calculator
# Formula used: y = f'(a)(x - a) + f(a)

def tangent_line():
    try:
        f_prime = float(input("f'(x): "))
        f_a = float(input("f(a): "))
        a = float(input("a: "))
    except:
        return "Invalid input! Please enter numeric values."

    m = f_prime
    c = f_a - (m * a)

    if c >= 0:
        return "y = " + str(m) + "x + " + str(c)
    else:
        return "y = " + str(m) + "x - " + str(-c)

print("Equation: " + tangent_line())