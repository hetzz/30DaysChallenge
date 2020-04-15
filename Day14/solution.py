def stringShift(s,shift):
    new_str = ""
    total_shift = 0
    for k in shift :
        if k[0] == 0:
            k[1] = -1 * k[1]
        total_shift += k[1]
    print(total_shift)
    total_shift = total_shift % len(s)
    if total_shift > 0 :
        new_str = s[-total_shift:] + s[:-total_shift]
    elif total_shift < 0:
        new_str = s[-total_shift:] + s[:-total_shift]
    else:
        new_str = s
    return new_str

s = "xqgwkiqpif"
shift = [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]
print(stringShift(s,shift))