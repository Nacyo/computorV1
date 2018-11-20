def print_solutions(z1, z2, coefs):
    if z1 == "ok" and z2 == "ok" and coefs[0] != 0.0:
        print("There is no solution")
    elif z1 != "ok" and z2 != "ok":
        print("The solutions are \n{:.10g}\n{:.10g}".format(z1, z2))
    elif z1 == "ok" and z2 == "ok" and coefs[0] == 0.0:
        print("All real number are solution")
    else:
        print("The solution is {:.10g}".format(z1))


def print_degree(coefs):
    if coefs[2]:
        degree = 2
    elif coefs[1]:
        degree = 1
    else:
        degree = 0
    print("Polynomial degree: {:d}".format(degree))
    return (degree)


def print_reduced_form(coefs):
    if coefs[2] != 0:
        reduced_form = "Reduced form: {:.10g} * X^0 {:+.10g} * X^1 {:+.10g} * X^2 = 0".format(coefs[0], coefs[1], coefs[2])
    elif coefs[1] != 0:
        reduced_form = "Reduced form: {:.10g} * X^0 {:+.10g} * X^1 = 0".format(coefs[0], coefs[1])
    else:
        reduced_form = "Reduced form: {:.10g} * X^0 = 0".format(coefs[0])
    print(reduced_form.replace("+", "+ ").replace("-", "- "))  # mettre un espace entre signe et chiffre


def print_des(des, deg):
    if deg > 0:
        if des > 0:
            print("Discriminant is strictly positive")
        elif des < 0:
            print("Discriminant is strictly negative")
        else:
            print("Discriminant is equal to 0")
