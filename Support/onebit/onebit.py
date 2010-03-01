from jinjalib import Template, Environment
import os

# if 'ONEBIT_DEV' in os.environ:
from jinjalib.loaders import FileSystemLoader
env = Environment(loader=FileSystemLoader(os.environ['TM_BUNDLE_SUPPORT']+'/onebit/templates'))
# else:
#     from jinjalib.code_loaders import FileSystemCodeLoader as FileSystemLoader
#     env = Environment(loader=FileSystemLoader(os.environ['TM_BUNDLE_SUPPORT']+'/onebit/templatesc'))
    
    

import commands
cmds = (
    {'test':'which java', 'error':'You do not have java installed.'},
)
for cmd in cmds:
    if commands.getoutput(cmd['test']) == '':
        import sys
        template = env.get_template("error.html")
        sys.exit(template.render(
            sdk=('ANDROID_SDK' in os.environ),
            title='Error', 
            error=cmd['error'],
        ))



