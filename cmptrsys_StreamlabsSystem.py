import os
import sys
import json
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

import clr
clr.AddReference('IronPython.SQLite.dll')
clr.AddReference('IronPython.Modules.dll')

from cmptrsyssettings import Settings
from cmptrsysbase import CommandBase
from bytessys import KiloByte, MegaByte, GigaByte, TeraByte

ScriptName = 'CmptrSys'
Website = 'https://Github.com/FrancescoMagliocco/CmptrSys'
Description = 'TBA'
Creator = 'FrancescoMagliocco/Cmptr/CmptrGmr/CmptrGmrLIVE'
Version = '0.0.0.1'

def Init():
    directory = os.path.join(os.path.dirname(__file__), 'settings')
    if not os.path.exists(directory):
        os.makedirs(directory)

    global settings_file
    settings_file = os.path.join(__file__, 'settings.json')
    global settings
    settings = Settings(settings_file)
    # TODO: Implement the enabling of each metric
    KiloByte(settings)
    MegaByte(settings)
    GigaByte(settings)
    TeraByte(settings)
    # FIXME: 'pb_command' is not found
#    PetaByte(settings)

def Execute(data):
    if (data.IsChatMessage()
            and CommandBase.is_command(data.GetParam(0).lower())):
        cmd = CommandBase.get_command(data.GetParam(0).lower())

        if (Parent.HasPermission(
                data.User, cmd.permission, 'TODO:  Add Permission Info')
                and not Parent.IsOnCooldown(ScriptName, cmd.command)):
            cmd.execute(Parent, data)

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

def Unload():
    Parent.Log(ScriptName, 'Unloaded!')

def ScriptToggled(state):
    Parent.Log(ScriptName, 'Toggled: {0}'.format(str(state)))
