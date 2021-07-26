import pymysql
import config as cfg

class DataBaseOperation(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        '''单例模式'''
        if cls._instance is None:
            cls._instance = super(DataBaseOperation, cls).__new__(cls)
        return cls._instance

    def __init__(self, mode=True):
        if mode:
            self.connect = pymysql.Connect(
                user=cfg.USERNAME,
                password=cfg.PASSWORD,
                host=cfg.HOST,
                port=cfg.PORT,
                db=cfg.DB,
                charset=cfg.CHARSET
            )
            # 获得游标
            self.cursor = self.connect.cursor()

    def insert(self, datas:tuple):
        sql = '''
            INSERT INTO `address_book`(`name`, `gender`, `age`, `phone`, `address`) 
            VALUES (%s, %s, %s, %s, %s);
        '''
        try:
            self.cursor.execute(sql,datas)
        except pymysql.err.Error as exc:
            print(repr(exc))
            self.connect.rollback()
        else:
            self.connect.commit()

    def select(self,keyword=None):
        sql = '''
            SELECT `name`, s.`gender`, `age`, `phone`, `address` FROM `address_book` AS a
            LEFT OUTER JOIN `sex` AS s ON a.`gender` = s.id;
        '''
        if keyword is not None:
            sql = f'{sql.replace(";","")}\tWHERE a.name = "{keyword}";'

        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        # 游标
        if datas:
            self.cursor.scroll(0,'absolute')
        return datas

    def update(self, keyword, *args):
        sql = f'''
                UPDATE `address_book` 
                SET `name`=%s, `gender`=%s, `age`=%s, `phone`=%s, `address`=%s 
                WHERE `name` = "{keyword}";
            '''
        try:
            self.cursor.execute(sql, args)
        except pymysql.err.Error as exc:
            print(repr(exc))
            self.connect.rollback()
        else:
            self.connect.commit()

    def delete(self, keyword=None):
        sql = f'''
            DELETE FROM `address_book` WHERE `name` = "{keyword}";
        '''
        try:
            rows = self.cursor.execute(sql)
        except pymysql.err.Error:
            self.connect.rollback()
            return 0
        else:
            self.connect.commit()
            return rows

    def clear(self):
        sql = '''
            TRUNCATE TABLE `address_book`;
        '''
        self.cursor.execute(sql)
        # try:
        #     self.cursor.execute(sql)
        # except pymysql.err.Error:
        #     self.connect.rollback()
        # else:
        #     self.connect.commit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        # 关闭链接
        self.cursor.close()
        self.connect.close()

if __name__ == '__main__':
    import random
    import time
    from pprint import pprint
    names = list('ABCDE')
    address = '河北、上海、北京、南京、浙江'.split('、')
    datas = [
        (
            name,
            random.randint(1,2),
            random.randint(0,100),
            f'1{random.randint(1,9)}%s' % f"{int(time.time() * random.randint(1,100))}"[:9],
            random.choice(address)
        ) for name in names
    ]
    with DataBaseOperation() as db:
        pprint(db.select())
