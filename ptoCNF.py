import re

def to_CNF(expression):
    # Implement the transformation rules to CNF
    # Rule 1: Remove Implications
    expression = re.sub(r'(\w+)\s*=>\s*(\w+)', r'(~\1|\2)', expression)
    # Rule 2: Push negations inward
    while True:
        expression_new = re.sub(r'~\(([^\(\)]+)\)', r'(\1)', expression)
        expression_new = re.sub(r'~(\w+)', r'(\1)', expression_new)
        if expression_new == expression:
            break
        expression = expression_new
    # Rule 3: Distribute OR over AND
    while True:
        expression_new = re.sub(r'\(([^\(\)]+)\)\s*\|\s*\(([^\(\)]+)\)', r'(\1\2)', expression)
        if expression_new == expression:
            break
        expression = expression_new
    # Return the expression in CNF
    return expression

# Example usage
expression = "A => B"
print("Expression: ", expression)
cnf_expression = to_CNF(expression)
print("CNF: ", cnf_expression)
