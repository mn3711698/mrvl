# -*- coding: utf-8 -*-

##############################################################################
# Author：QQ173782910
# linux支持python3.6 windows支持64位python3.8,python3.7
##############################################################################

import platform
try:
    from .base import Base
except:
    if platform.system() == 'Windows':
        if '3.8' in platform.python_version():
            try:
                from .base_w38 import Base
            except Exception as e:
                raise ValueError("请检查strategies目录下的是否存在base_w38文件", e)
        elif '3.7' in platform.python_version():
            try:
                from .base_w37 import Base

            except Exception as e:
                raise ValueError("请检查strategies目录下的是否存在base_w37文件", e)
        else:
            raise ValueError("该win的python版本未提供支持")
    elif platform.system() == 'Linux':
        if '3.6' in platform.python_version():
            try:
                from .base_l36 import Base
            except Exception as e:
                raise ValueError("请检查strategies目录下的是否存在base_l36文件", e)
        else:
            raise ValueError("该linux的python版本未提供支持")
    else:
        raise ValueError("操作系统未提供支持")
