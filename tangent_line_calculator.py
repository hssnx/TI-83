def main():
    def tangent_line():
        try:
            f_prime = float(input("f'(x): "))
            f_a = float(input("f(a): "))
            a = float(input("a: "))
        except ValueError:
            return "Invalid input! Please enter numeric values."

        m = f_prime
        c = f_a - m * a

        if c >= 0:
            equation = f"y = {m}x + {c}"
        else:
            equation = f"y = {m}x - {-c}"
        return equation

    equation = tangent_line()
    print(f"Equation: {equation}")

main()