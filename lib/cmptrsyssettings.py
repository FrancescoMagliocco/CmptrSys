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
            self.kb_message = '{0.UserName} has {1:f}KB'

            self.mb_enable = True
            self.mb_command = '!megabytes'
            self.mb_aliases = ['!megabyte', '!mb']
            self.mb_message = '{0.UserName} has {1:f}MB'

            self.gb_enable = True
            self.gb_command = '!gigabytes'
            self.gb_aliases = ['!gigabyte', '!gb']
            self.gb_message = '{0.UserName} has {1:f}GB'

            self.tb_enable = True
            self.tb_command = '!terabytes'
            self.tb_aliases = ['!terabyte', '!tb']
            self.tb_message = '{0.UserName} has {1:f}TB'

            self.pb_enable = True
            self.pb_command = '!petabytes'
            self.pb_aliases = ['!petabyte', '!pb']
            self.pb_message = '{0.UserName} has {1:f}PB'


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
                f.write('var settings = {0.UserName};'.format(
                    json.dumps(self.__dict__, encoding='utf-8')))
        except:
            pass
#            Parent.Log(ScriptName, 'Failed to save settings file')
