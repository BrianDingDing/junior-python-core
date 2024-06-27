# 路径: 从根目录开始计算(不包含根目录)
import package_01.package_public_01 as t

t.test01()

from package_01.package_public_01 import *

test01()

# result: package01, test01, test01
