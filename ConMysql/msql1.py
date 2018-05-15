#coding=utf-8
#python连接数据步骤
#1、导入数据库驱动模块import mysql.connector
#2、打开数据库连接
#   cnn = mysql.connector.connect(user='root',passwd='',database='mysql')
#3、使用cursor()方法获取操作游标
#   cursor=cnn.cursor()
#4、使用execute方法执行SQL语句
#   cursor.execute(sql)
#5、关闭数据库连接
#   cnn.close()

# 注：如果数据库连接参数多 可以写成字典模式
config={'host':'127.0.0.1',#默认127.0.0.1
        'user':'root',
        'password':'',
        'port':3306 ,#默认即为3306
        'database':'mysql',
        'charset':'utf8'#默认即为utf8
        }
import mysql.connector
# 创建连接
cnn = mysql.connector.connect(**config)
cursor = cnn.cursor()
class conMysql:
    # 1、创建表
    def creatTable(self):
        sql_create_table = 'CREATE TABLE IF NOT EXISTS `student` ' \
                           '(id int(10) NOT NULL AUTO_INCREMENT,' \
                           'name varchar(10) DEFAULT NULL,' \
                           'age int(3) DEFAULT NULL,' \
                           'PRIMARY KEY (`id`))' \
                           'CHARSET=utf8'
        cursor.execute(sql_create_table)

    # 2、插入数据(三种方式)
    def insertData(self):
        # 2.1直接插入
        sql_insert1 = 'INSERT INTO STUDENT(name,age,BirthDay)' \
                      'values("Rose",22,"1999-05-01")'
        cursor = cnn.cursor()
        cursor.execute(sql_insert1)
        # 2.3元组连接插入
        sql_insert2 = 'INSERT INTO STUDENT(name,age) VALUES(%s,%s)'  # 此处的%s是占位符
        data = ('shiki', 25)
        cursor.execute(sql_insert2, data)
        # 2.3字典连接插入
        sql_insert3 = 'INSERT INTO STUDENT(name,age) VALUES (%(name)s, %(age)s)'
        data = {'name': 'Ailis', 'age': '30'}
        cursor.execute(sql_insert3, data)
    # 3、查询操作
    def query(self):
        sql_query='SELECT name,age FROM STUDENT WHERE age > %s'
        cursor = cnn.cursor()
        cursor.execute(sql_query,(25,))
        if cursor:
            for name,age in cursor:
                print('%s’s age is older than 20,and her/his age is %d' %(name,age))

    # 4、删除操作
    def deleteData(self):
        sql_delete = 'delete from student where name = %(name)s and age = %(age)s'
        data = {'name': 'shiki', 'age': 25}
        cursor.execute(sql_delete, data)

    #关闭连接
    def closeConction(self):
        cursor.close()
        cnn.close()

if __name__ == '__main__':
    functionLibrary=conMysql()
    try:
        functionLibrary.creatTable()
        functionLibrary.insertData()
        functionLibrary.deleteData()
        functionLibrary.query()
    except mysql.connector.Error as e:
        print('数据库错误'.format(e))
    finally:
        functionLibrary.closeConction()
