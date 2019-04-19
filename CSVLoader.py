from MySQLAccessor import MySQLAccessor
from PostgreSQLAccessor import PostgreSQLAccessor


class CSVLoader(MySQLAccessor, PostgreSQLAccessor):
    '''
    summary:
        This is a class for operate CSV file

    include method:
        getConnection(): A method for connect the database can print database version and connected time point
        readCSV(): A method for read csv and insert into array
        InsertCSVIntoDatabase(): A method that can insert csv file into database
        loadCSV(): A method that can download the table of database to local

    Attributes:
        databaseType: A String of database type
    '''
    def __init__(self, databaseType):
        if(databaseType == 'MySQL'):
            # connect MySQL
            MySQLAccessor.__init__(self)

        elif(databaseType == 'PostgreSQL'):
            # connect PostgreSQL
            PostgreSQLAccessor.__init__(self)

    def readCSV(self, path):
        """read the csv data into the array

           Args:
               path: A String of the path of csv file which waiting for read"""
        i = 0
        csvData = numpy.array(pandas.read_csv(path, 'r'))
        csvList = csvData.tolist()
        value = [[] for index in range(len(csvList))]

        for j in csvList:
            j = str(j).split('[\'')[1].split('\']')
            spam = list(str(j[0]).split(','))
            value[i].append(spam[0])

            for k in range(1, len(spam)-1):
                value[i].append(float(spam[k]))

            value[i].append(int(spam[-1]))
            i = i + 1
        return value

    def InsertCSVIntoDatabase(self, tableName, path):
        """Insert CSV file into Database"""
        try:
            sqlSentence = "load data infile \'" + tableName + "\'\r\n" +\
                          "into table " + path + "\r\n" + \
                          "fields terminated by ','\r\n" + \
                          "optionally enclosed by '\"'\r\n" + \
                          "escaped by '\"'\r\n" + \
                          "lines terminated by '\\r\\n';"
            cursor = self.conn.cursor()
            cursor.execute(sqlSentence)
            self.conn.commit()
            return True

        except self.dataBaseType.Error as error:
            # if there is error rollback the operation
            self.conn.rollback()
            print('Error: %s' % error)
            return

    def loadCSV(self, tableName, path):
        """download the the table of database to local"""
        try:
            sqlSentence = "select * from " + tableName + "\r\n" + \
                          "into outfile \'" + path + "\'\r\n" + \
                          "fields terminated by ','\r\n" + \
                          "optionally enclosed by '\"'\r\n" + \
                          "escaped by '\"'\r\n" + \
                          "lines terminated by '\\r\\n';"
            cursor = self.conn.cursor()
            cursor.execute(sqlSentence)
            self.conn.commit()
            return True

        except self.dataBaseType.Error as error:
            # if there is error rollback the operation
            self.conn.rollback()
            print('Error: %s' % error)
            return

