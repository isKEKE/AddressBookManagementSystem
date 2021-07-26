# 内存存储
class People(object):
    # 姓名
    name = None
    # 性别
    gender = None
    # 年龄
    age = None
    # 电话
    phone = None
    # 地址
    address = None

    def __getitem__(self, item):
        _lis = ["name","gender","age","phone","address"]
        return _lis[item]




if __name__ == "__main__":
    p = People()
    index = 0
    while True:
        print(p[index])
        index += 1