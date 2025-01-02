## a python script which converts a quadratic equation to its canonical form

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a numeric value.")

# Convert quadratic equation ax^2 + bx + c to canonical form
# Canonical form: a(x-h)^2 + k

def canonical_form(a, b, c):
    h = -b / (2 * a)  # Vertex x-coordinate
    k = c - (b**2) / (4 * a)  # Vertex y-coordinate
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

    # the summit of the parabola is at (h, k)
    summit = (round(h, 2), round(k, 2))
    print("Summit: ", summit)

main()
