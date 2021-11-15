import os
import sys
import importlib

if __name__ == '__main__':
    # 直接或间接导入过calendar模块
    import mailbox

    # 模块目录加入到系统路径
    temp_dir = "%s/temp_dir" % os.path.dirname(__file__)
    sys.path.insert(0, temp_dir)

    # 去掉BuiltinImporter
    builtin = None
    for importer in sys.meta_path:
        if importer.__name__ == 'BuiltinImporter':
            builtin = importer
    if builtin:
        sys.meta_path.remove(builtin)

    # 去掉已加载的模块
    for exclude in ["calendar", "math"]:
        if exclude in sys.modules:
            del sys.modules[exclude]
    print(importlib.import_module("basic.package1"))
