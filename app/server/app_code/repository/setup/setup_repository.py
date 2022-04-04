from app_code.repository.mariadb.Execute import Execute

EXECUTE = Execute()

def get_table_exist(table):

    sql = """select table_name FROM information_schema.tables WHERE table_schema = 'zebrands' AND table_name = '{table}';""".format(table = table)

    return EXECUTE.only_sql(sql)

def create_users():

    if not get_table_exist("users"):

        sql = """
                CREATE TABLE zebrands.users (
                uid varchar(50) COLLATE utf8_spanish2_ci NOT NULL,
                fullname varchar(50) CHARACTER SET utf8 COLLATE utf8_spanish2_ci NOT NULL,
                email varchar(50) CHARACTER SET utf8 COLLATE utf8_spanish2_ci NOT NULL,
                type varchar(10) CHARACTER SET utf8 COLLATE utf8_spanish2_ci NOT NULL,
                status varchar(10) CHARACTER SET utf8 COLLATE utf8_spanish2_ci NOT NULL,
                password varchar(100) CHARACTER SET utf8 COLLATE utf8_spanish2_ci NOT NULL,
                PRIMARY KEY (uid)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish2_ci
        """

        EXECUTE.only_setup(sql)

        return True
    
    return False

def create_items():
    if not get_table_exist("items"):
    
        sql = """
        
            
            CREATE TABLE zebrands.items (
                uid varchar(50) COLLATE utf8_spanish2_ci NOT NULL,
                sku varchar(20) COLLATE utf8_spanish2_ci NOT NULL,
                name varchar(25) COLLATE utf8_spanish2_ci NOT NULL,
                price float NOT NULL,
                brand_id varchar(50) COLLATE utf8_spanish2_ci NOT NULL,
                status varchar(10) COLLATE utf8_spanish2_ci NOT NULL,
                PRIMARY KEY (uid),
                KEY item_brand (brand_id)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish2_ci
            
        """
        EXECUTE.only_setup(sql)

def create_brands():
    if not get_table_exist("brands"):

        sql = """
            
            CREATE TABLE zebrands.brands (
            uid varchar(50) COLLATE utf8_spanish2_ci NOT NULL,
            name varchar(20) COLLATE utf8_spanish2_ci NOT NULL,
            status varchar(10) COLLATE utf8_spanish2_ci NOT NULL,
            PRIMARY KEY (uid)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish2_ci

            
        """
        EXECUTE.only_setup(sql)

def create_items_view():

    if not get_table_exist("items_view"):

        sql = """
            
            CREATE TABLE zebrands.items_view (
            uid varchar(50) COLLATE utf8_spanish2_ci NOT NULL,
            item_id varchar(50) COLLATE utf8_spanish2_ci NOT NULL,
            datetime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
            status varchar(50) COLLATE utf8_spanish2_ci NOT NULL,
            PRIMARY KEY (uid)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish2_ci
            
        """
        EXECUTE.only_setup(sql)

def create_notifications():

    if not get_table_exist("notifications"):

        sql = """
            CREATE TABLE zebrands.notifications (
            uid varchar(50) COLLATE utf8_spanish2_ci NOT NULL,
            user_from varchar(50) COLLATE utf8_spanish2_ci NOT NULL,
            user_to varchar(50) COLLATE utf8_spanish2_ci NOT NULL,
            title varchar(50) COLLATE utf8_spanish2_ci NOT NULL,
            msg longtext COLLATE utf8_spanish2_ci NOT NULL,
            datetime datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
            status varchar(10) COLLATE utf8_spanish2_ci NOT NULL,
            PRIMARY KEY (uid)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish2_ci
        """
        EXECUTE.only_setup(sql)