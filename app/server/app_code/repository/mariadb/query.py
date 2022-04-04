from app_code.repository.mariadb.Database import Connection

def execute_insert(table, fields, values, value_length):
    
    fields = str(fields).replace("'","")

    conn = Connection()

    sql = "INSERT INTO {table} {fields} VALUES {value_length}".format(table = table, fields = fields, value_length = value_length)
    
    conn.execute(sql, values)

def execute_find_id(table, value, fields = "*"):

    conn = Connection()

    sql = "SELECT {fields} FROM {table} WHERE status != 'deleted' and uid = '{value}'".format(fields = fields, table = table, value = value)

    return conn.get_first(sql)

def execute_find_one(table, condition, fields = "*"):

    conn = Connection()

    sql = "SELECT {fields} FROM {table} WHERE status != 'deleted' and {condition}".format(fields = fields, table = table, condition = condition)

    return conn.get_first(sql)

def execute_all(table, fields = "*", condition = None):

    conn = Connection()

    sql = "SELECT {fields} FROM {table} where status != 'deleted' {condition} ".format(fields = fields, table = table, condition = condition if condition else "")

    return conn.get_all(sql)

def execute_setup(sql):

    conn = Connection()

    conn.execute(sql)


def execute_sql(sql):

    conn = Connection()

    return conn.get_all(sql)

def execute_update(table, data,  condition):

    conn = Connection()

    sql= """UPDATE 
                {table} 
            SET 
                {data} 
            WHERE 
                {condition}
        """.format(table = table, data = data, condition = condition)
    
    conn.execute(sql)

def execute_delete(table, condition):

    sql= """UPDATE 
                {table} 
            SET 
                status = "deleted" 
            WHERE 
                {condition}""".format(table = table, condition = condition)

    conn = Connection()

    conn.execute(sql)
