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
