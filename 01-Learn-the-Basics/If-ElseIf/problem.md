# If ElseIf

| | |
|---|---|
| **Striver section** | Learn the Basics — Things to Know in C++/Java/Python or any language |
| **Topic** | Language Basics |
| **Difficulty** | Easy |
| **Tags** | basics, conditionals |
| **Source** | [https://www.naukri.com/code360/problems/if-elseif](https://www.naukri.com/code360/problems/if-elseif) |

## Problem Statement

A chain of `if / else if / else` picks **exactly one** branch: the
conditions are tested top to bottom and the first true one wins, so the
order you write them in is part of the logic.

You are given `q` exam scores. Convert each score to a letter grade using
these bands:

| Score | Grade |
| --- | --- |
| 90 to 100 | `A` |
| 75 to 89 | `B` |
| 60 to 74 | `C` |
| 40 to 59 | `D` |
| 0 to 39 | `F` |

The bands do not overlap and together they cover every allowed score.

## Input Format

- Line 1: an integer `q`, the number of scores.
- Next `q` lines: one integer `score` each.

## Output Format

Print `q` lines. Line `i` is the single uppercase letter grade of the `i`-th score.

## Constraints

- `1 <= q <= 1000`
- `0 <= score <= 100`

## Examples

### Example 1

**Input**

```text
4
95
78
61
12
```

**Output**

```text
A
B
C
F
```

**Explanation:** 95 falls in 90-100, 78 in 75-89, 61 in 60-74 and 12 in 0-39.

### Example 2

**Input**

```text
3
90
89
40
```

**Output**

```text
A
B
D
```

**Explanation:** The boundaries belong to the higher band: 90 is already an A, while 89 is still a B and 40 is the lowest D.

## Test Cases

### Test Case 1

**Input**

```text
4
95
78
61
12
```

**Expected Output**

```text
A
B
C
F
```

### Test Case 2

**Input**

```text
3
90
89
40
```

**Expected Output**

```text
A
B
D
```

All 8 test cases (including 6 hidden) are in [test_cases.txt](test_cases.txt).
