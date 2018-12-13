
class AttrObject:
    def __init__(self, type, name, value):
        self.type = type
        self.name = name
        self.value = value

    def getType(self):
        return {
            int: "INTEGER",
            float: "REAL",
            str: "TEXT"
        }.get(self.type, self.type)

    def getName(self):
        if self.name == 'INDEX':
            return 'VAL_INDEX'
        return self.name

    def getValue(self):
        if self.name == 'TIME':
            return "strftime('%Y-%m-%d %H:%M:%S',datetime('" + str(self.value) + "', 'unixepoch'))"
        return self.value

    def setType(self):
        return self.type

    def setName(self):
        return self.name

    def setValue(self, value):
        self.value = value