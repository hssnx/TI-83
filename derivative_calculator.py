# Derivative Calculator
# Formula used: f'(x) = lim (h->0) [f(x+h) - f(x)] / h

def create_equation_function(equation_str):
    allowed_chars = set("0123456789+-*/(). xX^")
    if not set(equation_str).issubset(allowed_chars):
        raise ValueError("Equation contains disallowed characters")
    equation_str = equation_str.replace('^', '**')

    def evaluate_at_x(x_value):
        return eval(equation_str, {"__builtins__": None}, {"x": x_value})
    return evaluate_at_x


def main():
    equation_input = input("Equation: ")
    equation_func = create_equation_function(equation_input)

    x_value = float(input("Enter x: "))

    h = 0.00001

    derivative = (equation_func(x_value + h) - equation_func(x_value)) / h
    print("Derivative =", round(derivative, 2))
main()