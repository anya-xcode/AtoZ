# Problem: Input Output
# Approach: Solution (Other)
# Time Complexity: not specified
# Space Complexity: not specified

import sys
from typing import List


def build_lines(name: str, a: int, b: int) -> List[str]:
    x = "Hello, "+ name+"!" 
    y =  a + b
    z = a * b
    return x, y , z
    
    # Return the three output lines: the greeting, then a + b, then a * b.
    pass


# --- Input/output handling ---
def main():
    data = sys.stdin.read().split()
    name = data[0]
    a, b = int(data[1]), int(data[2])
    for line in build_lines(name, a, b):
        print(line)


if __name__ == "__main__":
    main()
