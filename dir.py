import os

def tree(path, excluded=[], indent='|  ', sort='files-first', level=0):
  
  for name in filter(os.path.isfile, os.listdir(path)):
    if name not in excluded:
      print(f'{indent*level}{name}')

  for name in filter(os.path.isdir, os.listdir(path)):
    if name not in excluded:
      print(f'{indent*level}{name}/')
      tree(f'{path}/{name}', level=level+1)

tree(
  'C:/Users/Mikołaj/OneDrive/_projects/siir-task-1',
  [
    '.vscode',
    '.git',
    '.gitattributes',
    '.gitignore',
    'activate_venv.ps1',
    'quick_run.ps1',
    'dir.py',
    'dokument.txt',
    'README.md',
    'zadanie.zip',
    'venv'
  ]
)