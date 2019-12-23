'''This file contains class system.
Class system is operation system abstraction
for command execution in Windows systems.
'''
import subprocess
from .system import ISystem


class WinSystem(ISystem):

    def runCommand(self, command):
        '''
        Run command in windows. Run command as:
            cmd /c chmod 65001 & command.
        Set 65001 encoding (Unicode) for next parse.
        '''
        command = (['cmd', '/c', 'chcp', '65001', '&']) + (command.split())
        try:
            result = subprocess.run(command, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            output = result.stdout.decode('utf-8', errors='replace')
            '''And remove first line from output, because first line is
                chmod 65001 output.'''
            output = output[output.find('\n'):]
            if not output.strip():
                output = result.stderr.decode('utf-8', errors='replace')
        except Exception as ex:
            output = "Error: " + str(ex)
        return output or ("Error")
