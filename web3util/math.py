import humanize, datetime

def printDollar(number: int):
    flag = False
    if number < 0:
        flag = True
        number = -1 * number
    if number >= 1000000000000:
        number = round(number / 1000000000000, 2)
        return "$" + "{0:.2f}".format(number) + "T"
    if number >= 1000000000:
        number = round(number / 1000000000, 2)
        return "$" + "{0:.2f}".format(number) + "B"
    if number >= 1000000:
        number = round(number / 1000000, 2)
        return "$" + "{0:.2f}".format(number) + "M"
    if number >= 1000:
        number = round(number / 1000, 2)
        return "$" + str(number) + "K"
    return ("-" if flag else "") + "$" + "{0:.2f}".format(number)

def printETime(then: datetime.datetime):
    now = datetime.datetime.now()
    return humanize.naturaltime(now - then) + " ("+str(then)+")"

def printToken(number: int, token: str):
    token = token.upper()
    if number >= 1000000000000:
        number = round(number / 1000000000000, 2)
        return "{0:.2f}".format(number) + "T " + token
    if number >= 1000000000:
        number = round(number / 1000000000, 2)
        return "{0:.2f}".format(number) + "B " + token
    if number >= 1000000:
        number = round(number / 1000000, 2)
        return "{0:.2f}".format(number) + "M " + token
    if number >= 1000:
        number = round(number / 1000, 2)
        return "{0:.2f}".format(number) + "K " + token
    return "{0:.2f}".format(number) + " " + token

