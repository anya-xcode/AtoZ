# Input Output

| | |
|---|---|
| **Striver section** | Learn the Basics — Things to Know in C++/Java/Python or any language |
| **Topic** | Language Basics |
| **Difficulty** | Easy |
| **Tags** | basics, io |
| **Source** | [https://www.naukri.com/code360/problems/input-output](https://www.naukri.com/code360/problems/input-output) |

## Problem Statement

Every judged problem works the same way: your program reads the whole test
from standard input, computes something, and prints the answer to standard
output. Nothing else counts — no prompts, no decorations, no extra blank
words. This first exercise is only about getting that pipe right.

You are given a `name` (one word) and two integers `a` and `b`. Greet the
person, then report the sum and the product of the two numbers, each on its
own line.

## Input Format

- Line 1: a single word `name` made of Latin letters only (no spaces).
- Line 2: two space-separated integers `a` and `b`.

## Output Format

Print exactly three lines:

- Line 1: `Hello, <name>!` — the word `Hello`, a comma, a space, the name, then `!`.
- Line 2: the value of `a + b`.
- Line 3: the value of `a * b`.

## Constraints

- `1 <= length of name <= 20`
- `name contains only the letters a-z and A-Z`
- `-10^6 <= a, b <= 10^6`

## Examples

### Example 1

**Input**

```text
Ada
3 4
```

**Output**

```text
Hello, Ada!
7
12
```

**Explanation:** 3 + 4 = 7 and 3 * 4 = 12, printed on separate lines after the greeting.

### Example 2

**Input**

```text
Grace
-5 9
```

**Output**

```text
Hello, Grace!
4
-45
```

**Explanation:** -5 + 9 = 4 and -5 * 9 = -45. Negative results are printed with a minus sign.

## Test Cases

### Test Case 1

**Input**

```text
Ada
3 4
```

**Expected Output**

```text
Hello, Ada!
7
12
```

### Test Case 2

**Input**

```text
Grace
-5 9
```

**Expected Output**

```text
Hello, Grace!
4
-45
```

All 8 test cases (including 6 hidden) are in [test_cases.txt](test_cases.txt).
