## 小车环境搭建
#### 1.首先确定文件结构：
```
custom-gym/
|-- README.md
|-- setup.py
|-- custom_gym/
|   |-- __init__.py
|   |-- envs/
|   |   |-- __init__.py
|   |   |-- custom_env.py
|   |   |-- custom_env_extend.py
```
**一级目录为 __custom-gym.__** 你可以取任何不冲突的名字。包含setup.py(安装),README.md（说明书）和custom_gym文件夹（环境主体）。<br><br>
**二级目录为 __custom_gym.__** 包含__init__.py（初始化）和envs文件夹（环境脚本）。<br><br>
**三级目录为envs.** 包含__init__.py（初始化）和两个测试环境脚本custom_env.py和custom_env_extend.py（当然你也可以只测试一个或者多加几个试试）。<br>
#### 2.配置文件<br>
**custom-gym/setup.py**应该包含:
```
from setuptools import setup

setup(name='custom_gym',        # Secondary directory
    version='0.1',
    install_requires=['gym']    # And any other dependencies foo needs
)
```
**custom-gym/custom_gym/__ init__.py**应该包含：
```
from gym.envs.registration import register

register(
    id='custom_env-v0',                                   # Format should be xxx-v0, xxx-v1....
    entry_point='custom_gym.envs:CustomEnv',              # Expalined in envs/__init__.py
)
register(
    id='custom_env_extend-v0',
    entry_point='custom_gym.envs:CustomEnvExtend',
)
```
**custom-gym/custom_gym/envs/__ init__.py** 应该包含：
```
from custom_gym.envs.custom_env import CustomEnv
from custom_gym.envs.custom_env import CustomEnvExtend
```
**custom-gym/custom_gym/envs/custom_env.py** 应该包含：
```
import gym

class CustomEnv(gym.Env):
    def __init__(self):
        print('CustomEnv Environment initialized')
    def step(self):
        print('CustomEnv Step successful!')
    def reset(self):
        print('CustomEnv Environment reset')
```
这里省去了render，close等模块，之后的文章会在更具具体的问题来详细设置。这里只做展示目的。<br><br>
**同理，custom-gym/custom_gym/envs/custom_env_extend.py** 应该长这个样子：
```import gym

class CustomEnvExtend(gym.Env):
    def __init__(self):
        print('CustomEnvExtend Environment initialized')
    def step(self):
        print('CustomEnvExtend Step successful!')
    def reset(self):
        print('CustomEnvExtend Environment reset')

```
#### 3.安装与测试<br>
**切换目录到一级目录custom-gym**,就是包含setup.py这个文件夹。然后运行：
```
pip install -e .
```
#### 4.安装完成
