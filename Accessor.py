class Accessor(object):
    '''
    summary:
        This is a class for operate database

    include method:
        readConnectTime(): A method to read the time span of connection
        getTimezone(): A method to get the now time zone
        setTimezone():A method to set new timezone
        createDatabase():A method to create a database
        dropDatabase():A method to delete the database
        dropTable():A method to drop the table
        addKey():A method to add key for table
        updateTable():A method to update the selected table
        readOneColumn():A method to read one column
        deleteData():A method to delete a element
        sqlOperation():A method to receive a sql sentence and execute
        searchTable():A method to determine if a table exists in a database
        printMember(): A method to print all method and member variables

    Attributes:
        databaseType: A string of database type include MySQL and PostgreSQL
        timezone: A string of your timezone
    '''
    def __init__(self, databaseType):
        self.databaseType = databaseType

    def readConnectedTime(self):
        """read the time span of connection"""
        timeSpan = time.time() - self.connectTime
        print("The time span of the database connection is: %ss" % timeSpan)

    def getTimeZone(self):
        """get the time zone"""
        print(datetime.datetime.now(self.timezone))

    def setTimeZone(self):
        """set the time zone"""
        self.timezone = pytz.timezone(input("input the new area of time zone(like Asia/Shanghai):"))

    def createDatabase(self, databaseName):
        """create a database

           Args:
               databaseName: the name of database wait for create"""

        try:
            # use cursor() method to get cursor of operation
            cursor = self.conn.cursor()
            # use _query() method to get version-number database
            cursor._query('CREATE DATABASE %s' % databaseName)
            # commit the operation
            self.conn.commit()
            print("create a new database %s successful" % databaseName)
            return True

        except self.databaseType.Error as error:
            # if there is error rollback the operation
            self.conn.rollback()
            print('Error: %s' % error)
            choice = input("If you want to rename or drop the database or do nothing?(r/d/n):")

            if choice == 'r':
                # rename the database
                rename = input("Input the rename:")
                self.createDatabase(rename)

            elif choice == 'd':
                # delete the database
                self.dropDatabase(databaseName)

            else:
                # do nothing
                print("Nothing has been done.")

    def dropDatabase(self, databaseName):
        """delete the database

           Args:
               databaseName: the name of database wait for delete"""
        try:
            sqlSentence = "DROP DATABASE %s" % (databaseName,)
            cursor = self.conn.cursor()
            cursor.execute(sqlSentence)
            self.conn.commit()
            print("Drop successful!")
            return True

        except self.databaseType.Error as error:
            # if there is error rollback the operation
            self.conn.rollback()
            print('Error: %s' % error)

    def dropTable(self, tableName):
        """drop the table

           Args:
               tableName: the name of table wait for delete"""
        try:
            sqlSentence = "DROP TABLE %s" % (tableName,)
            cursor = self.conn.cursor()
            cursor.execute(sqlSentence)
            self.conn.commit()
            print("Drop successful!")
            return True

        except self.databaseType.Error as error:
            # if there is error rollback the operation
            self.conn.rollback()
            print('Error: %s' % error)

    def addKey(self, tableName, key):
        """add the key in table

           Args:
               tableName: A String of tableName waiting for operate
               key: A string of key waiting for add"""
        try:
            sqlSentence = "alter table %s add column %s Decimal(16, 6) default \'0\'"% (tableName, key)
            cursor = self.conn.cursor()
            cursor.execute(sqlSentence)
            self.conn.commit()
            print("Key add success!")
            return True

        except self.databaseType.Error as error:
            # if there is error rollback the operation
            self.conn.rollback()
            print('Error: %s' % error)
            return False

    def updateTable(self, operateTable, afterTable, regular):
        """update the selected table

           Args:
               operateTable: A String of tableName waiting for operate
               afterTable: A string of tablename after operate
               regular: A string of selection"""
        try:
            sqlSentence = "updata %s set %s where %s"% (operateTable, afterTable, regular)
            cursor = self.conn.cursor()
            cursor.execute(sqlSentence)
            self.conn.commit()
            print("updata success!")
            return True

        except self.databaseType.Error as error:
            # if there is error rollback the operation
            self.conn.rollback()
            print('Error: %s' % error)
            return False

    def readOneColumn(self, columnName, tableName):
        """read one column

           Args:
               columnName: A String of columnName waiting for read
               tableName: A string of tablename waiting for read"""
        try:
            sqlSentence = "SELECT %s FROM %s"% (columnName, tableName)
            cursor = self.conn.cursor()
            cursor.execute(sqlSentence)
            self.conn.commit()
            return True

        except self.databaseType.Error as error:
            # if there is error rollback the operation
            self.conn.rollback()
            print('Error: %s' % error)
            return False

    def deleteData(self, tableName, element):
        """delete a element

           Args:
               tableName: A String of tableName waiting for delete
               element: A string of element waiting for delete"""
        try:
            sqlSentence = "delete from %s where %s"% (tableName, element)
            cursor = self.conn.cursor()
            cursor.execute(sqlSentence)
            self.conn.commit()
            return True

        except self.databaseType.Error as error:
            # if there is error rollback the operation
            self.conn.rollback()
            print('Error: %s' % error)
            return False

    def sqlOperation(self):
        """input a sql sentence and execute"""
        try:
            sqlSentence = input("input the createSentence: ")
            cursor = self.conn.cursor()
            cursor.execute(sqlSentence)
            self.conn.commit()
            print("success execute")
            return True

        except self.databaseType.Error as error:
            # if there is error rollback the operation
            self.conn.rollback()
            print('Error: %s' % error)
            return False

    def searchTable(self, tableName):
        """Determine if a table exists in a database

           Args:
               tableName: the name of table wait for search"""
        try:
            sqlSentence = "select * from %s "% (tableName,)
            cursor = self.conn.cursor()
            cursor.execute(sqlSentence)
            self.conn.commit()
            print("The table exists in database!")
            return True

        except self.databaseType.Error as error:
            # if there is error rollback the operation
            self.conn.rollback()
            print('Error: %s' % error)
            return False

    def printMember(self):
        """print all method and member variables"""
        print(Accessor.__doc__)
