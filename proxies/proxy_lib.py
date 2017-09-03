from sys import modules, path
import types
import logging
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)


def get_modules(name="proxy_lib"):
    result = []
    for module_name in modules.keys():
        if name.lower() in module_name.lower():
            result.append("\t> {:20} : {}".format(module_name, modules[module_name]))
    return result


def get_path():
    result = []
    for dir in path:
        if dir.startswith("/usr"):
            continue
        result.append("\t- {}".format(dir))
    return result


def get_fake_module(fake_module_name):
    fake_module = types.ModuleType(fake_module_name)
    fake_module.__filename__ = "proxies/proxy_lib.py"
    code = compile(open(fake_module.__filename__, "r").read(), fake_module.__filename__, 'exec')
    exec(code, fake_module.__dict__)
    modules[fake_module_name] = fake_module
    return fake_module


class ProxySingleton(object):
    activated = False
    parameter = None

    @classmethod
    def setup(cls, parameter):
        cls.parameter = parameter
        cls.activated = True
        _logger.info("[ID:{}] Proxy service activated".format(id(cls)))

    @classmethod
    def action(cls, data):
        if not cls.activated:
            _logger.info("[ID:{}] Proxy is not activated. Skipping".format(id(cls)))
            return
        old_parameter = cls.parameter
        cls.parameter = data
        new_parameter = cls.parameter
        _logger.info("[ID:{}] Successfully executed action. Changed parameter from {} to {}".format(
            id(cls),
            old_parameter,
            new_parameter
        ))
