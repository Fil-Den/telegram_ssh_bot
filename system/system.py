'''This file contains class system.
Class system is operation system abstraction
for command execution.
'''
import subprocess
from sys import platform


class System:

    def runCommand(self, command):
        '''run command. Command is string contains CLI command'''
        output = 'while not realized'
        if platform == "linux" or platform == "linux2":
            pass
        elif platform == "win32":
            output = self.__runCommandWindows(command)
        return output

    def __runCommandWindows(self, command):
        '''
        Run command in windows. Run command as:
            cmd /c chmod 65001 & command.
        Set 65001 encoding (Unicode) for next parse.
        '''
        command = (['cmd', '/c', 'chcp', '65001', '&']) + (command.split())
        try:
            result = subprocess.run(command, stdout=subprocess.PIPE)
            output = result.stdout.decode('utf-8', errors='replace')
            '''And remove first line from output, because first line is
                chmod 65001 output.'''
            output = output[output.find('\n'):]
        except Exception as ex:
            output = str(ex)
        return output


system = System()
