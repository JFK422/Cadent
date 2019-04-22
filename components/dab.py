import sqlite3

class DatabaseActions():

    def connect(self):
        global connection
        global cur
        connection = sqlite3.connect("./Data/conf/cadent.db")
        cur = connection.cursor()
        try:
            cur.execute("SELECT * FROM cnfLogic")
            cur.fetchall()
        except:
            DatabaseActions.createTables(self)
            DatabaseActions.createInitData(self)

    def close(self):
        connection.close()

    #createTables and createInitData are used to construct the games config database.
    #These methods may not be necessary but it makes creating the config db a lot easier than doing it manually
    def createTables(self):
        cnfLogic = "CREATE TABLE IF NOT EXISTS cnfLogic('prim' INTEGER PRIMARY KEY AUTOINCREMENT, 'name' TEXT, 'value' INTEGER);"
        cnfPerf = "CREATE TABLE IF NOT EXISTS cnfPerf('prim' INTEGER PRIMARY KEY AUTOINCREMENT, 'name' TEXT, 'value' INTEGER);"

        cur.execute(cnfLogic)
        cur.execute(cnfPerf)
        connection.commit()

    def createInitData(self):
        #Game Logic
        cur.execute("INSERT INTO cnfLogic (name, value) VALUES ('gameTime', 1);")
        connection.commit()

        #Performance settings
        cur.execute("INSERT INTO cnfPerf (name, value) VALUES ('fpsLimit', 120);")
        connection.commit()
    
    def insert(self):
        print("insert")
    
    def read(self):
        print("read")
    
    def update(self):
        print("update")

    def delete(self):
        print("delete")