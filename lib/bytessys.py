from cmptrsysbase import CommandBase
# TODO: Have all these activated in one class to minimize code.
class Kilobyte(CommandBase):
    def __init__(self, settings):
        CommandBase.__init__(self,
                             settings.kb_command,
                             settings.kb_aliases,
                             settings.kb_message)

    def execute(self, Parent, data):
        Parent.SendStreamMessage(self.message.format(
            data, float(Parent.GetPoints(data.User)) / 1024))

class Megabyte(CommandBase):
    def __init__(self, settings):
        CommandBase.__init__(self,
                             settings.mb_command,
                             settings.mb_aliases,
                             settings.mb_message)

    def execute(self, Parent, data):
        Parent.SendStreamMessage(self.message.format(
            data, float(Parent.GetPoints(data.User)) / 1048576))

class Gigabyte(CommandBase):
    def __init__(self, settings):
        CommandBase.__init__(self,
                             settings.gb_command,
                             settings.gb_aliases,
                             settings.gb_message)

    def execute(self, Parent, data):
        Parent.SendStreamMessage(self.message.format(
            data, float(Parent.GetPoints(data.User)) / 1073741824))

class Terabyte(CommandBase):
    def __init__(self, settings):
        CommandBase.__init__(self,
                             settings.tb_command,
                             settings.tb_aliases,
                             settings.tb_message)

    def execute(self, Parent, data):
        Parent.SendStreamMessage(self.message.format(
            data, float(Parent.GetPoints(data.User)) / 1099511627776))

class Petabyte(CommandBase):
    def __init__(self, settings):
        CommandBase.__init__(self,
                             settings.pb_command,
                             settings.pb_aliases,
                             settings.pb_message)

    def execute(self, Parent, data):
        Parent.SendStreamMessage(self.message.format(
            data, float(Parent.GetPoints(data.User)) / 1125899906842624))
