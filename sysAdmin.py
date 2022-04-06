"""
system admin operations
"""

import os
import subprocess

#os.system('ls')

print('\n ls using subprocess')

subprocess.run('ls')

subprocess.run(["ls", "-l", 'README.md'])

cmd = 'df' #'ps' #'uname'
cmdArgument = '-h' #'-x' #'-a'

print(f'Gathering sys info with commadn : {cmd} {cmdArgument}')
subprocess.run([cmd, cmdArgument])
