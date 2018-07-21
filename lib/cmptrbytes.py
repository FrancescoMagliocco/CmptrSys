import os
import sys
import json

from cmptrsyssettings import CmptrBytesSettings

class BytesSys:

    bytes_settings_file = ''

    bytes_settings = CmptrBytesSettings

    def Init(self, main_script_settings):
#        Parent.Log(ScriptName, 'Init BytesSys')
        directory = os.path.join(os.path.dirname(__file__), 'settings')
        if not os.path.exists(directory):
            os.makedirs(directory)

        bytes_settings_file = os.path.join(directory, 'cmptrsysbytessettings.json')
#        bytes_settings = CmptrBytesSettings(bytes_settings_file)
#        main_script_settings.commands['!test'] = self.get_bytes

    def get_bytes(self, data):
#        Parent.Log(ScriptName, 'getBytes')
        return self.bytes_settings.get_bytes(data.User)

