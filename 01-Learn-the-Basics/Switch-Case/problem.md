# Switch Case

| | |
|---|---|
| **Striver section** | Learn the Basics — Things to Know in C++/Java/Python or any language |
| **Topic** | Language Basics |
| **Difficulty** | Easy |
| **Tags** | basics, conditionals, dispatch |
| **Source** | [https://www.naukri.com/code360/problems/switch-case](https://www.naukri.com/code360/problems/switch-case) |

## Problem Statement

A `switch` picks one branch out of many by matching a value against a list
of labels, with a `default` branch for everything that matches nothing.
Python has no `switch` keyword before 3.10, so the same job is done with an
`if / elif / else` chain or — more idiomatically — a dictionary that maps
each label to the action it should trigger.

Build a tiny calculator. You are given `q` commands; each command is an
operation name followed by two integers `a` and `b`:

| Operation | Result |
| --- | --- |
| `add` | `a + b` |
| `sub` | `a - b` |
| `mul` | `a * b` |
| `div` | `a / b`, rounded down to an integer |
| `mod` | the remainder of `a / b` |

Any other operation name is unsupported: print `invalid` for it — that is
the `default` case.

## Input Format

- Line 1: an integer `q`, the number of commands.
- Next `q` lines: a word `op` (lowercase Latin letters) and two integers `a` and `b`, space-separated.

For every `div` and `mod` command it is guaranteed that `a >= 0` and `b >= 1`,
so the result is an ordinary non-negative integer.

## Output Format

Print `q` lines. Line `i` is the integer result of the `i`-th command, or the
word `invalid` if its operation is not one of the five supported names.

## Constraints

- `1 <= q <= 1000`
- `1 <= length of op <= 10, lowercase Latin letters only`
- `-10^6 <= a, b <= 10^6`
- `For `div` and `mod`: 0 <= a <= 10^6 and 1 <= b <= 10^6`

## Examples

### Example 1

**Input**

```text
5
add 7 5
sub 7 5
mul 7 5
div 7 5
mod 7 5
```

**Output**

```text
12
2
35
1
2
```

**Explanation:** 7 + 5 = 12, 7 - 5 = 2, 7 * 5 = 35, 7 divided by 5 is 1 with remainder 2.

### Example 2

**Input**

```text
3
pow 2 10
add -4 9
mul -3 -6
```

**Output**

```text
invalid
5
18
```

**Explanation:** `pow` is not one of the five supported names, so it falls through to the default branch.

## Test Cases

### Test Case 1

**Input**

```text
5
add 7 5
sub 7 5
mul 7 5
div 7 5
mod 7 5
```

**Expected Output**

```text
12
2
35
1
2
```

### Test Case 2

**Input**

```text
3
pow 2 10
add -4 9
mul -3 -6
```

**Expected Output**

```text
invalid
5
18
```

All 8 test cases (including 6 hidden) are in [test_cases.txt](test_cases.txt).
