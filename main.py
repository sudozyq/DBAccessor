


def main():
    obj = MySQLAccessor.MySQLAccessor()
    obj.getTimeZone()
    obj.readConnectedTime()
    # obj.setTimeZone()
    # obj.createDatabase("BA")
    obj.dropDatabase("BA2")
    # obj2 = PostgreSQLAccessor.PostgreSQLAccessor()
    # obj.getConnection()
    # obj.createDatabase('BAtable5')
    # obj.sqlOperation()
    # obj.searchTable('EMPLOYEE2')
    # obj.getTimeZone()
    # obj.setTimeZone()
    # obj.getTimeZone()
    # obj.printMember()
    # obj.createTable()
    # obj.insertIntoTable('EMPLOYEE')
    # time.sleep(5)
    # obj.createDatabase('createTT5')
    # obj.readConnectedTime()
    # rest = obj.get_one()
    # print(rest)
    # obj.add_one()
    # print(rest)
    # rest = obj.get_more_by_page(1, 5)
    # for item in rest:
    #     print(item)
    #     print('-----------------')
    # obj.add_one()


if __name__ == '__main__':
    main()
