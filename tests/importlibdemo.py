import importlib.util
import sys



name = 'os'

modules = sys.modules

if name in modules:
    print(f"{name!r} already in sys.modules")
elif (spec := importlib.util.find_spec(name)) is not None:
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    print(f"{name!r} has been imported")
else:
    print(f"can't find the {name!r} module")

import summer_boot.enviroment

file_path = summer_boot.enviroment.__file__
module_name = summer_boot.enviroment.__name__

spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
spec.loader.exec_module(module)
env = type(module.BaseEnvironment())
print(env.DEFAULT_APPLICATION_NAME)
