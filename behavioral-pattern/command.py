#! /usr/bin/python

# -*- coding: utf8 -*-

from sys import stdout as console


# Handling 'exit' command
class SessionClosed(Exception):
    def __init__(self, value):
        self.value = value


# Interface
class AbstractCommand:
    def execute(self):
        raise NotImplementedError()

    def cancel(self):
        raise NotImplementedError()

    def name():
        raise NotImplementedError()


# ConcreteCommand (rm command)
class RmCommand(AbstractCommand):
    def execute(self):
        console.write("You are executed \"rm\" command\n")

    def cancel(self):
        console.write("You are canceled \"rm\" command\n")

    def name(self):
        return "rm"


# ConcreteCommand (uptime command)
class UptimeCommand(AbstractCommand):
    def execute(self):
        console.write("You are executed \"uptime\" command\n")

    def cancel(self):
        console.write("You are canceled \"uptime\" command\n")

    def name(self):
        return "uptime"


# ConcreteCommand (undo command)
class UndoCommand(AbstractCommand):
    def execute(self):
        try:
            cmd = HISTORY.pop()
            TRASH.append(cmd)
            console.write("Undo command \"{0}\"\n".format(cmd.name()))
            cmd.cancel()

        except IndexError:
            console.write("ERROR: HISTORY is empty\n")

    def name(self):
        return "undo"


# ConcreteCommand (redo command)
class RedoCommand(AbstractCommand):
    def execute(self):
        try:
            cmd = TRASH.pop()
            HISTORY.append(cmd)
            console.write("Redo command \"{0}\"\n".format(cmd.name()))
            cmd.execute()
        except IndexError:
            console.write("ERROR: TRASH is empty\n")

    def name(self):
        return "redo"


# ConcreteCommand (history command)
class HistoryCommand(AbstractCommand):
    def execute(self):
        i = 0
        for cmd in HISTORY:
            console.write("{0}: {1}\n".format(i, cmd.name()))
            i = i + 1

    def name(self):
        print "history"


# ConcreteCommand (exit command)
class ExitCommand(AbstractCommand):
    def execute(self):
        raise SessionClosed("See U next time!\n")

    def name(self):
        return "exit"

# Context
HISTORY = list()
TRASH = list()

# Invoker class
class Interpret:
    def __init__(self):
        # All supported command
        self.command = {'rm': RmCommand(),
                    'uptime': UptimeCommand(),
                    'undo': UndoCommand(),
                    'redo': RedoCommand(),
                    'history': HistoryCommand(),
                    'exit': ExitCommand()
        }

    def parse(self, expression):
        return self.command[expression]

# Client
def main():
    interpret = Interpret()
    try:
        while True:
            console.flush()
            console.write("pysh >> ")
            cmd = raw_input()
            try:
                command = interpret.parse(cmd)
                command.execute()
                if (not isinstance(command, UndoCommand) and not
                    isinstance(command, RedoCommand) and not
                    isinstance(command, HistoryCommand)):
                    TRASH = list()
                    HISTORY.append(command)
            except KeyError:
                console.write("ERROR: Command \"%s\" not supported\n" % cmd)
    except SessionClosed as e:
        console.write(e.value)

if __name__ == "__main__":
    main()
