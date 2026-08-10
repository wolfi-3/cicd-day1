import sys
from calc import add, subtract, divide


def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <add|subtract|divide> <a> <b>")
        sys.exit(1)

    op, a, b = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])

    operations = {
        "add": add,
        "subtract": subtract,
        "divide": divide,
    }

    if op not in operations:
        print(f"Unknown operation: {op}")
        sys.exit(1)

    result = operations[op](a, b)
    print(result)


if __name__ == "__main__":
    main()

# ci trigger fix
