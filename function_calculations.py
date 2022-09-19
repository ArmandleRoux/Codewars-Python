def one(a="1"):
    if a[0] == "/":
        return str(1 / int(a[1]))
    elif a[0] == "*":
        return str(1 * int(a[1]))
    elif a[0] == "+":
        return str(1 + int(a[1]))
    elif a[0] == "-":
        return str(1 - int(a[1]))
    else:
        return a


def two(a="2"):
    if a[0] == "/":
        return str(2 / int(a[1]))
    elif a[0] == "*":
        return str(2 * int(a[1]))
    elif a[0] == "+":
        return str(2 + int(a[1]))
    elif a[0] == "-":
        return str(2 - int(a[1]))
    else:
        return a


def three(a="3"):
    if a[0] == "/":
        return str(3 / int(a[1]))
    elif a[0] == "*":
        return str(3 * int(a[1]))
    elif a[0] == "+":
        return str(3 + int(a[1]))
    elif a[0] == "-":
        return str(3 - int(a[1]))
    else:
        return a


def four(a="4"):
    if a[0] == "/":
        return str(4 / int(a[1]))
    elif a[0] == "*":
        return str(4 * int(a[1]))
    elif a[0] == "+":
        return str(4 + int(a[1]))
    elif a[0] == "-":
        return str(4 - int(a[1]))
    else:
        return a


def five(a="5"):
    if a[0] == "/":
        return str(5 / int(a[1]))
    elif a[0] == "*":
        return str(5 * int(a[1]))
    elif a[0] == "+":
        return str(5 + int(a[1]))
    elif a[0] == "-":
        return str(5 - int(a[1]))
    else:
        return a


def six(a="6"):
    if a[0] == "/":
        return str(6 / int(a[1]))
    elif a[0] == "*":
        return str(6 * int(a[1]))
    elif a[0] == "+":
        return str(6 + int(a[1]))
    elif a[0] == "-":
        return str(6 - int(a[1]))
    else:
        return a


def seven(a="7"):
    if a[0] == "/":
        return str(7 / int(a[1]))
    elif a[0] == "*":
        return str(7 * int(a[1]))
    elif a[0] == "+":
        return str(7 + int(a[1]))
    elif a[0] == "-":
        return str(7 - int(a[1]))
    else:
        return a


def eight(a="8"):
    if a[0] == "/":
        return str(8 / int(a[1]))
    elif a[0] == "*":
        return str(8 * int(a[1]))
    elif a[0] == "+":
        return str(8 + int(a[1]))
    elif a[0] == "-":
        return str(8 - int(a[1]))
    else:
        return a


def nine(a="9"):
    if a[0] == "/":
        return str(9 / int(a[1]))
    elif a[0] == "*":
        return str(9 * int(a[1]))
    elif a[0] == "+":
        return str(9 + int(a[1]))
    elif a[0] == "-":
        return str(9 - int(a[1]))
    else:
        return a


def divided_by(a):
    return "/" + a


def times(a):
    return "*" + a


def plus(a):
    return "+" + a


def minus(a):
    return "-" + a


print(three(times(eight())))
print(five(plus(nine())))
print(four(divided_by(two())))
print(seven(minus(one())))
