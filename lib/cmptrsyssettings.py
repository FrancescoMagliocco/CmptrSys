import os
import codecs
import json

from cmptrbytes import BytesSys

class CmptrSysScriptSettings(object):
    def __init__(self, settings_file=None):
        try:
            with codecs.open(
                    settings_file, encoding='utf-8-sig', mode='r') as f:
                self.__dict__ = json.load(f, encoding='utf-8')
        except:
            self.commands = {'!test': BytesSys.get_bytes}
            self.response = []
            self.cooldown = []
            self.perm = []
            self.info = []

    def Reload(self, json_data):
        self.__dict__ = json.loads(json_data, encoding='utf-8')

    def Save(self, settings_file):
        try:
            with codecs.open(
                    settings_file, encoding='utf-8-sig', mode='w+') as f:
                json.dump(self.__dict__, f, encoding='utf-8')
            with codecs.open(settings_file.replace('json', 'js'),
                             encoding='utf-8-sig', mode='w+') as f:
                f.write('var settings = {0}'.format(
                    json.dumps(self.__dict__, encoding='utf-8')))
        except:
            return

        return
#            Parent.Log(ScriptName, 'Failed to save settings file.')

class CmptrBytesSettings(object):
    def __init__(self, settings_file=None):
        try:
            with codecs.open(
                    settings_file, encoding='utf-8-sig', mode='r') as f:
                self.__dict__ = json.load(f, encoding='utf-8')
        except:
            self.commands = []
            self._users = {}
            self.response = []
            self.cooldown = []
            self.perm = []
            self.info = []

    def has_user(self, user):
        return user.ltrim('@') in self._users

    def add_user(self, user):
        self._users[user.ltrim('@')] = {
            'bytes': 0,
            'deaths': 0,
            'warnings': 0
        }

    def get_bytes(self, user):
        user = user.ltrim('@')
        if user in self._users:
            return '{0:s} has {1:d} bytes.'.format(user,
                                                   self._users[user]['bytes'])

        return '{0:s} can not be found.'.format(user)

    def Reload(self, json_data):
        self.__dict__ = json.loads(json_data, encoding='utf-8')

    def Save(self, settings_file):
        try:
            with codecs.open(
                    settings_file, encoding='utf-8-sig', mode='w+') as f:
                json.dump(self.__dict__, f, encoding='utf-8')
            with codecs.open(settings_file.replace('json', 'js'),
                             encoding='utf-8-sig', mode='w+') as f:
                f.write('var settings = {0}'.format(
                    json.dumps(self.__dict__, encoding='utf-8')))
        except:
            return
#            Parent.Log(ScriptName, 'Failed to save settings file.')
        return
