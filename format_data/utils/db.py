import psycopg2, datetime, sys
from utils.func import get_config

config = get_config()

class Database:
    def __init__(self):
        self.con = psycopg2.connect(
                                    database = config['configDB']['database'],
                                    user = config['configDB']['user'],
                                    password = config['configDB']['password'],
                                    host = config['configDB']['host'],
                                    port = config['configDB']['port']
                                    )

        self.cur = self.con.cursor()


    def insert(self, tableName, *values):
        self.cur.execute("INSERT INTO {0} VALUES {1};".format(tableName, values))
        self.con.commit()
        return True

    # additional functions for db

    # def get_value(self, tableName, argument, selector, value):
    #     self.cur.execute("SELECT {1} from {0} where {2} = \'{3}\';".format(tableName, argument, selector, value))
    #     self.con.commit()
    #     return self.cur.fetchall()[0][0]
    #
    # def update(self, tableName, argument, selector, newValue, findValue):
    #     self.cur.execute("UPDATE {0} set {1} = \'{3}\' where {2} = \'{4}\';".format(tableName, argument, selector, newValue, findValue))
    #     self.con.commit()
    #     return True
    #
    # def remove(self, tableName, selector, value):
    #     self.cur.execute("DELETE from {0} where {1} = \'{2}\';".format(tableName, selector, value))
    #     self.con.commit()
    #     return True
    #
    # def get_all(self, tableName):
    #     self.cur.execute("SELECT * from {0};".format(tableName))
    #     self.con.commit()
    #     return self.cur.fetchall()
    #
    #
    def custom_command(self, command):
        self.cur.execute(command)
        self.con.commit()
        return self.cur.fetchall()
