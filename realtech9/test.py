import os, sys

uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])
github_base_dir = uppath(__file__, 2)
print(github_base_dir)
sys.path.append(os.path.join(github_base_dir, 'PreProcessing'))

from Dictionary import kopro, sd
print(sd)
