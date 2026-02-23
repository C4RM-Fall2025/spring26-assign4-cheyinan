def WhoAmI():
    return "yc4796"

def getBondPrice(y, face, couponRate, m, ppy=1):
    y = y / ppy
    couponRate = couponRate / ppy
    periods = m * ppy
    bondPrice = 0
    for t in range(1, periods + 1):
        cashflow = face * couponRate
        if t == periods:
            cashflow += face
        bondPrice += cashflow / (1 + y) ** t 
    return bondPrice

def getBondDuration(y, face, couponRate, m, ppy=1):
    y = y / ppy
    couponRate = couponRate / ppy
    periods = m * ppy
    bondPrice = 0
    weightedSum = 0
    for t in range(1, periods + 1):
        cashflow = face * couponRate
        if t == periods:
            cashflow += face
        pv = cashflow / (1 + y) ** t
        bondPrice += pv
        weightedSum += t * pv
    bondDuration = weightedSum / bondPrice / ppy
    return bondDuration

def getBondPrice_E(face, couponRate, yc):
    m = len(yc)
    coupon = face * couponRate
    bondPrice = 0
    for i in range(m):
        t = i + 1
        rate = yc[i]
        cashflow = coupon
        if i == m - 1:
            cashflow += face
        pv = cashflow / (1 + rate) ** t
        bondPrice += pv
    return bondPrice

def getBondPrice_Z(face, couponRate, times, yc):
    coupon = face * couponRate
    bondPrice = 0
    m = len(times)
    for i in range(m):
        t = times[i]
        rate = yc[i]
        cashflow = coupon
        if i == m - 1:
            cashflow += face
        pv = cashflow / (1 + rate) ** t
        bondPrice += pv
    return bondPrice

def FizzBuzz(start, finish):
    for i in range(start, finish + 1):
        if i % 15 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
