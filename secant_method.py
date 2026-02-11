def f(x):
    return x**3 - x - 2

def secant(x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
        
        if abs(x2 - x1) < tol:
            print("Iterations:", i+1)
            return x2
        
        x0 = x1
        x1 = x2

    return x2
