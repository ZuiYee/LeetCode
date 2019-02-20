# 在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
#
# 使用Step-wise线性搜索。
def get_value(l, r, c):
    return l[r][c]

def find(l, x):
    # l为矩形 x为查找数
    m = len(l) - 1  # 矩形列长
    n = len(l[0]) - 1  # 矩形行长
    r = 0
    c = n
    while c >=0 and r<=m:
        value = get_value(l, r, c)
        print(value)
        if value == x:
            return True
        elif value > x:
            c = c - 1
        elif value < x:
            r = r + 1


def main():
    L = [[1, 3, 4, 5, 9, 10, 11], [2, 4, 5, 6, 8, 11, 12], [12, 23, 24, 25, 28, 30, 33]]
    x = 30
    find(L,6)

if __name__ == '__main__':
    main()
