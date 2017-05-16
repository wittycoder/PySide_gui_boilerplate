import os
from subprocess import call

for f in os.listdir('ui'):
    call('pyside-uic -o %s_ui.py ui%s%s' % (f[:-3], os.sep, f), shell=True)
