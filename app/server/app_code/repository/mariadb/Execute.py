from app_code.repository.mariadb.query import execute_insert, execute_find_id, execute_all , execute_update, execute_delete, execute_find_one, execute_sql, execute_setup
from app_code.exception.basic_exception import NotFoundException
class Execute():

    def __init__(self, table = None, obj = None, title = None):

        self.table = table

        self.obj = obj

        self.title = title

    def find_or_fail(self, data_id):

        result = execute_find_id(table=self.table, value=data_id)

        if result:

            return self.obj(*result)
        
        raise NotFoundException(self.title)

    def find_one(self, condition):

        result = execute_find_one(table=self.table, condition=condition)

        return self.obj(*result) if result else None

    def find_one_result(self, condition):

        return execute_find_one(table=self.table, condition=condition)

    def find_count(self, condition):

        fields = "count(uid)"
        return execute_find_one(table=self.table, condition=condition, fields = fields)


    def all(self, condition = None):

        list_all = execute_all(self.table, condition = condition)

        return list(map(lambda obj: self.obj(*obj), list_all))

    def only_sql(self, sql):

        return execute_sql(sql)

    def only_setup(self, sql):

        return execute_setup(sql)

    def save(self, obj):

        fields = obj.get_tuple_fields()
        
        values = obj.get_tuple_values()

        value_length = str(tuple(['?' for value in fields]))

        value_length = value_length.replace("'","")
        
        execute_insert(self.table, fields, values, value_length)
        
        return self.find_or_fail(obj.get_uid())

    def update(self,data_id, data, condition):

        execute_update(table=self.table, data = data, condition = condition)

        return self.find_or_fail(data_id)

    def delete(self, data_id):

        condition = "uid = '{}'".format(data_id)

        execute_delete(table=self.table, condition = condition)