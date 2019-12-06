'''
把单词本插入
database dict.words
id word mean
'''
import pymysql
import hashlib


class DatabaseModel():
    def __init__(self):
        self.db = pymysql.connect(host = "176.17.1.74",
                     port= 3306,
                     user = "root",
                     passwd = "123456",
                     database = "security",
                     charset = "utf8")
        self.cur= None

    def create_cur(self): #一个database可以生成多个游标
        self.cur=self.db.cursor()


    # def register(self,name,password):
    #     '''
    #     每次注册一个游标生灭、密码加密；用户名密码不含空字符
    #     登录成功-1
    #     注册成功-2
    #     注册或登录失败-3
    #     '''
    #     if self.login(name,password):
    #         return 1
    #     try:
    #         self.create_cur()
    #         password = change_passwd(password)
    #         sql = "insert into login (user,password) \
    #               values(%s,%s);"
    #         self.cur.execute(sql,[name,password])#传参数，可以不用考虑格式
    #         self.db.commit()
    #         self.cur.close()
    #         self.login(name,password)
    #         return 2
    #     except Exception as e:
    #         print(e)
    #         self.db.rollback()
    #         self.cur.close()
    #         return 3
    #
    # def login(self,name,password):
    #     '''
    #     每次登录一个游标生灭
    #     登录成功-返回True
    #     登录失败-返回False
    #     密码加密
    #     '''
    #     self.create_cur()
    #     sql = "select user, password from login;"
    #     self.cur.execute(sql)
    #     password = change_passwd(password)
    #     for i in self.cur:
    #         if name == i[0] and password == i[1]:
    #             print("succeed!")
    #             self.cur.close()
    #             return True
    #     self.cur.close()
    #     return False
    #
    #
    # def check(self,word,name):
    #     '''
    #     添加查找历史
    #     每次查找一个游标生灭
    #     查找成功-返回释义
    #     查找失败-返回False
    #     '''
    #     self.create_history(word,name)
    #     try:
    #         self.create_cur()
    #         sql = "select meaning from dict where word = '%s';"%(word)
    #         self.cur.execute(sql)
    #         re = ""
    #         for i in self.cur:
    #             re = i[0]
    #         self.cur.close()
    #         return re
    #     except Exception as e:
    #         print(e)
    #         self.db.rollback()
    #         self.cur.close()
    #         return False
    #
    # def create_history(self,word,name):
    #     try:
    #         self.create_cur()
    #         sql = " insert into history0 (user, word) values(%s,%s);"
    #         self.cur.execute(sql,[name,word])
    #         self.db.commit()
    #     except Exception as e:
    #         print(e)
    #         self.db.rollback()
    #     finally:
    #         self.cur.close()
    #
    # def history(self):
    #     try:
    #         self.create_cur()
    #         sql = "select user,word,time from history0 order by time desc limit 10;"
    #         self.cur.execute(sql)
    #         result = []
    #         for i in self.cur:
    #             result.append(i)
    #         self.cur.close()
    #         return result
    #     except Exception as e:
    #         print(e)
    #         self.db.rollback()
    #         self.cur.close()
    #         return False
    #
    # def close(self):
    #     self.db.close()
    #
    def add_car(self, owners_visiters, plate_number, address, tels):
        '''
        add_car(业主车辆登记/来访车辆登记)
        输入 业主/访客 车牌号 住址(参考_address.py) 联系电话 e.g.db.add_car("owners", "浙A323UU", ("梯云纵",1,6,9,1), '12306')
        输出(是否添加成功) True False
        '''
        address="云从苑%s%d-%d楼%d层%d室"%(address[0],address[1],address[2],address[3],address[4])
        try:
            self.create_cur()
            sql = "insert into plates (`owners/visiters`, plate_number, tels, address_id) values(%s,%s,%s,(select id from address where address=%s));"
            self.cur.execute(sql,[owners_visiters,plate_number,tels,address])
            self.db.commit()
            self.cur.close()
            return True
        except Exception as e:
            print(e)
            self.db.rollback()
            self.cur.close()
            return False

    def check_car(self, plates_number, in_out):
        '''
        check_car(车辆准入/放行)
        输入 车牌号 进/出 e.g. db.check_car("浙A323UU","in")
        输出 False(未登记访客)/True(业主或已登记访客)
        '''

        try:
            self.create_cur()
            sql = "select plate_number from plates where plate_number= '%s';"%(plates_number)
            self.cur.execute(sql)
            number=""
            for i in self.cur:
                number=i
            self.cur.close()
            if number=="":
                return False
            else:
                # self.create_history(plates_number, in_out)
                return True
        except Exception as e:
            print(e)
            self.db.rollback()
            self.cur.close()
            return False

    def check_person(self, owners_id, in_out):
        '''
        check_person(人员准入/放行)
        输入 人员_id 进/出e.g.result=db.check_person(None/9166,"in")
        输出 False(未登记访客)/True(业主或已登记访客)
        '''

        try:
            self.create_cur()
            sql = "select * from owners where id='%s';" % (owners_id)
            self.cur.execute(sql)
            number = ""
            for i in self.cur:
                number = i
            self.cur.close()
            if number == "":
                return False
            else:
                # self.create_history(owners_id, in_out)
                return True
        except Exception as e:
            print(e)
            #地址不在册:(1048, "Column 'address_id' cannot be null")
            self.db.rollback()
            self.cur.close()
            return False


# db=DatabaseModel()
# result=db.add_car("visiters", "闵A323UU", ("梯云纵",1,6,9,1), '12345')
# print(result)