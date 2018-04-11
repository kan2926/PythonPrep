
def  pow(dblbase, ipower):
    if ipower == 0:
        return float(1)
    elif ipower < 0:
        return round(1.0/(dblbase*pow(dblbase, -ipower -1)),9)
    else:
        return dblbase * pow(dblbase, ipower-1)

print(pow(4.5, -3))
