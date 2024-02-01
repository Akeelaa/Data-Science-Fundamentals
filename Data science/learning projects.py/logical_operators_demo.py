"""
Demonstrating logical operators: and, or, and not.

Conjunction (and) - Both conditions must be true:
If 10 is less than 50 AND 500 is greater than 100, it prints "this is a conjunction."
Otherwise, it prints "not a conjunction."

Disjunction (or) - Either one condition must be true:
If 10 is less than 50 OR 500 is greater than 100, it prints "this is a disjunction."
Otherwise, it prints "not a disjunction."

Negation (not) - Opposite is true:
If NOT 100 is less than 500, it prints "this is negation."
Otherwise, it prints "not negation."
"""

# Conjunction (and)
if 10 < 50 and 500 > 100:
    print("This is a conjunction")
else:
    print("Not a conjunction")

# Disjunction (or)
if 10 < 50 or 500 > 100:
    print("This is a disjunction")
else:
    print("Not a disjunction")

# Negation (not)
if not 100 < 500:
    print("This is negation")
else:
    print("Not negation")
