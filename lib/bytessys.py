from cmptrsysbase import CommandBase

def _get_user(data):
    return data.GetParam(1) if data.GetParamCount() > 1 else data.User

def _get_username(data):
    return data.GetParam(1) if data.getParamCount() > 1 else data.UserNamme

# TODO: Have all these activated in one class to minimize code.
class KiloByte(CommandBase):
    def __init__(self, settings):
        CommandBase.__init__(self,
                             settings.kb_command,
                             settings.kb_aliases,
                             settings.kb_message)

    def execute(self, Parent, data):
        Parent.SendStreamMessage(self.message.format(
            _get_username(data),
            float(Parent.GetPoints(_get_user(data))) / 1024))

class MegaByte(CommandBase):
    def __init__(self, settings):
        CommandBase.__init__(self,
                             settings.mb_command,
                             settings.mb_aliases,
                             settings.mb_message)

    def execute(self, Parent, data):
        Parent.SendStreamMessage(self.message.format(
            _get_username(data),
            float(Parent.GetPoints(_get_user(data))) / 1048576))

class GigaByte(CommandBase):
    def __init__(self, settings):
        CommandBase.__init__(self,
                             settings.gb_command,
                             settings.gb_aliases,
                             settings.gb_message)

    def execute(self, Parent, data):
        Parent.SendStreamMessage(self.message.format(
            _get_username(data),
            float(Parent.GetPoints(_get_user(data))) / 1073741824))

class TeraByte(CommandBase):
    def __init__(self, settings):
        CommandBase.__init__(self,
                             settings.tb_command,
                             settings.tb_aliases,
                             settings.tb_message)

    def execute(self, Parent, data):
        Parent.SendStreamMessage(self.message.format(
            _get_username(data),
            float(Parent.GetPoints(_get_user(data))) / 1099511627776))

class PetaByte(CommandBase):
    def __init__(self, settings):
        CommandBase.__init__(self,
                             settings.pb_command,
                             settings.pb_aliases,
                             settings.pb_message)

    def execute(self, Parent, data):
        Parent.SendStreamMessage(self.message.format(
            _get_username(data),
            float(Parent.GetPoints(_get_user(data))) / 1125899906842624))
