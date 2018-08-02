import os
import sys
import json
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

import clr
clr.AddReference('IronPython.SQLite.dll')
clr.AddReference('IronPython.Modules.dll')

from cmptrsyssettings import Settings

ScriptName = 'CmptrSys'
Website = 'https://Github.com/FrancescoMagliocco/CmptrSys'
Description = 'TBA'
Creator = 'FrancescoMagliocco/Cmptr/CmptrGmr/CmptrGmrLIVE'
Version = '0.0.0.1'

global settings_file
settings_file = ''

global settings
settings = Settings()

def Init():
    directory = os.path.join(os.path.dirname(__file__), 'settings')
    if not os.path.exists(directory):
        os.makedirs(directory)

    settings_file = os.path.join(directory, 'settings.json')
    settings = Settings(settings_file)

def is_command(command):
    Parent.Log(ScriptName, str(settings.commands))
    Parent.Log(ScriptName, str(settings.aliases))
    return any(command in k or command in v for k, v in settings.aliases)

def Execute(data):
    if (data.IsChatMessage()
            and is_command(data.GetParam(0).lower())):
        Parent.Log(ScriptName, '{0} is a command.'.format(data.GetParam(0)))
#            and not Parent.IsOnCooldown(ScriptName, script_settings.command)
#            and Parent.HasPermission(
#                data.User, script_settings.permission, script_settings.info)):
#        Parent.SendStreamMessage(script_settings.commands[data.GetParam(0).lower()](data))
#        Parent.AddCooldown(
#            ScriptName, script_settings.command, script_settings.cooldown)

def Tick():
    pass

def Parse(parse_string, userid, username, targetid, target_name, message):
    if '$myparameter' in parse_string:
        return parse_string.replace('$myparameter', 'null')

    return parse_string

def ReloadSettings(json_data):
    settings.__dict__ = json.loads(json_data)
    settings.Save(settings_file)

def Unload():
    Parent.Log(ScriptName, 'Unloaded!')
    settings.Save(settings_file)

def ScriptToggled(state):
    Parent.Log(ScriptName, str(state))
