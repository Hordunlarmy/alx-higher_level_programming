#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

argv = sys.argv

if (len(argv) < 2) or (len(argv) > 4):
    print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
elif (len(argv) == 4):
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    if (operator == "+"):
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif (operator == "-"):
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif (operator == "*"):
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif (operator == "/"):
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        print(f"Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
