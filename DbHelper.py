import sqlite3
import logging
import configparser


class DbHelper:
    def __init__(self):
        self.logger = logging.getLogger('[COLIOT]')
        self.connection = None
        self.cursor = None
        self.connected = False

        # DB_CONFIG
        self.database = self.getConfig()
        self.timeout = None
        self.detect_types = None
        self.isolation_level = None
        self.check_same_thread = None
        self.factory = None
        self.cached_statements = None
        self.uri = None

    def getConfig(self):
        template = configparser.ConfigParser()
        template.optionxform = lambda option: option
        template.read('coliot.conf')
        template.sections()

        # Control config
        if not 'SQLITE' in template:
            self.logger.error("SQLite database not found!")
            return None
        database = str(template['SQLITE']['database'])
        self.logger.info("DATABASE LOADED " + database)
        return database

    def connect(self):
        # Connect to database
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        self.connected = True

    def insert(self, table, args):
        # Insert to database
        values = ''

        for arg in args:
            values = values + "%s" % arg.getValue()
            if not arg is args[-1]:
                values = values + ','

        try:
            with self.connection:
                self.cursor.execute("INSERT INTO " + table + " VALUES (" + values + ")")
                self.connection.commit()
                self.logger.info("SAVE")
        except sqlite3.IntegrityError:
            self.logger.error("Couldn't create ROW to DB (INSERT) INSERT INTO " + table + " VALUES (" + values + ")")

    def createTable(self, table, args):
        attr = ''

        for arg in args:
            if arg.getName() == 'TIME':
                attr = attr + "%s %s" % ('TIME', 'DATETIME')
            elif arg.getName() == 'TIMESTAMP':
                attr = attr + "%s %s" % ('TIMESTAMP', 'DATETIME')
            else:
                attr = attr + "%s %s" % (arg.getName(), arg.getType())
            if not arg is args[-1]:
                attr = attr + ','

        try:
            with self.connection:
                self.cursor.execute("CREATE TABLE " + table + " (" + attr + ")")
                self.connection.commit()
                self.logger.info("CREATE TABLE " + table)
        except sqlite3.IntegrityError:
            self.logger.error("Couldn't create TABLE to DB (CREATE) CREATE TABLE " + table + " (" + attr + ")")

    def existTable(self, table):
        try:
            with self.connection:
                self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='" + table + "';")
        except sqlite3.IntegrityError:
            self.logger.error("Couldn't check TABLE in DB (TABLE) " + table)

        if self.cursor.fetchone() is None:
            return False
        else:
            return True

    def insertColiotTable(self, table, args):
        table_id = '1'
        self.cursor.execute('SELECT id FROM tables ORDER BY id DESC LIMIT 1;')
        row = self.cursor.fetchone()
        if row:
            table_id = str(row[0] + 1)

        self.cursor.execute(
            "INSERT INTO tables VALUES (strftime('%Y-%m-%d %H:%M:%f',datetime('now', 'localtime')),strftime('%Y-%m-%d %H:%M:%f',datetime('now', 'localtime'))," + table_id + ",'"
            + table + "',NULL,NULL,1,NULL,NULL,0,NULL,0,NULL,NULL,NULL,NULL,NULL,'[main].[" + table + "](id:" + table_id + ")',0,NULL,0,NULL)")
        self.connection.commit()
        self.logger.info("SAVE coliot tables")

        column_id = 1
        self.cursor.execute('SELECT id FROM table_columns ORDER BY id DESC LIMIT 1;')
        row = self.cursor.fetchone()
        if row:
            column_id = row[0] + 1

        value = ''
        type = ''
        for arg in args:
            if arg.getName() == 'TIME':
                value = 'TIME'
                type = 'DATETIME'
            else:
                value = arg.getName()
                type = arg.getType()

            self.cursor.execute(
                "INSERT INTO table_columns VALUES (strftime('%Y-%m-%d %H:%M:%f',datetime('now', 'localtime')),strftime('%Y-%m-%d %H:%M:%f',datetime('now', 'localtime')),"
                + str(
                    column_id) + "," + table_id + ",'" + value + "',0,1,'" + type + "',0,0,0,0,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL)")
            self.connection.commit()
            column_id = column_id + 1

        self.logger.info("SAVE coliot table_columns")

    def close(self):
        # Close database
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        self.connected = False

    def isConnected(self):
        return self.connected
