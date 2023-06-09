def ebnf_click(x, left, middle, right):
    if x[1] == 'EBNF':
        return left
    if x[1] == 'CLICK':
        return middle
    return right


def krl(x, left, right):
    if x[3] == 'KRL':
        return left
    return right


def two(x, left, right):
    if x[2] == "LASSO":
        return left
    return right


def main(x):
    if x[0] == 'MAKO':
        return ebnf_click(x, krl(x, 0, 1), two(x, 2, 3), krl(x, 4, 5))
    if x[0] == 'VOLT':
        return ebnf_click(x, 7, two(x, 8, 9), 10)
    if x[0] == "BRO":
        return 6
print(main())
