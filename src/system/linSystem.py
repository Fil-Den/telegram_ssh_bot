'''This file contains class system.
Class system is operation system abstraction
for command execution in Linux systems.
'''
import subprocess
from .system import ISystem


class LinSystem(ISystem):

    def runCommand(self, command):
        '''Run command in Lunux systems.'''
        command = command.split()
        try:
            result = subprocess.run(command, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            output = result.stdout.decode('utf-8', errors='replace')
            if not output.strip():
                output = result.stderr.decode('utf-8', errors='replace')
        except Exception as ex:
            output = "Error: " + str(ex)
        return output or ("Error")
