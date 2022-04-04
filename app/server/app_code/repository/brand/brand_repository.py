from app_code.repository.mariadb.Execute import Execute
from app_code.model.Brand_Model import Brand

TABLE = "brands"

EXECUTE = Execute(TABLE, Brand, "Brand")

def find_or_fail(brand_id):

   return EXECUTE.find_or_fail(brand_id)

def find_by_name(brand_name):

    condition = "name ='{}'".format(brand_name)

    return EXECUTE.find_one(condition)

def find_by_name_and_uid(brand_name, brand_uid):

    condition = """ name ='{}' AND
                    uid != '{}'
                """.format(brand_name, brand_uid)

    return EXECUTE.find_one(condition)

def all():

    return EXECUTE.all()

def save(brand):

    return EXECUTE.save(brand)

def update(brand):

    data = "name = '{}'".format(brand.name)

    condition = "uid = '{}'".format(brand.get_uid())
    
    return EXECUTE.update(brand.get_uid(), data, condition)


def delete(brand_id):

    return EXECUTE.delete(brand_id)
