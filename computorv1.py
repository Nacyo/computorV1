import sys
from srcs.errors_eq import *
from srcs.find_eq import *
from srcs.print_eq import *

def main():
     try:
        eq =  error_s()
        if eq == "er":
            sys.exit(1)
        coefs = find_coefficient(eq)
        print_reduced_form(coefs)
        deg = print_degree(coefs)
        des = coefs[1]**2 - 4 * coefs[0] * coefs[2]
        print_des(des, deg)
        z1, z2 = find_solutions(coefs, des)
        print_solutions(z1, z2, coefs)
     except SystemExit as e:
        sys.exit(e)
     except:
        print("Erreur")

main()
