import configparser
import logging
from os import walk
from AttrObject import AttrObject
from Template import Template


class TemplateReader:
    def __init__(self):
        self.path = './templates/'
        self.logger = logging.getLogger('[COLIOT]')

    def getTml(self):
        listTemplate = []
        for dir in self.getListdir():
            listTemplate.append(self.readFile(dir))
        return listTemplate

    def getListdir(self):
        files = []
        for path, dirname, filenames in walk(self.path):
            for filename in filenames:
                if filename.endswith(".tml"):
                    files.append(filename)
            break
        return files

    def readFile(self, filename):
        template = configparser.ConfigParser()
        template.optionxform = lambda option: option
        template.read(self.path + filename)
        template.sections()

        # Control set value
        if not 'MAIN' in template:
            return 0
        if not 'FIELDS' in template:
            return 0

        if not template['MAIN'].getboolean('Enable'):
            return 0

        templateName = template['MAIN']['TemplateName']
        tableName = template['MAIN']['TableName']

        fmt = []
        fields = template['FIELDS']
        for name in fields:
            fmt.append(AttrObject(fields[name], name, None))

        self.logger.info("INIT Template " + templateName)

        return Template(templateName, tableName, fmt)
