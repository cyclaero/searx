import os, sys, subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'patch'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyyaml'])

os.chdir(os.path.dirname(__file__))

import requests
url = 'https://codeload.github.com/searx/searx/zip/master'
r = requests.get(url, allow_redirects=True)
open('searx-master.zip', 'wb').write(r.content)

from zipfile import ZipFile
with ZipFile('searx-master.zip', 'r') as zipObj:
	zipObj.extractall()

import shutil
shutil.copy('searx-master\\searx\\settings.yml', 'searx-settings.yml')
subprocess.check_call([sys.executable, '-m', 'patch', 'searx-settings.patch'])

os.chdir('searx-master')
infile  = open('searx\\webutils.py')
outfile = open('searx\\webutils.tmp', 'w')
for line in infile:
   outfile.write(line.replace('static_files.add(f)', 'static_files.add(f.replace("\\\\", "/"))').replace('result_templates.add(f)', 'result_templates.add(f.replace("\\\\", "/"))'))
infile.close()
outfile.close()
os.remove('searx\\webutils.py')
os.rename('searx\\webutils.tmp', 'searx\\webutils.py')

os.remove('searx\\settings.yml')
os.rename('..\\searx-settings.yml', 'searx\\settings.yml')

subprocess.check_call([sys.executable, 'setup.py', 'install'])

os.chdir(os.path.dirname(__file__))
shutil.rmtree('searx-master')
os.remove('searx-master.zip')
