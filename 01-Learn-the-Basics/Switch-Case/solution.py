# Problem: Switch Case
# Approach: Solution (Other)
# Time Complexity: not specified
# Space Complexity: not specified

import sys


def apply_operation(op: str, a: int, b: int) -> str:
    match op:
        case "add":
            return str(a+b)
        case "sub":
            return str(a-b)
        case "mul":
            return str(a*b)
        case "div":
            return str(a//b)
        case "mod":
            return str(a%b) 
        case _ :
            return "invalid"                      
    # Return the result of op applied to a and b as a string,
    # or "invalid" when op is not one of add/sub/mul/div/mod.
    pass


# --- Input/output handling ---
def main():
    data = sys.stdin.read().split()
    q = int(data[0])
    out = []
    for i in range(q):
        op = data[1 + 3 * i]
        a, b = int(data[2 + 3 * i]), int(data[3 + 3 * i])
        out.append(apply_operation(op, a, b))
    print("\n".join(out))


if __name__ == "__main__":
    main()
