"""Sample Python application for CI demo.

Provides a simple `add` function and a command-line entry point.
"""

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference a - b."""
    return a - b


if __name__ == '__main__':
    # Simple demo when running directly
    print("add(2, 3) ->", add(2, 3))
