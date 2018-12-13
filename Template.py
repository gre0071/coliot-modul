class Template:
    def __init__(self, templateName, tableName, fmt):
        self.templateName = templateName
        self.tableName = tableName
        self.fmt = fmt

    def getFileds(self):
        fil = []
        for fmt in self.fmt:
            fil.append(fmt.name)
        return fil

    def init(self, rec):
        for fmt in self.fmt:
            fmt.setValue(rec[fmt.name])
        return 1

    def save(self, helper):
        if not helper.existTable(self.tableName):
            helper.createTable(self.tableName, self.fmt)
            if helper.existTable('tables'):
                helper.insertColiotTable(self.tableName)
        helper.insert(self.tableName, self.fmt)