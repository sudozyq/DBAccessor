from Accessor import Accessor


class PostgreSQLAccessor(Accessor):
    '''
    summary:
        This is a class for connect PostgreSQL

    include method:
        getConnection(): A method for connect the database can print database version and connected time point
        reconnect(): A method to reconnect database
        closeConnection(): A method for close the connection

    Attributes:
        host: A string of your database's ip
        user: A string of your user name
        password: A string of your password
        database: A string of your database's name
        port: An integer of database's port number
        connectTime: A number of database connection time point
        timezone: A string of your timezone
        reconnectTimes: Set An interger of reconnect times
    '''
    def __init__(self):
        Accessor.__init__(self, psycopg2)
        config = configparser.ConfigParser()
        os.chdir("E:\python_code\py_sql")
        config.read("pg_ident.conf")
        self.host = config.get("db", "db_host")
        self.user = config.get("db", "db_user")
        self.password = config.get("db", "db_password")
        self.database = config.get("db", "db_database")
        self.port = config.getint("db", "db_port")
        self.connectTime = config.getint("db", "db_connectTime")
        self.timezone = pytz.timezone(config.get("db", "db_timeZone"))
        self.reconnectTimes = config.getint("db", "db_reconnectTimes")
        self.getConnection()

    def getConnection(self):
        """ connect the database """
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
            )

            if self.conn:
                # use cursor() method to get cursor of operation
                cursor = self.conn.cursor()
                # use execute() method to get version-number database
                cursor.execute("SELECT VERSION()")
                # use fetchone() method get one data
                data = cursor.fetchone()
                # get a time point
                self.connectTime = time.time()
                # sift to date and clock
                siftTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.connectTime))
                print("Successful connection at : %s" % siftTime)
                print("Database version : %s " % data)
                # if connect success return TRUE
                return True

        except psycopg2.Error as error:
            print('Error: %s' % error)
            self.reconnect()
            # if connect fail return FALSE
            return False

    def reconnect(self):
        """reconnect the database"""
        counter = 1

        while counter <= self.reconnectTimes:
            print("\nReconnect %d times..." % (counter))
            counter += 1
            try:
                self.reconn = psycopg2.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database,
                    port=self.port,
                )

                if self.reconn:
                    cursor = self.reconn.cursor()
                    cursor.execute("SELECT "
                                   "VERSION()")
                    data = cursor.fetchone()
                    self.connectTime = time.time()
                    siftTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.connectTime))
                    print("Successful connection at : %s" % siftTime)
                    print("Database version : %s " % data)
                    break

            except psycopg2.Error as error:
                print('Error: %s' % error)
                # sleep 5s before next reconnect
                time.sleep(5)
                return False

    def closeConnection(self):
        """close the database"""
        try:

            if self.conn:
                # close
                self.conn.close()
                return True

        except psycopg2.Error as error:
            print('Error: %s' % error)
            return False