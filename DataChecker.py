import logging


class DataChecker:
    def __init__(self, rec, templates, db_helper):
        self.dictionary = rec.getFieldsDict().keys()
        self.rec = rec
        self.db_helper = db_helper
        self.logger = logging.getLogger('[COLIOT]')

        self.objects = templates

        if self.controlFields(0, self.dictionary) == 0:
            self.logger.info("Template is not defined")

    # Recursive control fields for every object
    def controlFields(self, index, dictionary):
        if len(dictionary) == len(self.objects[index].getFileds()):
            conformity = 0
            for i, dict in enumerate(dictionary):
                for o in self.objects[index].getFileds():
                    if o == dict:
                        conformity = conformity + 1
                if i == len(dictionary) - 1:
                    if conformity == len(dictionary):
                        template = self.objects[index]
                        template.init(self.getRecord(self.rec.strRecord()))
                        template.save(self.db_helper)
                        return 1
                    else:
                        return self.controlFields(index + 1, dictionary)
        else:
            if self.objects[index] is self.objects[-1]:
                return 0
            return self.controlFields(index + 1, dictionary)

    def getRecord(self, record):
        if not record:
            return 0
        list = {}
        record = record.replace(" ", "")
        record = record.replace("UnirecTime(", "")
        record = record.split(',')
        for rec in record:
            if '=' in rec:
                list[rec.split('=')[0]] = rec.split('=')[1]
        return list