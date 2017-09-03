import logging
import types
from modules import module_helloworld

#####################################
# Bad
# from proxy_lib import ProxySingleton

# Good
from proxies.proxy_lib import ProxySingleton, get_modules, get_path, get_fake_module
#####################################

FORMAT = '[%(filename)20s] %(funcName)18s : %(message)s'
logging.basicConfig(format=FORMAT)
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)


def start_execution():
    ProxySingleton().action(data=1)
    hello_world = module_helloworld.get_helloworld()
    _logger.info(hello_world)


if __name__ == "__main__":
    _logger.info("Modules:\n\t{}".format("\n\t".join(get_modules())))
    _logger.info("Path:\n\t{}".format("\n\t".join(get_path())))
    _logger.info("-"*30)

    _logger.info("Starting execution")
    ProxySingleton.setup(parameter=123)
    start_execution()

    new_proxy = get_fake_module(fake_module_name="proxy_lib_2")
    new_proxy.ProxySingleton.action(data=10)
    _logger.info("Modules:\n\t{}".format("\n\t".join(get_modules())))
