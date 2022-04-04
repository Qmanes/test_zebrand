import mariadb

class Connection():

    def __init__(self):

        self.config = {'host': 'mysqldb','port': 3306,'user': 'root','password': 'wRacgZTnJgYZTr4NfM9PA3m4289MXC4GCa6UJdDNLeYALKZbDF','database': 'zebrands'}
        self.connection = mariadb.connect(**self.config)
        self.cursor = self.connection.cursor()

    def execute_all(self, sql):

        self.execute(sql)
        
        result = self.cursor.fetchall()

        self.close()

        return result
        
    def execute(self, sql, values = None):

        self.cursor.execute(sql, values)

        self.commit()
        
    def commit(self):

        self.connection.commit()

    def close(self):

        self.cursor.close()
        self.connection.close()

    def get_first(self, sql):

        self.cursor.execute(sql)

        return self.cursor.fetchone()

    def get_all(self, sql):

        self.cursor.execute(sql)

        return self.cursor.fetchall()

    def execute_many(self, sql, data):

        self.cursor.executemany(sql, data)

