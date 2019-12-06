'''
把地址插入
database security.address
id address
'''
import pymysql

#连接数据库
#默认host：localhost，port：3306可不写
# select User,authentication_string,Host from user;显示user Host%所以谁都可以远程登录
db = pymysql.connect(
                     host="localhost",
                     port= 3306,
                     user = "root",
                     passwd = "123456",
                     database = "security",
                     charset = "utf8")

#生成游标对象，以执行sql语句，操作数据库数据，获取执行结果的对象
cur= db.cursor()
# 生成地址至列表addresses 共77111个
area=["梯云纵","燕子坞","还施水阁"]
addresses=[]
for ar in area:
    for house in range(17):
        for unit in range(6):
            for stage in range(22):
                #去掉不吉利的13楼
                if stage !=12:
                    for rm in range(12):
                        address="云从苑%s%d-%d楼%d层%d室"%(ar,house+1,unit+1,stage+1,rm+1)
                        addresses.append(address)

# 写操作
try:
    sql = "insert into address (address) values(%s);"
    cur.executemany(sql,addresses)#传参数，可以不用考虑格式
    db.commit()
except Exception as e:
    print(e)
    db.rollback()


cur.close()
db.close()