# Reverse-Polish-Notation-Caculator

[Reverse Polish notation (RPN)](http://en.wikipedia.org/wiki/Reverse_Polish_notation) is a mathematical notation in which every operator follows all of its operands, in contrast to [Polish notation](http://en.wikipedia.org/wiki/Polish_notation), which puts the operator in the prefix position. It is also known as postfix notation and is parenthesis-free as long as operator arities are fixed.#

## Installation

```CMD
$ git clone https://github.com/SamB032/Reverse-Polish-Notation-Caculator.git
$ python rpn.py
```

## Usage
Convert into RPN form:

```Python
#1 + 2 = 3
1 2 + = 3

#1 + 2 - 3 = 0
1 2 + 3 - = 0

#(1 + 2) * 3 = 9
1 2 + 3 * = 9
```

### Available operators

All inputs and cacaulations are saturated, meaning the min and max values of any given number
are -2147483648 and 2147483647. The typed equations can also be spread over multiple lines.

operator | operation                    | example
:-------:|------------------------------|------------
`=`      | Equality                     | `=' = Result of caculation
`+`      | addition                     | `1 2 +` = 3
`-`      | subtraction                  | `1 2 -` = -1
`*`      | multiplication               | `2 3 *` = 6
`/`      | Integer division             | `7 2 /` = 3 
`%`      | modulus                      | `12 5 %` = 2
`^`      | Exponent                     | `4^3` = 64 
`r`      | Random Number Seed           | `r` = Random Number
