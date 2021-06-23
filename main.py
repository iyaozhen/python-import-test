import os
import sys
import importlib
import builtins

if __name__ == '__main__':
    # 可能之前已经导入calendar模块
    import calendar

    temp_dir = "%s/temp_dir" % os.path.dirname(__file__)
    sys.path.insert(0, temp_dir)

    # builtin = False
    # for importer in sys.meta_path:
    #     if hasattr(importer, '_ORIGIN') and importer._ORIGIN == 'built-in':
    #         builtin = importer
    # if builtin:
    #     sys.meta_path.remove(builtin)
    print(sys.meta_path)
    print(sys.path_hooks)
    if 'calendar' in sys.modules:
        del sys.modules['calendar']
    print(sys.modules.keys())
    print(importlib.import_module("basic.package1"))
