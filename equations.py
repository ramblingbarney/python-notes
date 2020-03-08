# 2. Quadratic Equation

import cmath

def find_roots(a, b, c):
    
    d = (b**2) - (4*a*c)
    
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    
    return (sol1.real, sol2.real)

print(find_roots(2, 10, 8));
