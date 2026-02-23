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
