from bisection_method import bisection
from regula_falsi_method import regula_falsi
from newton_raphson_method import newton_raphson
from secant_method import secant

print("Root Finding for f(x) = x^3 - x - 2\n")

root_bis = bisection(1, 2)
print("Bisection Root:", root_bis)

root_reg = regula_falsi(1, 2)
print("Regula-Falsi Root:", root_reg)

root_new = newton_raphson(1.5)
print("Newton-Raphson Root:", root_new)

root_sec = secant(1, 2)
print("Secant Root:", root_sec)
