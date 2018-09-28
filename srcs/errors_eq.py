import sys
import re

def error_s():
    if len(sys.argv) == 1:
        eq = input('Enter your equation: ')
    elif len(sys.argv) != 2:
        print('Usage: ./computorV1 \"<quadratic equation>\"')
        return "er"
    else:
        eq = sys.argv[1]
    error_degree = re.findall('(\^- ?[0123456789]|\^ ?[3456789])', eq)
    if (error_degree) :
        print('Error degree, I can\'t solve')
        return "er"
    table = str.maketrans("", "", " \r\n\t\f\v")
    eq = eq.translate(table)
    error_syntax = re.findall(r'(-)(\*)|(-)(--)|(--)(\+)|(\+)(--)|(\+)(\+)|(\^)(0([\d]))|(\^)([\d])(\*)|([xX])([xX])|([\d])([xX])|([xX])([*.\d])|([=])([=+])|([\^ =.*])([\^ =.*])|([\^ x.*=X+-])\1|[^\d^ x.*=X+-]|(\^)[^\d]|([\^ .=+*-])$|^([\^ .=*])|^((?!=).)*$', eq)
    if (error_syntax) :
        print('Error syntax, I can\'t solve')
        return "er"
    eq = re.sub('x','X', eq.strip())
    return eq
