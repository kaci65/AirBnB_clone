#!/usr/bin/python3
"""Main console module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""
    prompt = '(hbnb)' + ' '

    def do_quit(self, argument):
        """Quit command to exit program"""
        return True
    def do_EOF(self, argument):
        """exit program"""
        # ctrl_D
        return True
    def empty_line(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
