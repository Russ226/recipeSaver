import pymysql


class DbReader:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Pen1992@',
                             db='recipedb')

    def writeToDb(self, sqlStatement, params):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sqlStatement, params)
                self.connection.commit()
                return

        except pymysql.Error as err:
            print(err)
            self.connection.rollback()
            return


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()