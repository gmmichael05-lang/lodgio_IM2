import pymysql

pymysql.install_as_MySQLdb()

# This tells Django to skip its strict version check for mysqlclient
import MySQLdb
MySQLdb.version_info = (2, 2, 1)