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
