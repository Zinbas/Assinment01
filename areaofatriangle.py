"""areaofatriangle.py
Compute the area of a triangle using Heron's formula with validation.

Usage:
    python areaofatriangle.py

This module provides a callable function `triangle_area(a, b, c)` and a
command-line interactive `main()` that prompts for side lengths, validates
inputs, and prints the area rounded to 2 decimal places.
"""

import math
import sys


def triangle_area(a, b, c):
    """Return the area of a triangle with sides a, b, c using Heron's formula.

    Raises ValueError if sides are not positive or do not form a valid triangle.
    """
    a = float(a)
    b = float(b)
    c = float(c)

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive numbers.")

    if not (a + b > c and b + c > a and c + a > b):
        raise ValueError("Side lengths do not satisfy the triangle inequality.")

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def _prompt_float(prompt):
    val = input(prompt)
    try:
        return float(val)
    except ValueError:
        raise ValueError(f"Invalid number: {val!r}")


def main():
    try:
        a = _prompt_float("Enter length of side a: ")
        b = _prompt_float("Enter length of side b: ")
        c = _prompt_float("Enter length of side c: ")
        area = triangle_area(a, b, c)
    except ValueError as exc:
        print("Error:", exc)
        sys.exit(1)

    print("The area of the triangle is:", round(area, 2))


if __name__ == "__main__":
    main()

