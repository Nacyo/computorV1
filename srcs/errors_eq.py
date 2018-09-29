import sys
import re

def format_error_degree(str):
    str = str[1:]
    return (int(str))

def handle_error_degree(list):
    max_value = max(list)
    deg = min(list)
    if max_value > 2:
        deg = max_value
        print("The polynomial degree is {:d}, I cannot solve".format(deg))
    else:
        print("There is a power {:d}, I cannot solve with negative degree".format(deg))

def error_s():
    if len(sys.argv) == 1:
        eq = input('Enter your equation: ')
    elif len(sys.argv) != 2:
        print('Usage: ./computorV1 \"<quadratic equation>\"')
        return "er"
    else:
        eq = sys.argv[1]
    list_deg = re.findall('(\^- ?[0-9]|\^ ?[3-9])', eq)
    if (list_deg):
        error_degree = list(map(format_error_degree, list_deg))
        handle_error_degree(error_degree)
        return "er"
    table = str.maketrans("", "", " \r\n\t\f\v")
    eq = eq.translate(table)
    error_syntax = re.findall(r'(-)(\+-)|(\+)(-\+)|\+\*-|(-)(\*)|(\*-\+)|(-\+\*)|(-)(--)|(--)(\+)|(\+)(--)|(\+)(\+)|(\^)(0([\d]))|(\^)([\d])(\*)|([xX])([xX])|([\d])([xX])|([xX])([*.\d])|([=])([=+])|([\^ =.*])([\^ =.*])|([\^ x.*=X+-])\1|[^\d^ x.*=X+-]|(\^)[^\d]|([\^ .=+*-])$|^([\^ .=*])|^((?!=).)*$', eq)
    if (error_syntax) :
        print('Error syntax, I can\'t solve')
        return "er"
    eq = re.sub('x','X', eq.strip())
    return eq
