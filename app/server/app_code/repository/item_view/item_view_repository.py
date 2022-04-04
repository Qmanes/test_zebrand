from app_code.model.ItemView_Model import ItemView
from app_code.model.Item_Model import Item
from app_code.model.Brand_Model import Brand
from app_code.repository.mariadb.Execute import Execute

TABLE = "items_view"
EXECUTE = Execute(TABLE, ItemView, "Item View")


def save(item_view):

    EXECUTE.save(item_view)

def all():

    sql = """
        SELECT

            item.uid as item_id,
            item.name as item_name,
            brand.name as brand_name,
            itemview.datetime as itemview_datetime,
            itemview.uid as itemview_id

        FROM

            items_view as itemview

        INNER JOIN

            items AS item

        ON

            (itemview.item_id = item.uid)

        INNER JOIN

            brands AS brand

        ON
            (item.brand_id = brand.uid)
    """

    response_list = EXECUTE.only_sql(sql)

    return list(map(lambda response: set_item_view(response), response_list))


def set_item_view(response):

    item_view = ItemView(uid = response[4], item_id = response[0], datetime= str(response[3]))

    item_view.set_item(response[1])

    item_view.set_brand(response[2])

    return item_view