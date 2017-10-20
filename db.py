# coding=utf8
import psycopg2
import logging

# HOST = '47.93.5.189'
# HOST = 'localhost'
HOST = '172.16.10.133'
PORT = '5432'
USER = 'sneaky'
PASSWORD = '77WN88wwc'
DATABASE = 'sneaky'
logging.basicConfig(filename='db.log', level=logging.DEBUG, filemode='a')
class BaseDB(object):

    def __init__(self, database='sneaky', port='5432'):
        self.conn = psycopg2.connect(database=database, password=PASSWORD, user=USER, host=HOST, port=port)
        self.cur = self.conn.cursor()

    def query(self, table=None, columns_values=None,update_sql=None):
        # 插入操作
        if table and columns_values:
            try:
                sql = 'INSERT INTO  %s  %s  ' % (table, columns_values)
                self.cur.execute(sql)
                self.commit()
            except Exception as e:
                self.commit()
                if 'duplicate key' in str(e) and update_sql:
                    self.update(table, update_sql)
                logging.error(str(e))

    def update(self,table, update_sql=None):
        # 更新操作
        if update_sql:
            try:
                self.cur.execute('update %s set %s' % (table, update_sql))
                self.commit()
            except Exception as e:
                self.commit()
        pass

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()
