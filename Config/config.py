import pymysql.cursors
from datetime import date

prodUserMysql = 'root'
prodPassMysql = 'root.'
prodDbMysql = ''

devUserMysql = 'root'
devPassMysql = 'root'
devDbMysql = ''


def dbCnn():
    isProd = False
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                             user= prodUserMysql if isProd == True else devUserMysql ,
                             password= prodPassMysql if isProd == True else  devPassMysql,
                             db= prodDbMysql if isProd == True else devDbMysql,
                             charset='utf8mb4',
                             port=8889,
                             cursorclass=pymysql.cursors.DictCursor)
    return connection

