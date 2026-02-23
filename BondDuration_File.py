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
