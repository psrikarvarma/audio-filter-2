import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s = 4.42e-5 * s**4 / (s**8 + 0.132*s**7 + 1.179*s**6 + 0.116*s**5 + 0.516*s**4 + 0.033*s**3 + 0.099*s**2 + 0.00322*s + 0.00708)

# Perform substitution
substitution = ((1 - z**-1) / (1 + z**-1))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)
