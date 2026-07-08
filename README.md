# First-Coded-Calculator

A simple command-line calculator that takes two numbers and an operation
(add, subtract, multiply, divide), with input validation so it won't crash
on bad input.

**To run:** `python calculator.py`

## Features I built in
- Input validation using try/except so non-numeric input doesn't crash it
- while/break loops that re-ask until the input is valid
- Menu validation for the operation choice
- Divide-by-zero handling
- Specific exception catching (`except ValueError`) instead of a bare except

## Notes
Built using u/RockPhily's calculator code as an outline.

I used AI (Claude) to help clarify and explain some parts of this code —
explaining concepts like try/except, while loops, and break; pointing me
toward bugs (a misplaced break, a divide-by-zero crash, using a bare except
instead of `except ValueError`) by asking questions rather than handing me
answers; and helping me understand tracebacks. But I wrote and debugged 90%
of this calculator's code myself.

Today is July 7th, 2026. I plan on becoming a Software Developer or working
in Cybersecurity. — Derick S Martinez
