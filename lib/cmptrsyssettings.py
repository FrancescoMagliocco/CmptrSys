import os
import codecs
import json

class Settings(object):
    def __init__(self, settings_file=None):
        try:
            with codecs.open(
                    settings_file, encoding='utf-8-sig', mode='r') as f:
                self.__dict__ = json.load(f, encoding='utf-8')
        except:
            self.commands = [['!kilobytes', '!kilobyte', '!kb'],
                             ['!megabytes', '!megabyte', '!mb'],
                             ['!gigabytes', '!gigabyte', '!gb'],
                             ['!terabytes', '!terabyte', '!tb'],
                             ['!petabytes', '!petabyte', '!pb']]

    def Reload(self, json_data):
        self.__dict__ = json.loads(json_data, encoding='utf-8')

    def Save(self, settings_file):
        try:
            with codecs.open(
                    settings_file, encoding='utf-8-sig', mode='w+') as f:
                json.dump(self.__dict__, f, encoding='utf-8')

            with codecs.open(settings_file.replace('json', 'js'),
                             encoding='utf-8-sig',
                             mode='w+') as f:
                f.write('var settings = {0};'.format(
                    json.dumps(self.__dict__, encoding='utf-8')))
        except:
            pass
#            Parent.Log(ScriptName, 'Failed to save settings file')
