def countElements(arr):
    dict_no = {}
    for x in arr:
        dict_no[x] = 0
    for x in arr :
        try:
            dict_no[x+1] += 1
        except:
            continue
    return sum(list(dict_no.values()))

arr = [1,1,2,2]
print(countElements(arr))