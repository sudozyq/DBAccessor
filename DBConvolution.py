from CSVLoader import CSVLoader


class DBConvolution(CSVLoader):
    '''
    summary:
        This is a class for operate database

    include method:
        conv(): The vector consisting of patternVector and field Name column
                in tableName table is convoluted, and the result vector from
                convolution is stored in resultFieldName in tableName table.

    Attributes:
        databaseType: A string of database type include MySQL and PostgreSQL
    '''
    def __init__(self, databaseType):
        CSVLoader.__init__(self, databaseType)

    def conv(self, patternVector, tableName, fieldName, resultFieldName, primaryKey):
        """The vector consisting of patternVector and field Name column
        in tableName table is convoluted, and the result vector from
        convolution is stored in resultFieldName in tableName table.

           Args:
               patternVector: The vector ready to do convolution
               tableName: The table whose column waiting for convolute
               fieldName: A column waiting for convolute
               resultFieldName: A Vector in tableName store the result of convolution
               primaryKey: premaryLKey of table """
        convValue = []
        value = self.readOneColumn(fieldName, tableName)
        convData = self.readOneColumn(primaryKey, tableName)

        for i in convData:
            i = str(i)[1:-2]
            convValue.append(i)

        self.addKey(tableName, resultFieldName)
        patternlength = len(patternVector)
        valueLength = len(value)

        for i in range(valueLength):
            if i < patternlength:
                convSum = numpy.dot(patternVector[:i + 1], value[:i + 1])
                convAvg = float(convSum) / (i + 1)

            else:
                convSum = numpy.dot(patternVector[0:patternlength + 1], value[i - patternVector + 1:i + 1])
                convAvg = float(convSum) / patternlength

            afterTable = "%s = %f" % (resultFieldName, convAvg)
            regular = "%s = %f" % (primaryKey, convValue[i])

            self.updateTable(tableName, afterTable, regular)
