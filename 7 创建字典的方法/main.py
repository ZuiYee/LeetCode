# 1 直接创建
def idea1():
    dict = {'name': 'earth', 'port': '80'}


# 2 工厂方法
#
def idea2():
    items = [('name', 'earth'), ('port', '80')]
    dict2 = dict(items)
    dict1 = dict((['name', 'earth'], ['port', '80']))


# 3 fromkeys()方法
#

def idea3():
    dict1 = {}.fromkeys(('x', 'y'), -1)
    dict = {'x': -1, 'y': -1}
    dict2 = {}.fromkeys(('x', 'y'))
    dict2 = {'x': None, 'y': None}
