# coding:utf-8
def quicksort(list):
    if len(list) < 2:
        return list
    else:
        midpivot = list[0]
        lessbeforemidpivot = [i for i in list[1:] if i <= midpivot]
        print('lessbeforemidpivot:', lessbeforemidpivot)
        biggerafterpivot = [i for i in list[1:] if i > midpivot]
        print('biggerafterpivot:', biggerafterpivot)
        finallylist = quicksort(lessbeforemidpivot) + [midpivot] + quicksort(biggerafterpivot)
        print('finallylist:', finallylist)
        return finallylist


print(quicksort([2, 4, 6, 7, 1, 2, 5]))
