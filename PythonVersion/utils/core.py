# 核心文件
import os
from utils.info import People
from contacts import ContactPersonOperation
from db import DataBaseOperation

class Core(object):
    def __init__(self):
        self.info = People()
        self.db = DataBaseOperation()
        self.cpo = ContactPersonOperation(self.info, self.db)

    def start(self):
        while True:
            self.cpo.server_say()
            reply = input('>>>')
            if reply == '0':
                break
            elif reply != '':
                if reply == '1':
                    self.cpo.add()

                elif reply == '2':
                    self.cpo.show()

                elif reply == '3':
                    self.cpo.delete()

                elif reply == '4':
                    self.cpo.find()

                elif reply == '5':
                    self.cpo.update()
                elif reply == '6':
                    self.cpo.clear()
                os.system("pause")
            os.system('cls')
        os.system("pause")
        self.db.close()