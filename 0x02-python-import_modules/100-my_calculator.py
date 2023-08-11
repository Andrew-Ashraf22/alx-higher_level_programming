#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    ope = sys.argv[2]
    if ope == '+':
        op = add(a, b)
    elif ope == '-':
        op = sub(a, b)
    elif ope == '*':
        op = mul(a, b)
    elif ope == '/':
        op = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(a, b, ope, op))
