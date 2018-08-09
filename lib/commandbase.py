import os
from abc import ABCMeta, abstractmethod

class Commands:
    __metaclass__ = ABCMeta
    commands = {}

    def __init__(self, cmd, alias, permission='Everyone', cooldown=0):
        self.command = cmd
        self.alias = [alias]
        self.permission = permission
        self.cooldown = cooldown

        Commands.commands[self.command] = self

    @classmethod
    def get_command(cls, cmd):
        return cls.commands[k if cmd == k or cmd in v.alias for k, v in cls.commands.items() else 'None']


        tmp = any(cmd in cls.commands or cmd in v.alias for v in
                cls.commands.values())
        return tmp

    @classmethod
    def is_command(cls, cmd):
        return any(cmd in cls.commands
                or cmd in v.alias for v in cls.commands.values())

    @abstractmethod
    def execute(self):
        pass

class Gibibyte(Commands):

    def __init__(self):
        Commands.__init__(self, '!gigabytes', ['!gigabyte', '!gb'])

    def execute(self):
        pass
