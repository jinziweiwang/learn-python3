#链接mysql
import pymysql

#定义数据源
DATABASE={
    'host':'127.0.0.1',
    'database':'yyj',
    'user':'root',
    'password':'yyj2020'

}
try:
    #连接数据库
    db=pymysql.connect('localhost','root','yyj2020','yyj')
    #开启游标
    cursor=db.cursor()
    sql='select * from t_user'
    sql_i = "insert into `t_user` values ('202000003','zhiyinying','0');"

    #执行游标sql
    cursor.execute(sql)
    cursor.execute(sql_i)
    db.commit()
    #获取结果集
    results =cursor.fetchall()
    #打印返回行
    for row in results:
        print(row)
except Exception as e:
    db.rollback()
    print(e)

'''
sql_i ="insert into `t_user` values ('202000003','zhiyinying','0');"

cursor.execute(sql_i)
db.commit()
'''

