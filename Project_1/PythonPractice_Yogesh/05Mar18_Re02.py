"""
\n
.       - Any character except new lin
\d      - Digits
\D      - Not a digit
\w      - word character(a-z, A-Z, 0-9, _)
\W      - Not a word character
\s      - Whitspace (space, tab, newline)
\S      - Not a whitespace

\b      - Word boundary
\B      - Not a word boundary
^       - Begining of a string
$       - End of a string


[]      - Matches character in bracket
[^ ]    - Matches character not in bracket
|       - Either or
( )     - Group

0 1 2 3 4 5 6 7 8 9
89898763
Meta characters need to be escaped:
[{()\^$|?*+

range of numbers [4-8]
range of characters [a-m]

Quantifiers:
*       - 0 or more
+       - 1 or more
?       - 0 or 1
{3}     - Exact number
{3,9}   - Range of numbers min to max

1) re to match mobile numbers
2) re to match email address
3) Get domain names out of url


import re
findall(string[, pos[, endpos]]) --> list.
finditer(string[, pos[, endpos]]) --> iterator.
"""
