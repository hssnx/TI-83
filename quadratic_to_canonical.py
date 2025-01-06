def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a numeric value.")

def canonical_form(a, b, c):
    h = -b / (2 * a)
    k = c - (b**2) / (4 * a)
    return h, k

def main():
    a = get_float("Enter a: ")
    while a == 0:
        print("Coefficient 'a' cannot be zero for a quadratic equation.")
        a = get_float("Enter a: ")
    b = get_float("Enter b: ")
    c = get_float("Enter c: ")

    h, k = canonical_form(a, b, c)
    print("Canonical form: {}(x - {:.2f})^2 + {:.2f}".format(a, h, k))

    summit = (round(h, 2), round(k, 2))
    print("Summit: ", summit)
main()