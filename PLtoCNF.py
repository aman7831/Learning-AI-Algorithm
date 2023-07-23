from sympy.logic import simplify_logic
from sympy.logic.boolalg import to_cnf

def propositional_to_CNF(formula):
    formula = simplify_logic(formula, form='cnf')
    return to_cnf(formula)

formula = "(A & B) | (~A & C)"
print("The given formula: ", formula)
print("In CNF: ", propositional_to_CNF(formula))
