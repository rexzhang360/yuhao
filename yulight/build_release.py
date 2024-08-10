# %%

from datetime import datetime
import time

# version = datetime.today().strftime('%Y%m%d')
from shutil import copyfile, make_archive
import os
from distutils.dir_util import copy_tree
from distutils.dir_util import remove_tree

version = "v3.6.0-rc.1"

# %%
for _ in range(2):
    try:
        remove_tree("./dist/yuhao")
    except:
        pass

# %%
os.makedirs("./dist/yulight")
os.makedirs("./dist/yulight/schema/yuhao")
# copyfile("./image/yulight.png", f"./dist/yulight/yulight_{version}.png")
copyfile("./beta/readme.md", f"./dist/yulight/readme.txt")
copyfile("./beta/schema/yuhao/yulight.full.dict.yaml", f"./dist/yulight.full.dict.yaml")
copyfile("../yujoy/beta/schema/yuhao.essay.txt", f"./beta/schema/yuhao.essay.txt")

copy_tree("./beta/mabiao", "./dist/yulight/mabiao")
copy_tree("./beta/schema", "./dist/yulight/schema")
copy_tree("./beta/hotfix", "./dist/yulight/hotfix")
copy_tree("./beta/trime", "./dist/yulight/trime")
copy_tree("./beta/custom", "./dist/yulight/custom")

# %%
# Hamster IME
make_archive(f"../dist/hamster/yuhao_light_{version}", "zip", "./dist/yulight/schema")

# %%
# Make zip
make_archive(f"../dist/yuhao_light_{version}", "zip", "./dist/yulight")
copyfile(f"../dist/yuhao_light_{version}.zip", f"../dist/宇浩光華_{version}.zip")

# %%
