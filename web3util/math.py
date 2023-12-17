import humanize, datetime

def printDollar(number: int):
    if number >= 1000000000000:
        number = round(number / 1000000000000, 2)
        return "$" + str(number) + "T"
    if number >= 1000000000:
        number = round(number / 1000000000, 2)
        return "$" + str(number) + "B"
    if number >= 1000000:
        number = round(number / 1000000, 2)
        return "$" + str(number) + "M"
    if number >= 1000:
        number = round(number / 1000, 2)
        return "$" + str(number) + "K"
    return "$" + str(number)

def printETime(then: datetime.datetime):
    now = datetime.datetime.now()
    return humanize.naturaltime(now - then)
