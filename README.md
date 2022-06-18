# markov-algo
A program to write &amp; run Markov algorithms on natural numbers.

## Running
``python main.py``

## Rules
Rules should be of form a -> b where a and b are some sequences of characters.

Rules are scanned through from top to bottom until for given input it contains the left hand side of some rule. A first occurence of such substring is replaced by the rule's right hand side. Then, the scan repeats.

If no applicable rules were found during the scan or a rule marked final was used, the algorithm halts.

To mark a rule final, put a dot after the arrow: ``# -> .|``

For empty word, write ``a -> `` or `` -> b``.

Some algorithms may have undefined outputs for certain inputs, so the program might enter an infinite loop. There's no way to figure out whether this will happen in general, according to the [Halting problem](https://en.wikipedia.org/wiki/Halting_problem).

**Example 1** - MA for function ``f(x) = x / 2``:
```
1. #|| -> |#
2. #| -> #|
3. # -> .
4. -> #

Input: ||||
Rule 4: |||| -> #||||
Rule 1: #|||| -> |#||
Rule 1: |#|| -> ||#
Rule 3: ||# -> ||
Output: ||
```

Note that the second rule handles the undefined case for the odd number (``x / 2`` is not an integer for odd ``x``).

**Example 2** - MA for function ``f(x, y) = x + y``
```
1. # ->

Input: ||||#||
Rule 1: ||||#|| -> ||||||
Output: ||||||
```

To add two numbers in unary system, we can simply remove the separator between them. 
