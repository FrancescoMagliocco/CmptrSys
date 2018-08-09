from abc import ABCMeta, abstractmethod

class CommandBase:
    __metaclass__ = ABCMeta
    _commands = {}

    def __init__(
            self, cmd, aliases, message, permission='Everyone', cooldown=0):
        self.command = cmd
        self.aliases = aliases
        self.message = message
        self.permission = permission
        self.cooldown = cooldown

        CommandBase._commands[self.command] = self

    @classmethod
    def is_command(cls, cmd):
        return any(cmd in cls._commands
                or cmd in v.aliases for v in cls._commands.values())

    @classmethod
    def get_command(cls, cmd):
        for k, v in cls._commands.items():
            if cmd == k or cmd in v.aliases:
                return v

        # TODO: Create a global command to be messaged
        # FIXME: cmd is not a valid command!
        return cls._commands[cmd]

    @abstractmethod
    def execute(self, Parent, data):
        pass
