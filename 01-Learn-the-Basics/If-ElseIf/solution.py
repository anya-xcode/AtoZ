# Problem: If ElseIf
# Approach: Solution (Other)
# Time Complexity: not specified
# Space Complexity: not specified

import sys


def grade_of(score: int) -> str:
    if 101 > score > 89 :
        return "A"
    elif 90 > score > 74 :
        return "B"
    elif 75 > score > 59 :
        return "C"
    elif 60 > score > 39 :
        return "D"
    elif 40 > score > -1 :
        return "F"
    
    
    # Return "A", "B", "C", "D" or "F" for the given score.
    pass


# --- Input/output handling ---
def main():
    data = sys.stdin.read().split()
    q = int(data[0])
    out = [grade_of(int(data[1 + i])) for i in range(q)]
    print("\n".join(out))


if __name__ == "__main__":
    main()
