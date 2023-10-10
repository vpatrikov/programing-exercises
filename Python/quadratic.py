import cmath

def quadratic (a, b, c):
    d = b**2 - 4*a*c
    
    if d == 0:
        x1 = -b/(2*a)
        x2 = -b/(2*a)
    elif d > 0:
        x1 = (-b + cmath.sqrt(d))/(2*a)
        x2 = (-b - cmath.sqrt(d))/(2*a)
    elif d < 0:
        print("No real solutions")
        
