import re


def find_coefficient(eq):
    coefs = [0, 0, 0]
    eq = re.sub(r'(X(?!\^))', 'X^1', eq).replace("--", "+").replace("+-", "-").replace("-+", "-")
    all = re.findall('([-+=]?)([\d\.]+)?(\*?[xX](?:\^(\d+))?)?', eq)
    all = [list(item) for item in all]
    all.pop()
    left_side = True
    for item in all:
        if item[0] == '=':
            left_side = False
            if item[2] == '' and item[1] == '':
                continue
        if item[1] == '':
            item[1] = '1'
        if item[3] in ('', '0'):
            index = 0
        elif item[3] == '1':
            index = 1
        else:
            index = 2
        if (item[0] == '-' and not left_side) or (item[0] in ('+', '=', '') and left_side):
            coefs[index] = coefs[index] + float(item[1])
        else:
            coefs[index] = coefs[index] - float(item[1])
    return coefs


def find_solutions(coefs, des):
    if coefs[2] != 0.0 or coefs[2] != 0:
        if des > 0.0:
            return (-coefs[1] - des**(1/2)) / (2 * coefs[2]),  (-coefs[1] + des**(1/2)) / (2 * coefs[2])
        elif des < 0.0:
            return (-coefs[1] - 1j * (-des)**(1/2)) / (2 * coefs[2]),  (-coefs[1] + 1j * (-des)**(1/2)) / (2 * coefs[2])
        else:
            return -coefs[1]/(2 * coefs[2]), "ok"
    elif coefs[1] != 0.0 or coefs[1] != 0:
        if -coefs[0]/coefs[1] == -0.0 or -coefs[0]/coefs[1] == -0:
            return 0, "ok"
        return -coefs[0]/coefs[1], "ok"
    else:
        return "ok", "ok"
