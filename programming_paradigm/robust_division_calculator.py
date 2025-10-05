def safe_divide(numerator, denominator):
    """Performs safe division with error handling for zero and invalid inputs."""
    try:
        # Try to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Attempt division
        try:
            result = num / den
            return f"The result of dividing {num} by {den} is {result:.2f}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Both inputs must be numeric values."

import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
