# 通讯簿联系人列表操作

class ContactPersonOperation(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        '''单例模式'''
        if cls._instance is None:
            cls._instance = super(ContactPersonOperation, cls).__new__(cls)
        return cls._instance

    def __init__(self, info, db):
        self.info = info
        self.db = db
        self._keyNames = ("姓名","性别","年龄","电话","地址")

    def server_say(self):
        context = '''
            *****************************
            *****\t1、添加联系人\t*****
            *****\t2、显示联系人\t*****
            *****\t3、删除联系人\t*****
            *****\t4、查找联系人\t*****
            *****\t5、修改联系人\t*****
            *****\t6、清空联系人\t*****
            *****\t0、退出通讯录\t*****
            *****************************
        '''.replace(' ','')
        print(context,end='')

    def write(self, oldData=None):
        _typeNames = dict(zip(list(self.info),self._keyNames))
        index = 0
        for key, title in _typeNames.items():
            reply = input(f'\t-{title}:') or None
            if reply is None and oldData is not None:
                reply = oldData[index]
            print(reply)
            setattr(self.info, key, reply)
            index += 1

        # 判断性别传入参数
        if self.info.gender is None:
            self.info.gender = 1
        elif self.info.gender == '男':
            self.info.gender = 1
        elif self.info.gender == '女':
            self.info.gender = 2

    def pprint(self,*args):
        for data in args[0]:
            list(
                map(
                    lambda x: print(f"\t{x[0]}: {x[1]}", end=' '),zip(self._keyNames, data)
                )
            )
            print()


    def add(self):
        # 写入到内存
        self.write()
        # 写入到Mysql数据库
        self.db.insert(
            datas=tuple(
                getattr(self.info,key) for key in self.info)
        )

    def show(self):
        datas = self.db.select()
        self.pprint(datas)

    def delete(self):
        reply = input('请输入关键字(姓名):\t')
        if input('Y/N?\t').lower() == 'y':
            flag = self.db.delete(reply)
        else:
            flag = False
        # 判断是否删除成功
        if flag:
            print('删除成功')
        else:
            print('删除失败')

    def find(self):
        reply = input("请输入关键字(姓名):") or -1
        data = self.db.select(reply)
        if data:
            self.pprint(data)
        else:
            print('查找失败')

    def update(self):
        reply = input('请输入关键字(姓名):\t')
        datas = self.db.select(reply)
        if datas:
            self.write(datas[0])
            self.db.update(
                reply,*tuple(getattr(self.info,key)for key in self.info)
            )

    def clear(self):
        if input('Y/N?\t').lower() == 'y':
            self.db.clear()

if __name__ == '__main__':
    pass