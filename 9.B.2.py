def maxx2(a):
    if len(a) < 2:
        return 0
    if a[-1] == 0:
        a = a[:-1]
    if len(a) < 2:
        return 0
    maxch = a[0]
    max2 = 0

    def max(bb, maxrn, max2rn):
        if not bb:
            return maxrn, max2rn
        h = bb[0]
        s = bb[1:]
        if h > maxrn:
            return max(s, h, maxrn)
        elif h > max2rn and h != maxrn:
            return max(s, maxrn, h)
        else:
            return max(s, maxrn, max2rn)
    maxch, max2 = max(a, maxch, max2)
    return max2
print(maxx2(120))