import pymysql

pymysql.install_as_MySQLdb()

import MySQLdb
# Django requires mysqlclient 2.2.1 or newer. We are mocking the version here 
# because PyMySQL reports an older version by default.
MySQLdb.version_info = (2, 2, 1, "final", 0)
MySQLdb.__version__ = "2.2.1"
