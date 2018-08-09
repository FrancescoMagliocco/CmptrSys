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
            self.kb_enable = True
            self.kb_command = '!kilobytes'
            self.kb_aliases = ['!kilobyte', '!kb']

            self.mb_enable = True
            self.mb_command = '!megabytes'
            self.mb_aliases = ['!megabyte', '!mb']

            self.gb_enable = True
            self.gb_command = '!gigabytes'
            self.gb_aliases = ['!gigabyte', '!gb']

            self.tb_enable = True
            self.tb_command = '!terabytes'
            self.tb_aliases = ['!terabyte', '!tb']

            self.pb_enable = True
            self.pb_command = '!petabytes'
            self.pb_aliases = ['!petabyte', '!pb']


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
