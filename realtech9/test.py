import os, sys

# uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])
# github_base_dir = uppath(__file__, 2)
# print(github_base_dir)
# sys.path.append(os.path.join(github_base_dir, 'PreProcessing'))
# 

# print(os.getcwd())
with open("uploads/lec00001_EBS.txt", 'r', encoding='utf-8') as f:
    a = f.read()
print(a)

# from Dictionary import sd
# print(sd)